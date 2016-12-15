Bare Metal Service
==================

Cross Project Spec - None

Feature Tracker - None

Problem Overview
----------------

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
   bare metal machine to external block device managed by Cinder and recover
   from it.

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

Requirement Specification
-------------------------

Use Cases
+++++++++

This section utilizes the `OpenStack UX Personas`_.

.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html
.. _Quinn the application developer: https://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/app-developer.html

*The best-matching persona seems to be `Quinn the application developer`_ at the time this proposal
is created.*

* BMT001 - As `Quinn the application developer`_, I want to use bare metal machine so that I
  get consistent performance not affected by another machine, nor impacted by
  hypervisor.

* BMT002 - As Quinn, I want to have a secure and clean bare
  metal machine deployed no matter who used it before.

* BMT003 - As Quinn, I want to have a secure and isolate networks so
  that these networks are not affected by other tenants in the cloud.

* BMT004 - As Quinn, I want to back up internal disk of bare
  metal and create a snapshot. This can be backed up to an external storage
  managed by Cinder.

* BMT005 - As Quinn, I want to use bare metal machine integrated
  with block storage service so that I can use external storage service.

* BMT006 - As Quinn, I want to see bare metal machine from
  console log and operate from console so that I can analyze problems at
  booting time and so on.

* BMT007 - As Quinn, I want to continue my operation immediately
  when a bare metal machine fails without any manual operations such as
  switchover. Similar to `High Availability for Virtual Machines`_ user story, the owner should not have to design
  the fail-over mechanism themselves. The system should monitor and detect
  bare metal machine failure and automatically fail-over to a spare bare metal
  machine.

* BMT008 - As Quinn, I want to use a bare metal machine with the
  network services such as FWaaS, LBaaS, Security Group, VPNaaS, and
  connection to VMs in virtual network(VXLAN) in the same manner of VMs.

Usage Scenario Examples
+++++++++++++++++++++++

1. Successful bare metal service

   a. Quinn creates virtual network.
   #. Quinn boots bare metal machine.
   #. Quinn uses block storage from bare metal machine.
   #. Quinn uses bare metal machine with consistent performance.

#. Analyze bare metal machine rebooting problem

   a. Quinn can't connect to bare metal machine remotely when
      rebooting.
   #. Quinn can see state of bare metal machine from console log.
   #. Quinn analyzes boot problem and resolved the issue.
   #. Quinn can boot successfully.

#. Bare metal machine data protection

   a. Quinn backs up data in bare metal machine.
   #. Quinn restore from data backed up.

Related Development Proposals
++++++++++++++++++++++++++++++

* `High Availability for Virtual Machines <https://review.openstack.org/#/c/289469/>`_

Requirements
++++++++++++

N/A.

External References
+++++++++++++++++++

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

Rejected Proposals
------------------

N/A.

Glossary
--------

N/A.
