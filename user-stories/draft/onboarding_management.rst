======================================================
Onboarding Hosts and VMs into OpenStack for Management
======================================================
**Sections in** *italics* **are optional.**

*Problem description*
---------------------
You have a number of physical hosts and virtual Machines in your
infrastructure you would like to manage with OpenStack

* For each host that you wish to manage:

 - Interrogate the hypervisor to obtain a list of all Virtual Machines
   running in that host
 - For each storage device attached to the host, obtain a list of all
   volumes associated with each VM
 - For each VM, obtain a list of all network interface addresses for
   each VM

* The Onboarding process must be non-disruptive to the operation of the
	host and the virtual machines running on the host

User Stories
------------
* As the Enterprise IT manager that is deploying an OpenStack cloud
	alongside my existing infrastructure, I need manage existing virtual
	machines compute resources with OpenStack without disrupting or
	changing the virtual machines


* As the Enterprise IT manager that is deploying an OpenStack cloud
	alongside my existing infrastructure, I need to manage the block
	storage used by my existing virtual machines into Cinder without
	disrupting operation of my existing virtual machines


* As the Enterprise IT manager that is deploying an OpenStack cloud
	alongside my existing infrastructure, I need manage existing virtual
	machines network resources without disrupting those virtual machines

Usage Scenarios Examples
------------------------
1. Managing existing Virtual Machines

	a. For each physical host in a legacy virtualized server
	environment, Obtain a list of all resources (Compute, Memory, Block
	storage and Network) for each Virtual Machine
	b. Create database entries for each virtual machine in the
	Virtual Machine OpenStack so that each of the legacy VMs are
	managed though OpenStack services such as Horizon, Nova, Cinder,
	Neutron.

Opportunity/Justification
-------------------------
Enterprises with extensive legacy applications environments would like
to consolidate management of those environments through OpenStack.  Due
to the nature of the applications and their value to the business, the
onboarding process needs to be non-disruptive and suitable for use at
scale.

The Onboarding capability should work with any virtualization technology
that provides OpenStack APIs to manage the virtual machine configuration

The ability to onboard legacy environments is widely desired by any
business that is currently has a legacy IT environment and is using
OpenStack to manage new applications.

Support for onboarding legacy environments in a non-disruptive manner
will greatly increase the adoption of OpenStack.

Related User Stories
--------------------

* https://etherpad.openstack.org/p/kilo-cinder-summit-topics

* https://etherpad.openstack.org/p/kilo-neutron-summit-topics

* https://goo.gl/Y73xXS

* https://blueprints.launchpad.net/cinder/+spec/over-subscription-in-thin-provisioning

*Requirements*
--------------
1. Onboarding must be non-disruptive to legacy environments such that
the applications, virtual machines and physical hosts should not need to
be restarted

*Gaps*
------
* Cinder API to list all volumes
* Cinder API to add volume to database (current “manage_existing”
	API requires too much intrinsic knowledge because it only provides the
	storage primary ID when what we need the WWPNs, Page83 SCSI Identifier,
	etc that the hypervisor would know
* Nova API to discover VM and all resources associated with it including
	Memory, Processor, Block Volumes
* Nova API to add existing VM to OpenStack database
* Neutron API to add network information to OpenStack database

Glance changes are not required for the initial onboarding
for management process

*Affected By*
-------------
None.

*External References*
---------------------
None.

Glossary
--------
**Hosts** Physical systems that contain a hypervisor allowing for
multiple virtual machines to run

**VM** Virtual Machines, each with their unique operating system,
processor, storage and network resources
