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
hypervisors. Therefore, the system must be able to recover or rescue the VM
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

* VM provisioning process (nova-compute service) is down.

* Host/Hypervisor is down.

* Network is down

* Attached Cinder volume failure

* Availability Zone/Data Center/Region failure


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

Related User Stories
++++++++++++++++++++
To be determined.


*Requirements*
++++++++++++++

* An ability to tag VMs that require HA.

* An ability to monitor VM failure.

* An ability to monitor provisioning process failure.

* An ability to monitor hypervisor host for failure

* An ability to automatically restart VMs due to VM failure

* An ability to restart provisioning processes

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
  unreachable via the cluster network, and this could conflict with the
  another instance of the same VM resurrected on another compute host.

* An ability to disable a failed host from nova scheduler

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
