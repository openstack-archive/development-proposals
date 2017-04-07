======================================
High Availability for Virtual Machines
======================================

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

*Problem Definition*
++++++++++++++++++++

Enterprise customers are moving their application workloads into OpenStack
clouds, for example to consolidate virtual estates, and benefit from increased
manageability and other economies of scale which OpenStack can bring.

However, it's typically impractical to re-architect all applications into a
purely cloud-native model at once. Therefore some applications, or parts
thereof, are deployed on non-disposable VMs in a pet model. This requires high
availability of such VMs. Even though VM volumes can be stored on a shared
storage system, such as NFS or Ceph, to improve the availability, VM state on
each hypervisor is not easily replicated to other hypervisors. Therefore, the
system must be able to recover the VM from failure events, preferably in an
automated and cost-effective manner.

Even for applications architected in a cloud-native "cattle" model which can
tolerate failures of individual VMs, at scale it is too impractical and costly
to have to manually recover every failure. Ideally this auto-recovery would be
implemented in the application or PaaS layer, to maximise integration with the
rest of the application. However even if a new feature implemented the
OpenStack layer primarily targeted auto-recovery of pets, it could also serve
as a cheap alternative for auto-recovery of cattle.

Opportunity/Justification
+++++++++++++++++++++++++

Many enterprise customers require highly available VMs in order to satisfy their
workload SLAs. For example, this is a critical requirement for NTT customers.

Requirements Specification
--------------------------

Use Cases
+++++++++

As a cloud operator, I would like to provide my users with highly available
VMs to meet high SLA requirements. There are several types of failure
events that can occur in OpenStack clouds. We need to make sure such events
can be detected and recovered by the system. Possible failure events include:

* VM crashes.

  For example, with the KVM hypervisor, the ``qemu-kvm`` process could crash.

* VM hangs.

  For example, an issue with a VM's block storage (either its
  ephemeral disk or an associated Cinder volume) could cause the VM to
  hang, and the QEMU layer to emit a ``BLOCK_IO_ERROR`` which would
  bubble up through ``libvirt`` and could be detected and handled by
  an automated recovery process.

* ``nova-compute`` service crashes or becomes unresponsive.

* Compute host crashes or hangs.

* Hypervisor fails, e.g. libvirtd process dies or becomes unresponsive.

* Network component fails.

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

* Availability Zone failure

* Data Center / Region failure

  Failure of a whole region or data center is obviously much more severe,
  requiring recovery of not just compute nodes but also OpenStack services in
  the control plane.  It needs to be covered by a Disaster Recovery plan,
  which will vary greatly for each cloud depending on its architecture,
  supported workloads, required SLAs, and organizational structure.  As such,
  a general solution to Disaster Recovery is a problem of considerable
  complexity, therefore it makes sense to keep it out of scope for this user
  story, which should instead be viewed as a necessary and manageable step on
  the long road to that solution.

As a cloud operator, I need to reserve a certain number of hypervisors so that
they can be used for failover hosts in case of a host failure event. This is
required for planning in order to meet an expected SLA. The number of failover
hosts depends on the expectation of VM availability (SLA), the size of the host
pool (failover segment), the possibility of host failures and the MTTR of host
failure, all of which are managed by the cloud operator.

The size of host pool (failover segment) is a pre-defined boundary for hosts
which they can find a healthy host to failover. These boundaries can defined as
"hosts are in same shared storage", "host aggregates", etc..

As a cloud operator, I need to perform host maintenances. I need to temporarily
and safely disable the HA mechanism for the affected hosts in order to perform
the maintenance task. Disabling HA mechanism for a host means that all alerts
from that host shall be neglected and no recovery action shall be taken.
For recovery, the actions are not limited to fencing, but nova server stop and
start, process restart on the host may also be a subject of the recovery
action.

As a cloud operator, I need to respond to customer issues and perform
troubleshooting. I need to know the history of what, when, where and how the
HA mechanism is performed. This information is used to better understand the
state of the system.

N.B. This user story concerns high availability, not 100% availability.
Therefore some service interruption is usually expected when failures occur.
The goal of the user story is to reduce that interruption via automated recovery.

Usage Scenario Examples
+++++++++++++++++++++++

* Recovery from VM failure

  Monitor the VM externally (i.e. as a black box, without requiring
  any knowledge of or invasive changes to the internals of the
  VM). Detect VM failure and notify system to recover the VM on the same
  hypervisor, or if that fails, on another hypervisor.

  Note that failures of the VM which are undetectable from outside it
  are out of scope of this user story, since they would require invasive
  monitoring inside the VM, and there is no general solution to this which
  would work across all guest operating systems and workloads.

* Recovery from ``nova-compute`` failure

  Monitor the provisioning process (nova-compute service). Detect
  process failure and notify system to restart the service.

  If it fails to restart the provisioning process, it should prevent scheduling
  any new VM instance onto the hypervisor/host that the process is running on.
  The operator can evacuate all VMs on this host to another healthy host and
  shutdown this host if it fails to restart the process. Prior to evacuation,
  the hosts must be fenced to prevent two instances writing to the same shared
  storage that lead to data corruption.

* Recovery from hypervisor host failure

  Monitor the hypervisor host. When failure is detected, resurrect
  all VMs from the failed host onto new hosts that enable an
  application workload to resume a process if the VM state is stored in a
  volume even though it loses the state on memory. If shared storage is used
  for instance volumes, these volumes survive outside the failed hypervisor
  host. However this is not required. If shared storage is not available,
  the instance VMs will be automatically rebuilt from their original image, as
  per standard nova evacuate behaviour.

  The design of the infrastructure, and its boundary of each subsystem such as
  shared storage, may restrict the deployment of VM instances and the
  candidates of failover hosts. To use nova-evacuate API to restart VM
  instances, the original hypervisor host and target hypervisor host need to
  connect to the same shared storage. Therefore, a cloud operator defines the
  segment of hypervisor hosts and assigns the failover hosts to each segments.
  These segments can be defined based on the shared storage boundaries or any
  other limitations critical for selecting the failover host.

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

