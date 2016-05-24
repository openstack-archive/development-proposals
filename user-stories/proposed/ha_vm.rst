======================================
High Availability for Virtual Machines
======================================

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

*Problem Definition*
++++++++++++++++++++

Enterprise customers are moving their application workloads onto OpenStack
clouds. However, not all applications can be re-architected into a
Cloud-native model at once. Some applications are deployed on a VM in a pet
model. This requires high availability of such VMs. Even though VM volumes can
be stored on a shared storage system, such as NFS or Ceph, to improve the
availability, VM state on each hypervisor is not easily replicated to other
hypervisors. Therefore, the system must be able to recover the VM
from failure events, preferably in an automated and cost effective manner.

Opportunity/Justification
+++++++++++++++++++++++++

Many enterprise customers require highly available VMs in order to satisfy their
workload SLAs. For example, this is a critical requirement for NTT customers.

Use Cases
---------

User Stories
++++++++++++

As a cloud operator, I would like to provide my users with highly reliable
VMs to meet high SLA requirements. There are several types of failure
events that can occur in OpenStack clouds. We need to make sure such events
can be detected and recovered by the system. Possible failure events include:

* VM is down.

* VM hangs.

  For example, an issue with a VM's block storage (either its
  ephemeral disk or an associated Cinder volume) could cause the VM to
  hang, and the QEMU layer to emit a ``BLOCK_IO_ERROR`` which would
  bubble up through ``libvirt`` and could be detected and handled by
  an automated recovery process.

* VM provisioning process (nova-compute service) is down.

* Compute host is down.

* Hypervisor has failed (e.g. libvirtd process is dead or unresponsive).

* Network is down

  There are many ways a network component could fail, e.g. NIC
  configuration error, NIC driver failure, NIC hardware failure, cable
  failure, switch failure and so on. Any production environment aiming
  for high availability already requires considerable redundancy at
  the network level, especially voting nodes within a cluster which
  needs its quorum protecting against network partitions. Whilst this
  redundancy will keep most network hardware failures invisible to
  OpenStack, the remainder still need defending against. However, in
  order to fulfill this user story we don't need to be able to
  pinpoint the cause of a network failure; it's enough to recognise
  which network connection failed, and then react accordingly.

* Availability Zone/Data Center/Region failure

N.B. This user story concerns high availability, not 100% availability.
Therefore some service interruption is usually expected when failures occur.
The goal of the user story is to reduce that interruption via automated recovery.

Usage Scenario Examples
+++++++++++++++++++++++

* VM is down

  Monitor the VM. Detect VM down failure and notify system to recover the VM.

* VM provisioning process is down

  Monitor the provisioning process (nova-compute service). Detect
  process failure and notify system to restart the service.

  If it fails to restart the provisioning process, it should prevent scheduling
  any new VM instance onto the hypervisor/host that the process is running on.
  The operator can evacuate all VMs on this host to another healthy host and
  shutdown this host if it fails to restart the process. Prior to evacuation,
  the hosts must be fenced to prevent two instances writing to the same shared
  storage that lead to data corruption.

* Hypervisor host is down

  Monitor the hypervisor host. Detect hypervisor host failure and evacuate
  all VMs from failed host. Restart the VMs on new hosts that enable an
  application workload to resume a process if the VM state is stored in a
  volume even though it loses the state on memory. A shared storage can be
  used for instance volume as these volumes survive outside the hypervisors
  host.

* Recovery from network failure

  Typically the cloud infrastructure uses multiple networks, e.g.

  - an administrative network used for internal traffic such as the message bus,
    database connections, and Pacemaker cluster communication

  - various neutron networks

  - storage networks

  - remote control of physical hardware via IPMI / iLO / DRAC or similar

  Failures on these networks should not necessarily be handled in the same
  way.  For example:

  - If a compute host loses connection to the storage network, its VMs cannot
    continue to function correctly, so automatic fencing and resurrection is
    probably the only reasonable response.

  - If it loses connection to the admin network, its VMs should still continue
    to function correctly, so the cloud operator might prefer to receive
    alerts via email/SMS instead of any fencing and automated resurrection
    which would be needlessly disruptive.

  - If the compute host loses connection to the project (tenant) network, then
    it may be possible to fix this with minimal downtime by automatically
    migrating the VMs to another compute host.

  The desired response will vary from cloud to cloud, therefore should be
  configurable.

Related User Stories
++++++++++++++++++++
To be determined.


*Requirements*
++++++++++++++

* Flexible configuration of which VMs require HA

  Ideally it should be possible to configure which VMs require HA at
  several different levels of granularity, e.g. per VM, per flavor,
  per project, per availability zone, per host aggregate, per region,
  per cell.  A policy configuring a requirement or non-requirement for
  HA at a finer level of granularity should be able to override
  configuration set at a coarser level.  For example, an availability
  zone could be configured to require HA for all VMs inside it, but
  VMs booted within the availability zone with a flavor configured as
  not requiring HA would override the configuration at the
  availability zone level.

  However, it does not make sense to support configuration per compute
  host, since then VMs would inherit the HA feature
  non-deterministically, depending on whether ``nova-scheduler``
  happened to boot them on an HA compute host or a non-HA compute
  host.

* An ability to monitor VM failure.

* An ability to monitor provisioning process failure.

* An ability to monitor hypervisor host for failure

* An ability to automatically restart VMs due to VM failure

* An ability to restart provisioning processes

* An ability to automatically evacuate VMs from a failed hypervisor host
  and restart the VMs on another available host. The host must be fenced prior
  to the evacuation process to ensure that no 2 instances are writing to the
  same storage.

* An ability to disable the ``nova-compute`` service of a failed host so
  that ``nova-scheduler`` will not attempt to provision new VMs to that
  host before ``nova`` notices.

*External References*
+++++++++++++++++++++

* `Masakari (GitHub) <https://github.com/ntt-sic/masakari>`_
* `Automatic Evacuation (Etherpad) <https://etherpad.openstack.org/p/automatic-evacuation>`_
* `Instance Auto-Evacuation Cross Project Spec (In Review) <https://review.openstack.org/#/c/257809>`_

*Rejected User Stories / Usage Scenarios*
-----------------------------------------

None.

Glossary
--------

To be determined.
