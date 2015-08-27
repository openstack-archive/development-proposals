============================================
Onboarding Legacy Apps into OpenStack (Pets)
============================================
**Sections in** *italics* **are optional.**

*Problem description*
---------------------
What do you do when you have a 3rd party app in your infrastructure and the 3rd party doesn't know openstack and
how to evaluate/modify their apps ability to be onboarded into OpenStack 

* Work from the top of the stack down ­ how do you address stateful apps
* Start with different language/tools (Java, etc) and then walk through the solution stack and identify the points where changes are needed and then how to implement it
* Or consider how to enable the app to still be stateful, but more failure tolerant
* I have a homegrown CRM, how do I port it to OpenStack?
* Partitioning Apps ­ How do you modularize an app so that the front end can be hosted in the cloud and the back end can be housed in the traditional infrastructure.
* This is focused on 3rd party applications: Porting, Rebuilding 
* I need to be able to test and validate the on­boarded app at scale!

User Stories
------------
* As the Enterprise IT manager that is deploying an OpenStack cloud alongside my existing infrastructure, I need manage existing virtual machines compute resources.

* As the Enterprise IT manager that is deploying an OpenStack cloud alongside my existing infrastructure, I need to onboard existing block storage into Cinder.

* As the Enterprise IT manager that is deploying an OpenStack cloud alongside my existing infrastructure, I need manage existing virtual machines network resources.

Usage Scenarios Examples
------------------------
1. Managing existing virtualized applications
 
	a. For each physical host in a legacy virtualized server environment, Obtain a
	list of all resources (Compute, Memory, Block storage and Network) for each
	Virtual Machine b. Create database entries for each virtual machine in the
	OpenStack so that each of the legacy VMs are managed though OpenStack services
	such as Horizon, Nova, Cinder, Neutron.

Opportunity/Justification
-------------------------
Enterprises with extensive legacy applications would like to manage these
applications using OpenStack services. Due to the nature of the applications and
their value to the business, the onboarding process needs to be non-disruptive
and suitable for use at scale.

The ability to onboard legacy environments is widely desired by any business that
is currently has a legacy IT environment and is using OpenStack to manage new
applications.

Support for onboarding legacy environments in a non-disruptive manner will
greatly increase the adoption of OpenStack.

Related User Stories
--------------------
* https://etherpad.openstack.org/p/kilo-nova-summit-topics

* https://etherpad.openstack.org/p/kilo-cinder-summit-topics

* https://etherpad.openstack.org/p/kilo-neutron-summit-topics

* https://github.com/openstack/cinder-specs/blob/master/specs/kilo/over-subscription-in-thin-provisioning.rst

* https://blueprints.launchpad.net/cinder/+spec/over-subscription-in-thin-provisioning

*Requirements*
--------------
1. Onboarding must be non-disruptive to legacy application environments.

*Gaps*
------
* Cinder API to list all volumes
* Cinder API to add volume to database (current “manage_existing” API requires
  too much intrinsic knowledge)
* Nova API to discover VM and all resources associated with it including Memory,
  Processor, Block Volumes
* Nova API to add existing VM to OpenStack database
* Neutron API to add network information to OpenStack database

*Affected By*
-------------
None.

*External References*
---------------------
None.

Glossary
========
**Pets** Legacy application workloads that are characterized by stateful
applications that lack of application level redundancy and high value to the
business (contrast with "cattle")

**Cattle** Designed for cloud applications that are characterized by stateless
application design and application redundancy
