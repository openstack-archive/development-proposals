.. This template should be in ReSTructured text. Please do not delete any of
.. the sections in this template.  If you have nothing to say for a whole
.. section, just write: None.  For help with syntax, see
.. http://sphinx-doc.org/rest.html You can also use an online RST editor at
.. rst.ninjs.org to generate proper RST.


Lifecycle Management for VMs
============================
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

From time to time, and for a variety of reasons, VMs that are created become
unused and they linger in the system consuming resources. We need a mechanism
to detect they are inactive and the clean them up.

By clean-them-up, I mean snap shot any needed data, send messages to any apps
as needed, log the appropriate information, then kill the VM and free up the
resources.

If a lease expires, then the VM is automatically be deleted. When Deleted all
resources used by that VM would be freed (cpu, memory, networks).

To address VM sprawl apply a life cycle model. When a tenant is launch a VM,
they can specify the type of use case (ex development) which will assign a
lease length (ex 90 days) and may have the ability to renew the lease before it
expires.

This will ensure efficient and valuable use of infrastructure resources.

Opportunity/Justification
+++++++++++++++++++++++++
.. This section is mandatory.
.. Use this section to give opportunity details that support why
.. pursuing these user stories would help address key barriers to adoption or
.. operation.

.. Some examples of information that might be included here are applicable market
.. segments, workloads, user bases, etc. and any associated data.  Please replace
.. "None." with the appropriate data.

Elasticity is a key business driver for cloud and automating, or at
least simplifying, lifecycle management and resource reclamation will
provide enterprises with a cost-effective way to help maintain control
over resource sprawl.  A second benefit will be that clouds running at
scale will operate more efficiently due to clean up older database
records associated with instances.

Requirements Specification
--------------------------

Use Cases
+++++++++
..  This section is mandatory. You may submit multiple
.. user stories in a single submission as long as they are inter-related and can be
.. associated with a single epic and/or function.  If the user stories are
.. explaining goals that fall under different epics/themes then please complete a
.. separate submission for each group of user stories.  Please replace "None." with
.. the appropriate data.

.. A list of user stories ideally in this or a similar format:

.. * As a <type of user>, I want to <goal> so that <benefit>

* As the sys admin I need to ensure the Hygiene of VMs in my deployment. This
  includes cleaning up stuff, dealing with stuck/orphans VMs to free up unused
  resources for other workloads to consumer.

* As a Public Cloud operator I have to be ably to comply with Government
  orders/investigations. This may require that I quarantine a VM (and
  associated resources) or that I make a VM (and associated resources)
  available to investigators for digital forensics.

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

TBD

Related User Stories
++++++++++++++++++++
.. This section is mandatory.
.. If there are related user stories that have some overlap in the problem domain or
.. that you perceive may partially share requirements or a solution, reference them
.. here.

* Life cycle management for Storage (does not exist yet)
* DB Hygiene (does not exist yet)

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

TBD

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
