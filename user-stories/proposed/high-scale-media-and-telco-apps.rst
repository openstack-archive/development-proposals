===========================
High Scale Media Telco Apps
===========================

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

This use case is specifically about deploying the Perimeta Session Border
Controller (SBC) Virtual Network Function (VNF) from Metaswitch Networks in
OpenStack.

Perimeta, like other SBCs, sits on the edge of a service provider's network and
polices SIP and RTP (i.e. VoIP) control and media traffic passing over both

* the access network between end-users and the core network
* the trunk network between the core and another service provider

.. code-block:: text

    Access     +      SP A core      +    Trunk        +      SP B core
    network    |      network        |    network      |      network
               |                     |                 |
               |                     |                 |
  +-------+  +-+--+   +---------+  +-+--+            +-+--+   +---------+
  |User   |  |SBC |   |Network  |  |SBC |            |SBC |   |Network  |
  |device |--|    |---|function |--|    |------------|    |---|function |
  +-------+  +-+--+   +---------+  +-+--+            +-+--+   +---------+
               |                     |                 |
               +                     +                 +

See the Glossary for a description of these terms.

In order to implement its security and admission control functions (e.g. DDoS
protection), Perimeta must perform line-rate processing of received packets.
For RTP streams, this equates to several million VoIP packets (each ~64-220
bytes depending on codec) per second per core.  Perimeta must be able to
guarantee this performance and offer SLAs.

Perimeta must be fully HA, with no single points of failure, and service
continuity over both software and hardware failures (i.e. all SIP sessions and
RTP sessions must continue with minimal interruption over software or hardware
failures).

Perimeta must be elastically scalable, enabling an NFV orchestrator to add and
remove instances in response to applied load.

To apply different policies to traffic from different customers, Perimeta must
be able to distinguish and separate traffic from different customers via VLANs
or similar mechanism.

Perimeta must separate networks carrying live customer traffic from networks
carrying management or other internal data.

Perimeta signaling instances must be able to support large numbers of
concurrent TCP connections (hundreds of thousands) to cater for large numbers
of clients using TCP.

Perimeta must be able to coexist with VMs which do not have these requirements
on the same host, so long as it can provide sufficient dedicated resources.
For example, just because Perimeta may not require security group function it
does not mean this can be disabled at a host scope, or just because Perimeta
uses SR-IOV or DPDK it does not mean that all VMs on that host must do so.

Opportunity/Justification
+++++++++++++++++++++++++

Although this user story is specifically about Perimeta, it is more generally
representative of the issues involved in deploying in OpenStack any VNF
utilising a fast data plane or high scale SIP.  The use case focuses on those
elements rather than more generic issues like orchestration and high
availability (HA).

Requirements Specification
--------------------------

Use Cases
+++++++++

* As a communication service provider, I want to deploy a highly available,
  high scale, high performance Session Border Controller on OpenStack to police
  VoIP traffic at the edge of my network.

Usage Scenarios Examples
++++++++++++++++++++++++

The Perimeta Session Border controller from Metaswitch Networks is a
Telco-grade implementation of a Session Border Controller designed to run
either on generic PC hardware or virtualized, running on OpenStack and other
clouds, providing high availability, high scale and high performance.

Related User Stories
++++++++++++++++++++

None.

*Requirements*
++++++++++++++

The problem statement above leads to the following requirements.

* Achieving packets per second target - networking implications

  A standard OpenStack/OpenvSwitch platform allows VMs to drive NICs to full
  bandwidth if using large packet sizes typical for Web applications. What
  makes VoIP different is the small packet size, which means order of magnitude
  more packets and permits only a few hundred CPU instructions per packet -
  nowhere near enough to drive a packet through the standard OpenStack
  networking stack from VM to NIC.  Instead, this requires technologies such
  as SR-IOV (https://blueprints.launchpad.net/nova/+spec/pci-passthrough-sriov
  - completed in 2014.2, though with some technical debt remaining) or a DPDK
  or similar poll mode based vSwitch in the host. Note that SR-IOV in
  particular imposes some limitations (e.g. prevents live migration) so may not
  be a desirable option for some SPs.

  Ideally the network would support and respect QoS rules on traffic priority
  and bandwidth limits.

* Security - networking implications

  Security groups must be disabled for network technologies where they are
  not bypassed completely.

  The network should protect against ARP poisoning attacks from other VMs.

* High scale TCP - networking implications

  For ports with security group function disabled, it is desirable that host
  connection tracking function is disabled to avoid performance and occupancy
  hits for large numbers of TCP connections and the need to tune host
  parameters unnecessarily.

