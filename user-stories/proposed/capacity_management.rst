Quotas, Usage Plans, and Capacity Management
============================================

Cross Project Spec - None

User Story Tracker - None

Problem Description
-------------------

*Problem Definition*
++++++++++++++++++++
A canonical property of an IaaS system like OpenStack is “capacity on demand”. Users expect to be able to allocate new resources via UI or API whenever needed, and to release them when the need ends. By supporting a large number of users, pooling resources, and maintaining some excess capacity, the cloud service provider (CSP) presents the illusion of infinite capacity.

In practice, of course, the resources are not infinite, and the CSP must institute measures to manage capacity so that resource exhaustion is minimized. This is generally done by imposing a cap or quota on the resources that a particular project may consume, and by managing the relationship between the available physical resources and the aggregate quotas for all projects. When a project requires more resources than its assigned quota, the user is generally required to submit a request, generally requiring human approval. The CSP may reject the request, or delay it until sufficient capacity is available. When the request is approved, the quota for the project is modified to reflect the new limit.

Other CSPs have introduced a number of mechanisms to provide them with flexibility in managing capacity. These include group quotas (shared by related projects), reserved instances, ephemeral instances (which may be reclaimed for reallocation), and market-based allocation models. At the present time, OpenStack does not support any of these.

One common factor in all these processes is that they do not reflect temporal variations in resource usage. Yet in many cases the user knows how their usage is going to vary over time, and such information would be useful to the CSP who needs to decide how to handle each request. It might also facilitate the automation of some of the processing. The following user stories capture the possibilities here.

Opportunity/Justification
+++++++++++++++++++++++++
.. This section is mandatory.
.. Use this section to give opportunity details that support why
.. pursuing these user stories would help address key barriers to adoption or
.. operation.

.. Some examples of information that might be included here are applicable market
.. segments, workloads, user bases, etc. and any associated data.  Please replace
.. "None." with the appropriate data.

None.

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

* As an OpenStack user, I want to specify my resource usage request (RUR) in a way that will enable automated processing by the CSP, so that my RUR will be handled more quickly and accurately.

* As a CSP I want to be able to automate the processing of RURs so that I can meet my user SLAs and gain more timely and accurate data input to my capacity management and planning systems.

* As a user, I want to be able to describe the temporal characteristics of my RUR, so that the CSP can plan capacity more accurately and reduce the chances of a resource request failure. My CSP may also offer me better pricing for more accurate usage prediction. Some examples of time-based RURs:

 a. I plan to use up to 60 vCPUs and 240GB of RAM from 6/1/2016 to 8/14/2016.
 b. I plan to use 200GB of object storage starting on 8/14/2016, increasing by 100GB every calendar month thereafter.
 c. I want guaranteed access to 30 vCPUs and 200GB of RAM for my project. In addition, during October-December, I want to be able to increase my usage to 150 vCPUs and 1TB of RAM

* As a user, I want to be able to submit an updated version of a rolling RUR for my project every month, so that my CSP has accurate information and can give me the best price and SLA.

* As a user, I want to be able to take advantage of pricing and other offers from my CSP in order to meet the business objectives for my project. For example:

 a. I want 60 vCPUs for a minimum of one hour. After that time, the CSP may shut down all my instances if the resources are needed elsewhere. (I assume that the price is lower on such instances.)
 b. I want up to 100 vCPUs for the next 24 hours. Tell me how many I can have.

* As a CSP, I want to be able to automate the construction and interpretation of a time-based resource usage plan so that I can schedule the most cost-effective actions to maintain my SLA. Some examples of actions:

 a. Schedule the provisioning of additional infrastructure.
 b. Repurpose existing allocated infrastructure.
 c. Assign a new project to one of a number of regions based on usage projections.
 d. Add “burst capacity” from a federation partner or reseller.
 e. Modify or defer another project.


Usage Scenarios Examples
++++++++++++++++++++++++
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

This Use Case is related to the Infinite Elasticity use case. The latter focuses on testing the capability of an OpenStack cloud to handle large-scale capacity requests.

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

* The implementation of these capabilities will depend in part on the existence of a more flexible and holistic quota scheme, so that the capacity management system can adjust quotas programmatically.
* It will also require a rich monitoring, notification, and visualization system, so that both user and CSP have accurate and timely data about the behavior of the system.

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
