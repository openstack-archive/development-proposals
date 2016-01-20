High Availability for Virtual Machines
======================================

*Problem description*
---------------------
Enterprise customers are moving their application workloads onto OpenStack
Cloud. However, not all applications can be re-architected into a Cloud-native
model at once. Some applications are deployed on a VM in a Pet model. This
requires high availability of such VM. Even though VM volumes can be stored on
a shared storage system, such as NFS or Ceph, to improve the availability, VM
state on each hypervisor is not easily replicated to other hypervisor.
Therefore, the system must be able to recover or rescue the VM from a failure
events preferably in an automated and cost effective manner.

User Stories
------------
Potentially there are few types of failure events:
* VM is down.
* VM provisioning process (nova-compute service) is down.
* Host/Hypervisor is down.
* Network is down
* Attached Cinder Volume failure
* Availability Zone/Data Center/Region failure


Usage Scenarios Examples
------------------------
* VM is down
Monitor the VM. Detect VM down failure and notify system to recover the VM.

* VM provisioning process is down
Monitor the provisioning process service (nova-compute service). Detect
process failure and notify system to restart the service.

* Host/Hypervisor is down
Monitor the hypervisor. Detect hypervisor failure and evaculate all VMs from
failure host to available hosts. Note: This scenario is feasible if a shared
storage is used for instance store or volume store as these volumes survices
outside the hypervisor.

Opportunity/Justification
-------------------------
Many enterprise customers requires HA VM feature in order to satisfy their
workload SLA. HA VM is a critical requirements for NTT customers.

Related User Stories
--------------------
To be determined.


*Requirements*
--------------
* An ability to monitor VM failure
* An ability to monitor provisioning process failure
* An ability to monitor hypervisor failure
* An ability to restart VM due to VM failure
* An ability to restart provisioning process.
* An ability to automatically evacuate VMs from a failure hosts to an
* available host.

*Gaps*
------
To be determined.


*Affected By*
-------------
To be determined.

*External References*
---------------------
https://github.com/ntt-sic/masakari

Glossary
--------
To be determined.