* Achieving packets per second target - compute implications

  * To achieve line rate all the working data for processing RTP streams
    (active flows etc.) must be kept in L3 cache - main memory look-ups are too
    slow. That requires pinning guest vCPUs to host pCPUs.

  * To optimise the data flow rate it is desirable to bind to a NIC on the host
    CPU's bus.

  * To offer performance SLAs rather than simply "best efforts" we need to
    control the placement of cores, minimise transaction lookaside buffer (TLB)
    misses and get accurate info about core topology (threads vs. hyperthreads
    etc).

* HA

  Perimeta must be deployable to provide a 5 9's level of availability.  If
  deployed in a single cloud instance, that instance must therefore itself be
  more than 5 9's available.  As that is hard to achieve with today's state of
  the art, Perimeta is designed to be able to span multiple independent cloud
  instances, so that the failure of any one cloud has a minor impact.  The
  requirements that creates are still being discussed and will be addressed in
  a future use case.

  When deploying Perimeta within a single cloud instance, Perimeta uses an
  active/standby architecture with an internal heartbeat mechanism allowing the
  standby to take over within seconds of failure of the active, including
  taking over its IP address.  To support these application level HA mechanisms
  requires:

  * support for anti-affinity rules to permit the active and standby being
    instantiated on the same host

  * support for application-controlled virtual IPs via gratuitous ARP based
    scheme (for IPv4) and NDP Neighbour Advertisements (for IPv6); in both
    cases the standby sends messages saying it now owns the virtual IP address.

  The former is supported through standard anti-affinity nova scheduler rules,
  and the latter through the neutron allowed-address-pairs extension.

  If using SR-IOV, Perimeta does not need multiple SR-IOV ports, as
  application level redundancy copes with the failure of a single NIC. However,
  it can take advantage of local link redundancy using multiple SR-IOV vNICs.
  For this to be of any benefit requires the SR-IOV VFs forming a redundant
  pair to be allocated on separate PFs.

  Additionally, it is clearly desirable that the underlying cloud instance is
  as available as possible e.g. no single points of failure (SPOFs) in the
  underlying network or storage infrastructure.

* Elastic scaling

  An NFV orchestrator must be able to rapidly launch or terminate new Perimeta
  instances in response to applied load and service responsiveness.  This is
  basic OpenStack nova function.

* Support for a scalable mechanism to support multiple networks in a VM

  There must be a scalable mechanism to present multiple networks to Perimeta,
  of order hundreds or thousands, so far exceeding the number of vNICs that can
  be attached.  Various mechanisms are possible; a common one, and the one
  that Perimeta supports, is for different customer networks to be presented
  over VLANs.  This creates a guest requirement for VLAN trunking support.

  There are multiple possible ways of mapping networks to these VLANs within
  OpenStack, for example, trunking external VLAN networks directly to the VMs
  with minimal OpenStack knowledge or configuration (already supported in Kilo)
  or configuring the mapping between OpenStack networks and VLANs as covered in
  VLAN aware VMs: https://blueprints.launchpad.net/neutron/+spec/vlan-aware-vms

*External References*
+++++++++++++++++++++

None.

*Rejected User Stories / Usage Scenarios*
-----------------------------------------

None.

Glossary
--------

**NFV**
  Network Functions Virtualization, the vision of deploying telecoms functions
  as virtual applications running on commercial off the shelf hardware.

**VNF**
  Virtual Network Function - a telecoms or other network function running as
  a virtual application.

**SIP**
  Session Initiation Protocol (RFC 3261) - a common application-layer control
  protocol for creating, modifying and destroying sessions between two or more
  participants.

**RTP**
  Real-time Transport Protocol (RFC 3550) - an end-to-end network transport
  protocol for transmitting real-time data like audio and video.

**VoIP**
  Voice over Internet Protocol - delivering voice and multimedia sessions over
  IP networks, commonly through the use of SIP + RTP.

**SBC**
  Session Border Controller, a telecoms function which polices SIP and RTP
  flows, providing security, quality of service, admission control and interop
  services.

**DDoS**
  Distributed Denial of Service - a form of packet flood attack.

**SLA**
  Service Level Agreement - contractual commitment to reach certain performance
  and availability targets.

**SR-IOV**
  Single Root I/O Virtualisation - a technique for presenting a single physical
  PCIe device (such as a NIC) as multiple virtual devices, directly presented
  to VMs.

**DPDK**
  Data Plane Development Kit - a set of libraries and drivers for fast packet
  processing.
