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


Usage Scenarios Examples
++++++++++++++++++++++++

* VM is down

  Monitor the VM. Detect VM down failure and notify system to recover the VM.

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

Related User Stories
++++++++++++++++++++
To be determined.


*Requirements*
++++++++++++++

* An ability to tag VMs that require HA.

* An ability to monitor VM failure.

* An ability to monitor provisioning process failure.

* An ability to monitor hypervisor host failure.

* An ability to restart VM due to VM failure.

* An ability to restart provisioning process.

* An ability to automatically evacuate VMs from a failure hypervisor host
  and restart the VMs on other available host. The host must be fenced prior
  to the evacuation process to ensure that no 2 instances are writing to the
  same storage.

* An ability to disable a failure host from nova scheduler.

*External References*
+++++++++++++++++++++

* https://github.com/ntt-sic/masakari
* https://etherpad.openstack.org/p/automatic-evacuation
* https://review.openstack.org/#/c/257809

*Rejected User Stories / Usage Scenarios*
-----------------------------------------

None.

Glossary
--------

To be determined.

