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
Cloud. However, not all applications can be re-architected into a
Cloud-native model at once. Some applications are deployed on a VM in a Pet
model. This requires high availability of such VM. Even though VM volumes can
be stored on a shared storage system, such as NFS or Ceph, to improve the
availability, VM state on each hypervisor is not easily replicated to other
hypervisor. Therefore, the system must be able to recover or rescue the VM
from a failure events preferably in an automated and cost effective manner.

Opportunity/Justification
+++++++++++++++++++++++++

Many enterprise customers requires HA VM feature in order to satisfy their
workload SLA. For example, HA VM is a critical requirements for NTT customers.

Use Cases
---------

User Stories
++++++++++++

As a cloud operator, I would like to provide my users with highly reliable
VM to meet high SLA requirement. Potentially there are few types of failure
events that can occurs with OpenStack Cloud. We need to make sure such events
can be detected and recovered by the system. Possible failure events include:

* VM is down.

* VM provisioning process (nova-compute service) is down.

* Host/Hypervisor is down.

* Network is down

* Attached Cinder Volume failure

* Availability Zone/Data Center/Region failure

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

Usage Scenarios Examples
++++++++++++++++++++++++

* VM is down

  Monitor the VM. Detect VM failure and notify system to recover the VM. If
  the VM is down and host is healthy, one option is to take recovery actions
  on the same host. These recovery actions may be restart the VM or send a
  notification to operator, which must be comply with the SLA as VM can be
  taken down when the cloud is out of resources.

* VM provisioning process is down

  Monitor the provisioning process (nova-compute service). Detect
  process failure and notify system to restart the service.

  If it fails to restart the provisioning process, it should stop scheduling
  a new VM instance onto the hypervisor/host that the process is running on.
  The operator can evacuate all VMs on this host to another healthy host and
  shutdown this host if it fails to restart the process. Prior to evacuation,
  the hosts must be fenced to prevent 2 instances writing to the same shared
  storage that lead to data corruption.

* Hypervisor host is down

  Monitor the hypervisor host. Detect hypervisor host failure and evacuate
  all VMs from failure host. Restart the VMs on new hosts that enable an
  application workload to resume a process if the VM state is stored in a
  volume even though it loses the state on memory. A shared storage can be
  used for instance volume as these volumes survive outside the hypervisors
  host.

  The design of the infrastructure, and its boundary of each subsystem such as
  shared storage, may restrict the deployment of VM instances and the
  candidates of failover hosts. To use nova-evacuate API to restart VM
  instances, the original hypervisor host and target hypervisor host need to
  connect to the same shared storage. Therefore, a cloud operator defines the
  segment of hypervisor hosts and assigns the failover hosts to each segments.
  These segments can be defined based on the shared storage boundaries or any
  other limitations critical for selecting the failover host.

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
To be determined.


*Requirements*
++++++++++++++

* An ability to tag VMs that require HA by the user and cloud operator. More
  information can be included such as requiring HA at different levels, such
  as region, AZ, host aggregage, compute host, project, cell, etc.

* An ability to remove the tag so that the user and cloud operator can
  temporary or permanently disable HA for certain VMs

* An ability to monitor VM failure

* An ability to monitor provisioning process failure

* An ability to monitor hypervisor host failure

* An ability to restart VM due to VM failure

* An ability to restart provisioning process

* An ability to automatically evacuate VMs from a failure hypervisor host
  and restart the VMs on other available host. The host must be fenced prior
  to the evacuation process to ensure that no 2 instances are writing to the
  same storage.

* An ability to disable a failure host from nova scheduler

* An ability to make sure the target host for VM evacuation is aligned with the
  underlying system boundaries and limitations

* An ability to reserve hypervisor host capacity and update the capacity in the
  event of a host failure

* An ability for operator to coordinate with host maintenance tasks

* An ability to check the history of failure and recovery actions

*External References*
+++++++++++++++++++++

https://github.com/ntt-sic/masakari

https://github.com/ntt-sic/masakari/wiki/Masakari-API-Design

https://etherpad.openstack.org/p/automatic-evacuation

https://etherpad.openstack.org/p/newton-instance-ha

https://review.openstack.org/#/c/257809

https://youtu.be/lddtWUP_IKQ

*Rejected User Stories / Usage Scenarios*
-----------------------------------------

None.

Glossary
--------
* **MTTR** - Mean Time To Repair
