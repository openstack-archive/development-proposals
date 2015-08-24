..

This work is licensed under a Creative Commons Attribution 3.0 Unported License.
http://creativecommons.org/licenses/by/3.0/legalcode

**Sections in** *italics* **are optional.**

..  This template should be in ReSTructured text. Please do not delete any of
the sections in this template.  If you have nothing to say for a whole section,
just write: None.  For help with syntax, see http://sphinx-doc.org/rest.html You
can also use an online RST editor at rst.ninjs.org to generate proper RST.

============================================ Onboarding Legacy Apps into
OpenStack (Pets) ============================================

*Problem description* --------------------- ● What do you do when you have a 3rd
party app in your infrastructure and the 3rd party  doesn't know openstack and
how to evaluate/modify their apps ability to be onboarded into OpenStack 

● Work from the top of the stack down ­ how do you address stateful apps ­  

● Start with different language/tools (Java, etc) and then walk through the
solution stack and identify the points where changes are needed and then how to
implement it 

● Or consider how to enable the app to still be stateful, but more failure
tolerant 

● I have a homegrown CRM, how do I port it to OpenStack? 

● Partitioning Apps ­ How do you modularize an app so that the front end can be
hosted in the cloud and the back end can be housed in the traditional
infrastructure. 

● This is focused on 3rd party applications: Porting, Rebuilding ● I need to be
able to test and validate the on­boarded app at scale!  None.

User Stories ------------ As the Enterprise IT manager that is deploying an
OpenStack cloud alongside my existing infrastructure, I need manage existing
virtual machines compute resources.

As the Enterprise IT manager that is deploying an OpenStack cloud alongside my
existing infrastructure, I need to onboard existing block storage into Cinder.

As the Enterprise IT manager that is deploying an OpenStack cloud alongside my
existing infrastructure, I need manage existing virtual machines network
resources.

Usage Scenarios Examples ------------------------ ..
 
1. Managing existing virtualized applications
 
a. For each physical host in a legacy virtualized server environment, Obtain a
list of all resources (Compute, Memory, Block storage and Network) for each
Virtual Machine b. Create database entries for each virtual machine in the
OpenStack so that each of the legacy VMs are managed though OpenStack services
such as Horizon, Nova, Cinder, Neutron. 

Opportunity/Justification ------------------------- ..

Enterprises with extensive legacy applications would like to manage these
applications using OpenStack services. Due to the nature of the applications and
their value to the business, the onboarding process needs to be non-disruptive
and suitable for use at scale. 

The ability to onboard legacy enviroments is widely desired by any business that
is currently has a legacy IT environment and is using OpenStack to manage new
applications. 

Support for onboarding legacy envirnoments in a non-disruptive manner will
greatly increase the odoption of OpenStack 

Related User Stories -------------------- ..

https://etherpad.openstack.org/p/kilo-nova-summit-topics

https://etherpad.openstack.org/p/kilo-cinder-summit-topics

https://etherpad.openstack.org/p/kilo-neutron-summit-topics

https://github.com/openstack/cinder-specs/blob/master/specs/kilo/over-subscription-in-thin-provisioning.rst

https://blueprints.launchpad.net/cinder/+spec/over-subscription-in-thin-provisioning

*Requirements* -------------- ..  This section is optional.  It might be useful
to specify additional requirements that should be considered but may not be
apparent through the user story and usage examples.  This information will help
the development be aware of any additional known constraints that need to be met
for adoption of the newly implemented features/functionality.  Use this section
to define the functions that must be available or any specific technical
requirements that exist in order to successfully support your use case. If there
are requirements that are external to OpenStack, note them as such. Please
always add a comprehensible description to ensure that people understand your
need.

1. Onboarding must be non-disruptive to legacy application environments


*Gaps* ------
- Cinder API to list all volumes 
- Cinder API to add volume to database (current “manage_existing” API requires
  too much intrinsic knowledge)
- Nova API to discover VM and all resources associated with it including Memory,
  Processor, Block Volumes
- Nova API to add existing VM to OpenStack database
- Neutron API to add network information to OpenStack database


*Affected By* ------------- ..  This section is optional.  This section should
be used for prior records of activity inside OpenStack related to this user
story (bugs that need to be fixed, blueprints for prior attempts, etc.).  If
possible, please include links to the related specs, blueprints, or bug reports.
Please replace "None." with the appropriate data.

None.

*External References* --------------------- ..  This section is optional.
Please use this section to add references for standards or well-defined
mechanisms.  You can also use this section to reference existing functionality
that fits your user story outside of OpenStack.  If any of your requirements
specifically call for the implementation of a standard or protocol or other
well-defined mechanism, use this section to list them.

Glossary ======== ..  This section is optional.  It is highly suggested that you
define any terms, abbreviations that are not   commonly used in order to ensure
that your user story is understood properly.

Provide a list of acronyms, their expansions, and what they actually mean in
general language here. Define any terms that are specific to your problem
domain. If there are devices, appliances, or software stacks that you expect to
interact with OpenStack, list them here.

Remember: OpenStack is used for a large number of deployments, and the better
you communicate your user story, the more likely it is to be considered by the
project teams.easier it will be to implement.

**reST** reStructuredText is a simple markup language

**TLA** Three-Letter Abbreviation is an abbreviation consisting of three letters

**Pets** Legacy application workloads that are characterized by stateful
applications that lack of application level redundancy and high value to the
business (contrast with "cattle")
  
**Cattle** Designed for cloud applications that are characterized by stateless
application design and application redundancy
