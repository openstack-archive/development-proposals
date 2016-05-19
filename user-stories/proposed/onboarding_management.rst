.. This template should be in ReSTructured text. Please do not delete any of
.. the sections in this template.  If you have nothing to say for a whole
.. section, just write: None.  For help with syntax, see
.. http://sphinx-doc.org/rest.html You can also use an online RST editor at
.. rst.ninjs.org to generate proper RST.


Onboarding Management
=====================
**Sections in** *italics* **are optional.**

.. In order to propose submitting a User Story as a cross project spec replace
.. 'Cross Project Spec - None' with 'Cross Project Spec - Ready for Submission'
.. after this change is accepted and merged then submit the Cross Project Spec
.. to the openstack/openstack-specs repository and replace 'Ready for
.. Submission' with a link to the review, and after merger of the Cross Project
.. spec with a link to the spec. Before proposing be sure to create and provide
.. a link to the User Story Tracker

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

*Problem Definition*
++++++++++++++++++++
.. This section is optional.
.. Please use it to provide additional details (if available) about your user story
.. (if warranted) for further expansion for clarity.  A detailed description of the
.. problem. This should include the types of functions that you expect to run on
.. OpenStack and their interactions both with OpenStack and with external systems.
.. Please replace "None." with the problem description if you plan to use this
.. section.

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

Opportunity/Justification
+++++++++++++++++++++++++
.. This section is mandatory.
.. Use this section to give opportunity details that support why
.. pursuing these user stories would help address key barriers to adoption or
.. operation.

.. Some examples of information that might be included here are applicable market
.. segments, workloads, user bases, etc. and any associated data.  Please replace
.. "None." with the appropriate data.

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

Use Cases
---------

User Stories
++++++++++++
..  This section is mandatory. You may submit multiple
.. user stories in a single submission as long as they are inter-related and can be
.. associated with a single epic and/or function.  If the user stories are
.. explaining goals that fall under different epics/themes then please complete a
.. separate submission for each group of user stories.  Please replace "None." with
.. the appropriate data.

.. A list of user stories ideally in this or a similar format:

.. * As a <type of user>, I want to <goal> so that <benefit>

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

Usage Scenario Examples
+++++++++++++++++++++++
.. This section is mandatory.
.. In order to explain your user stories, if possible, provide an example in the
.. form of a scenario to show how the specified user type might interact with the
.. user story and what they might expect.  An example of a usage scenario can be
.. found at http://agilemodeling.com/artifacts/usageScenario.htm of a currently
.. implemented or documented planned solution.  Please replace "None." with the
.. appropriate data.

.. If you have multiple usage scenarios/examples (the more the merrier) you may
.. want to use a numbered list with a title for each one, like the following:

.. 1. Usage Scenario Title a. 1st Step b. 2nd Step 2. Usage Scenario Title a. 1st
.. Step b. 2nd Step 3. [...]

1. Managing existing Virtual Machines

        a. For each physical host in a legacy virtualized server
        environment, Obtain a list of all resources (Compute, Memory, Block
        storage and Network) for each Virtual Machine
        b. Create database entries for each virtual machine in the
        Virtual Machine OpenStack so that each of the legacy VMs are
        managed though OpenStack services such as Horizon, Nova, Cinder,
        Neutron.

Related User Stories
++++++++++++++++++++
.. This section is mandatory.
.. If there are related user stories that have some overlap in the problem domain or
.. that you perceive may partially share requirements or a solution, reference them
.. here.

* https://etherpad.openstack.org/p/kilo-cinder-summit-topics

* https://etherpad.openstack.org/p/kilo-neutron-summit-topics

* https://goo.gl/Y73xXS

* https://blueprints.launchpad.net/cinder/+spec/over-subscription-in-thin-provisioning

*Requirements*
++++++++++++++
.. This section is optional.  It might be useful to specify
.. additional requirements that should be considered but may not be
.. apparent through the user story and usage examples.  This information will help
.. the development be aware of any additional known constraints that need to be met
.. for adoption of the newly implemented features/functionality.  Use this section
.. to define the functions that must be available or any specific technical
.. requirements that exist in order to successfully support your use case. If there
.. are requirements that are external to OpenStack, note them as such. Please
.. always add a comprehensible description to ensure that people understand your
.. need.

.. * 1st Requirement
.. * 2nd Requirement
.. * [...]

1. Onboarding must be non-disruptive to legacy environments such that
the applications, virtual machines and physical hosts should not need to
be restarted
2. OpenStack needs to at least tolerate Virtual Machine resource
configuration changes made by non-OpenStack management tools
after the VM has been onboarded into OpenStack.
The eventual goal is for full synchronization between all resource
management tools

Three phases of synchronization related to onboarding are:
Phase 1 - No synchronization - The move to OpenStack management is one
way only. No out of band/non-OpenStack management will be accommodated
by OpenStack.
Example: Nova would delete a VM that was migrated by a control
mechanism outside of OpenStack,

Phase 2 - OpenStack toleration. Management actions initiated outside of
OpenStack would be tolerated and the OpenStack database would reflect
the changes in resources.
Example, in the case of a live migration, OpenStack would
accept that the VM had been moved to a different physical host

Similar accommodation needed for changes to storage volumes outside of
Cinder and networking changes outside of Neutron

Phase 3 - Full synchronization - This would allow multiple management
control points to take action against managed resources and have the
changes reflected in all resource managers. Most important for VMware
environments.

Example: Self service provisioning initiated in OpenStack Horizon would
result in the new VMs also showing up in vCenter

*External References*
+++++++++++++++++++++
.. This section is optional.
.. Please use this section to add references for standards or well-defined
.. mechanisms.  You can also use this section to reference existing functionality
.. that fits your user story outside of OpenStack.  If any of your requirements
.. specifically call for the implementation of a standard or protocol or other
.. well-defined mechanism, use this section to list them.

None.

*Rejected User Stories / Usage Scenarios*
-----------------------------------------
.. This is optional
.. Please fill out this section after a User Story has been submitted as a
.. cross project spec to highlight any user stories deemed out of scope of the
.. relevant cross project spec.

None.

Glossary
--------
.. This section is optional.
.. It is highly suggested that you define any terms,
.. abbreviations that are not   commonly used in order to ensure
.. that your user story is understood properly.

.. Provide a list of acronyms, their expansions, and what they actually mean in
.. general language here. Define any terms that are specific to your problem
.. domain. If there are devices, appliances, or software stacks that you expect to
.. interact with OpenStack, list them here.

.. Remember: OpenStack is used for a large number of deployments, and the better
.. you communicate your user story, the more likely it is to be considered by the
.. project teams and the product working group.

.. Examples:
.. **reST** reStructuredText is a simple markup language
.. **TLA** Three-Letter Abbreviation is an abbreviation consisting of three letters
.. **xyz** Another example abbreviation

**Hosts** Physical systems that contain a hypervisor allowing for
multiple virtual machines to run

**VM** Virtual Machines, each with their unique operating system,
processor, storage and network resources
