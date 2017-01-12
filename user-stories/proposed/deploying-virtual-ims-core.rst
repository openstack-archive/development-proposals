Virtual IMS Core
================

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

*Problem Definition*
++++++++++++++++++++
This use case is about deploying a virtual IMS core as an NFV function in
OpenStack.  It replaces the version previously uploaded to the TelcoWG
repository [1].

An IMS core [2] is a key element of Telco infrastructure, handling VoIP device
registration and call routing.  Specifically, it provides SIP-based call
control for voice and video as well as SIP based messaging apps.

An IMS core is mainly a compute application with modest demands on
storage and network - it provides the control plane, not the media plane
(packets typically travel point-to-point between the clients) so does not
require high packet throughput rates and is reasonably resilient to jitter and
latency.

As a core Telco service, the IMS core must be deployable as an HA service
capable of meeting strict Service Level Agreements (SLA) with users.  Here
HA refers to the availability of the service for completing new call
attempts, not for continuity of existing calls.  As a control plane rather
than media plane service the user experience of an IMS core failure is
typically that audio continues uninterrupted but any actions requiring
signalling (e.g.  conferencing in a 3rd party) fail.  However, it is not
unusual for client to send periodic SIP "keep-alive" SIP pings during a
call, and if the IMS core is not able to handle them the client may tear
down the call.

An IMS core must be highly scalable, and as an NFV function it will be
elastically scaled by an NFV orchestrator running on top of OpenStack.
The requirements that such an orchestrator places on OpenStack are not
addressed in this use case.

Opportunity/Justification
+++++++++++++++++++++++++

Although this user story is specifically about deploying the Project
Clearwater virtual IMS core, it is more generally representative of the
issues involved in deploying in OpenStack any scalable Telco-grade control
plane Virtual Network Function (VNF) deployed as a series of load-balanced
stateless N+k pools.

Use Cases
---------

User Stories
++++++++++++

* As a communication service provider, I want to deploy a highly available,
  high scale, high performance virtual IMS core on OpenStack to provide my core
  Voice-over-IP service.

Usage Scenario Examples
+++++++++++++++++++++++

Project Clearwater [3] is an open-source implementation of an IMS core
designed to run in the cloud and be massively scalable.  It provides
P/I/S-CSCF functions together with a BGCF and an HSS cache, and includes a
WebRTC gateway providing interworking between WebRTC & SIP clients.

Related User Stories
++++++++++++++++++++

None.

*Requirements*
++++++++++++++

The problem statement above leads to the following requirements.

* Compute application

  OpenStack already provides everything needed; in particular, there are no
  requirements for an accelerated data plane, nor for core pinning nor NUMA.

* HA

  Project Clearwater itself implements HA at the application level, consisting
  of a series of load-balanced N+k pools with no single points of failure [4].

  To meet typical SLAs, it is necessary that the failure of any given host
  cannot take down more than k VMs in each N+k pool.  More precisely, given
  that those pools are dynamically scaled, it is a requirement that at no time
  is there more than a certain proportion of any pool instantiated on the
  same host.

  That by itself is insufficient for offering an SLA, though: to be deployable
  in a single OpenStack cloud (even spread across availability zones or
  regions), the underlying cloud platform must be at least as reliable as the
  SLA demands.  Those requirements will be addressed in a separate use case.

* Elastic scaling

  An NFV orchestrator must be able to rapidly launch or terminate new
  instances in response to applied load and service responsiveness.  This is
  basic OpenStack nova function.

* Placement zones

  In the IMS architecture there is a separation between access and core
  networks, with the P-CSCF component (Bono - see [4]) bridging the gap
  between the two.  Although Project Clearwater does not yet support this,
  it would in future be desirable to support Bono being deployed in a
  DMZ-like placement zone, separate from the rest of the service in the main
  MZ.

*External References*
+++++++++++++++++++++

* [1] https://review.openstack.org/#/c/179142/
* [2] https://en.wikipedia.org/wiki/IP_Multimedia_Subsystem
* [3] http://www.projectclearwater.org
* [4] http://www.projectclearwater.org/technical/clearwater-architecture/

Rejected User Stories / Usage Scenarios
---------------------------------------
None.

Glossary
--------

* NFV - Networks Functions Virtualisation, see http://www.etsi.org/technologies-clusters/technologies/nfv
* IMS - IP Multimedia Subsystem
* SIP - Session Initiation Protocol
* P/I/S-CSCF - Proxy/Interrogating/Serving Call Session Control Function
* BGCF - Breakout Gateway Control Function
* HSS - Home Subscriber Server
* WebRTC - Web Real-Time-Collaboration