* Capacity Reservation

  In order to ensure the uptime of VM instance, the operator needs to ensure a
  certain amount of host capacity is reserved to cater for a failure event. If
  there is not enough host capacity and a host failure event happens, the VM
  on the failure host cannot be evacuated to another host. It is assumed that
  there is equivalent host within the fault boundaries. If not, a more
  complicated logic (e.g. SR-IOV, DMTC, QoS requirements) will be required in
  order to reserve the capacity.

  The host capacity of the overall system is typically fragmented into segments
  due to the underlying component’s scalability and each segment has a limited
  capacity. To increase resource efficiency, high utilization of host capacity
  is preferred. However, as resources are consumed on demand, each segment
  tends to reach nearly full capacity if the system doesn’t provide a way to
  reserve a portion of host capacity. Therefore, a function to reserve host
  capacity for failover events is important in order to achieve high
  availability of VMs.

* Host Maintenance

  A host has to be temporarily and safely removed from the overall system for
  maintenances such as hardware upgrade and firmware update. Live migration
  should be triggered after putting node into maintenance prior to maintenance.
  During maintenance, the monitoring function on the host should be disabled
  and the monitoring alert for the host should be ignored. There should be no
  triggering of any recovery action of VM instances on the host if it’s
  running. The host should be excluded from reserved hosts as well.

* Event History

  History of the past events such as process failures, VM failures and host
  failures are useful information to determine the required maintenance work of
  a host. An easy mechanism to track past events can save operator time from
  system diagnosis. These APIs can also be used to generate the health or SLA
  report of the VM availability status.

Related User Stories
++++++++++++++++++++

* `Quotas, Usage Plans, and Capacity Management <http://specs.openstack.org/openstack/openstack-user-stories/user-stories/draft/capacity_management.html>`_

  The concept of capacity reservation is common with this story. The difference
  is that the story provides the reservation for users where this VM-HA story
  provides the reservation for specific contexts of resource inquiry such as
  aninstance evacuation, not for an instance creation.

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

* An ability to non-intrusively monitor VMs for failure

* An ability to monitor provisioning processes on the compute host for failure

  Provisioning processes include ``nova-compute``, associated backend
  hypervisor processes such as ``libvirtd``, and any other dependent
  services, e.g. ``neutron-openvswitch-agent`` if Open vSwitch is in use.

* An ability to monitor hypervisor host failure

* An ability to automatically restart VMs due to VM failure

  The restart should first be attempted on the same compute host, and if that
  fails, it should be attempted elsewhere.

* An ability to restart provisioning process

* An ability to automatically resurrect VMs from a failed hypervisor host
  and restart them on another available host

  The host must be fenced (typically via a STONITH mechanism) prior to the
  resurrection process, to ensure that there are never multiple instances of
  the same VM accidentally running concurrently and conflicting with each
  other.  The conflict could cause data corruption, e.g. if both instances are
  writing to the same non-clustered filesystem backed by a virtual disk on
  shared storage, but it could also cause service-level failures even without
  shared storage.  For example, a VM on a failing host could still be
  unexpectedly communicating on a project network even when the host is
  unreachable via the cluster network, and this could conflict with
  another instance of the same VM resurrected on another compute host.

* An ability to disable the ``nova-compute`` service of a failed host so
  that ``nova-scheduler`` will not attempt to provision new VMs to that
  host before ``nova`` notices.

* An ability to make sure the target host for VM evacuation is aligned with the
  underlying system boundaries and limitations

* An ability to reserve hypervisor host capacity and update the capacity in the
  event of a host failure

* An ability for operator to coordinate with host maintenance tasks

* An ability to check the history of failure and recovery actions

*External References*
+++++++++++++++++++++

* `Automatic Evacuation (Etherpad) <https://etherpad.openstack.org/p/automatic-evacuation>`_

* `Instance Auto-Evacuation Cross Project Spec (In Review) <https://review.openstack.org/#/c/257809>`_

* `Instance HA Discussion (Etherpad) <https://etherpad.openstack.org/p/newton-instance-ha>`_

* `High Availability for Pets and Hypervisors (Video) <https://youtu.be/lddtWUP_IKQ>`_

* `Masakari (GitHub) <https://github.com/ntt-sic/masakari>`_

* `Masakari API Design <https://github.com/ntt-sic/masakari/wiki/Masakari-API-Design>`_

*Rejected User Stories / Usage Scenarios*
-----------------------------------------

None.

Glossary
--------

* **MTTR** - Mean Time To Repair

* `Availability <https://en.wikipedia.org/wiki/Availability>`_ -
  ratio of the expected value of the uptime of a system
  to the aggregate of the expected values of up and down time.
  Not to be confused with
  `reliability <https://en.wikipedia.org/wiki/Reliability_engineering>`_.

* `High Availability <https://en.wikipedia.org/wiki/High_availability>`_ -
  a characteristic of a system which aims to ensure an agreed level of
  operational performance for a higher than normal period.  Not to be
  confused with 100% availability, which is sometimes described as
  `fault tolerance <https://en.wikipedia.org/wiki/Fault_tolerance>`_.

* `Pets and cattle
  <http://www.theregister.co.uk/2013/03/18/servers_pets_or_cattle_cern/>`_ -
  a metaphor commonly used in the OpenStack community to describe the
  difference between two service architecture models: cloud-native,
  stateless, disposable instances with built-in resilience in the
  application layer (cattle), vs. legacy, stateful instances with no
  built-in resilience (pets).
