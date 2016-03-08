Bare Metal Service
==================

Cross Project Spec - None

User Story Tracker - None

Problem description
====================

*Problem Definition*
--------------------

In order to support certain Enterprise Business Requirements, OpenStack must
be able to provision bare metal machines in a secure, multi-tenant, and
highly-available fashion, while providing the same integration with other
OpenStack services (such as volume storage, console access, etc) as it does
for virtual machines.

Some use cases for bare metal machines are:

#. Performance-sensitive applications that want to maximize efficiency, reduce
   overhead from virtualization, and avoid CPU, Network, or IO fluctuations
   from neighboring instances.

#. Security-sensitive applications, or applications with regulatory compliance
   requirements that can not be run on shared hardware.

#. Applications whose licensing costs depend on # of CPUs on the Host, regardles
   of whether virtualization is in play.

#. Applications that need direct IO access to specialized PCI devices which are
   not yet virtualizable.

To support these use cases, we need:

#. Bare metal machine configuration: Bare metal machine can be configured with
   CPU specification, memory capacity, local storage drive type such as SATA
   or SSD and it's capacity, and network iplink bandwidth. Infiniband or RoCEE
   may be needed to achieve network performance.

#. Network Isolation: Networks for one tenant is isolated from other tenants.

#. Storage Service Integration: Bare metal machine can be connected with block
   device service such as Cinder. Bare metal machine connects cinder backends
   dedicated to single tenant. Tenant can also back up internal storage of
   bare metal machine and recover from it.

#. Console: Tenant can operate bare metal machine from console, see console log
   integrated with existing Horizon UI.

#. Unified VM/BM Management: Unified management of both VMs and BMs (Bare
   metal machines) by software with the similar set of services/functionalities
   can be provided to users such as FWaaS, LBaaS, VPNaaS, Security Group,
   Block Storage, Backup, High Availability, Connection to VMs in virtual
   network (VXLAN), and Console.

Opportunity/Justification
-------------------------

Cloud service providers want to support bare metal machine, but it is a tough
challenge to provide IaaS access to bare metal with the same elastic and
service-oriented properties as they do with virtual machines.

Use Cases
=========

User Stories
------------

* As an Enterprise user, I want to use bare metal machine so that I get
  consistent performance not affected by another machine, nor impacted
  by hypervisor.

* As an Enterprise user, I want to have a secure and clean bare metal machine
  deployed no matter who used it before.

* As an Enterprise user, I want to create networks elastically so that I can
  use network like I have these networks not affected by other companies.

* As an Enterprise user, I want to back up internal disk of bare metal machine,
  recover from it.

* As an Enterprise user, I want to use bare metal machine integrated with
  block storage service so that I can use external storage service.

* As an Enterprise user, I want to see bare metal machine from console log and
  operate from console so that I can analyze problems at booting time and so on.

* As an Enterprise user, I want to continue my operation immediately when
  a bare metal machine fails without any manual operations such as switchover.
  Similar to HA VM user story, The user should not have to design the fail-over
  mechanism themselves. The system should monitor and detect bare metal machine
  failure and automatically fail-over to a spare bare metal machine.

* As an Enterprise user, I want to use a bare metal machine with the network
  services such as FWaaS, LBaaS, Security Group, VPNaaS, and connection
  to VMs in virtual network(VXLAN) in the same manner of VMs.

Usage Scenario Examples
------------------------

1.Successful bare metal service
  a. Enterprise user creates virtual network.
  b. Enterprise user boots bare metal machine.
  c. Enterprise user uses block storage from bare metal machine.
  d. Enterprise user uses bare metal machine with consistent performance.

2.Analyze bare metal machine rebooting problem
  a. Enterprise user can't connect to bare metal machine remotely when rebooting.
  b. Enterprise user can see state of bare metal machine from console log.
  c. Enterprise user analyzes boot problem and resolved the issue.
  d. Enterprise user can boot successfully.

3.Bare metal machine data protection
  a. Enterprise user backs up data in bare metal machine.
  b. Enterprise user restore from data backed up.

Related User Stories
====================

* `High Availability for Virtual Machines <https://review.openstack.org/#/c/289469/>`_

*Requirements*
==============

None.

*External References*
=====================

* `[RFE] [Ironic] Ironic Neutron ML2 Integration <https://bugs.launchpad.net/ironic/+bug/1526403>`_
* `[SPEC] [Ironic] Update of the Ironic Neutron Integration spec <https://review.openstack.org/#/c/188528/>`_
* `[RFE] [Ironic] VLAN Aware Baremetal Instances <https://bugs.launchpad.net/ironic/+bug/1543584>`_
* `[SPEC] [Ironic] VLAN Aware Baremetal Instances <https://review.openstack.org/#/c/277853>`_
* `[BP] [Nova] Tenant networking support for Ironic driver <https://blueprints.launchpad.net/nova/+spec/ironic-networks-support>`_
* `[SPEC] [Nova] Tenant networking support for Ironic driver <https://review.openstack.org/#/c/237067>`_

* `[RFE] [Ironic] Add volume connection information into ironic db <https://bugs.launchpad.net/ironic/+bug/1526231>`_
* `[SPEC] [Ironic] Volume connection information for Ironic nodes <https://review.openstack.org/#/c/200496/>`_
* `[BP] [Nova] Add support for Ironic nodes to boot from Cinder volume <https://blueprints.launchpad.net/nova/+spec/ironic-boot-from-volume>`_

* `[RFE] [Ironic] Nova serial console support for Ironic <https://bugs.launchpad.net/ironic/+bug/1553083>`_
* `[SPEC] [Ironic] Nova serial console support <https://review.openstack.org/#/c/296869/>`_
* `[SPEC] [Ironic] Add nova-compatible-serial-console.rst to not-implemented <https://review.openstack.org/#/c/293827/>`_

* `[RFE] [Ironic] Bare metal node N+1 redundancy <https://bugs.launchpad.net/ironic/+bug/1526234>`_
* `[SPEC] [Ironic] Bare metal node N+1 redundancy <https://review.openstack.org/#/c/259320>`_

*Rejected User Stories / Usage Scenarios*
=========================================

None.

Glossary
========

TBD.
