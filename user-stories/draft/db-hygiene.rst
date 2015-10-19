..  This template should be in ReSTructured text. Please do not delete any of
.. the sections in this template.  If you have nothing to say for a whole section,
.. just write: None.  For help with syntax, see http://sphinx-doc.org/rest.html You
.. can also use an online RST editor at rst.ninjs.org to generate proper RST.

Database cleanup of deleted object
============================================
**Sections in** *italics* **are optional.**

*Problem description*
---------------------
.. This section is optional. 
.. Please use it to provide additional details (if available) about your user story
.. (if warranted) for further expansion for clarity.  A detailed description of the
.. problem. This should include the types of functions that you expect to run on
.. OpenStack and their interactions both with OpenStack and with external systems.
.. Please replace "None." with the problem description if you plan to use this
.. section.

Each operator of the openstack need an ability to clean up openstack database of the objects that has been deleted. Currently a new record is created in OpenStack database when an object (project, user, VM, network, volume, swift object, etc.) is created. When an object is deleted by a user/admin its record in database remains but is marked as deleted.  As Openstack cloud stays in operation over time the number of records in database continues to grow with deleted objects record and database becomes too large consuming resources on controller node(s) and impacting responsiveness of database, or even crushing controller(s).
WHile a record for deletion of an object is needed to cloud governance it does not require that this record remain in database. Thus, some tool is needed for openstack operator to cleanup database from records of deleted objects.

.. user stories in a single submission as long as they are inter-related and can be
.. associated with a single epic and/or function.  If the user stories are
.. explaining goals that fall under different epics/themes then please complete a
.. separate submission for each group of user stories.  Please replace "None." with
.. the appropriate data. 

.. A list of user stories ideally in this or a similar format:

.. * As a <type of user>, I want to <goal> so that <benefit>

* As part of PoC of OpenStack cloud an operator needs a tool to purge database of deleted records. That is need to be able to rerun the same test tool that would create the same objects every run as well as testing actual grown od database for operational condition not OpenStack implementation artifacts.

* As an operator of OpenStack cloud I need an ability to remove records of deleted objects from database. But I need to store records for audit purpose. 

* As a cloud deployment engineer, I need to be able to re-run the same tests (with same objects) in a repeatable manner so that I can have a high certainty in the outcome of my proof of concept and cloud functionality. 

* As a cloud deployment engineer, I need only the appropriate records in my database so that I can complete my upgrade in the allocated down time.

Usage Scenarios Examples
------------------------
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

Opportunity/Justification
-------------------------
.. This section is mandatory. 
.. Use this section to give opportunity details that support why
.. pursuing these user stories would help address key barriers to adoption or
.. operation.

.. Some examples of information that might be included here are applicable market
.. segments, workloads, user bases, etc. and any associated data.  Please replace
.. "None." with the appropriate data.

None.

Related User Stories
--------------------
.. This section is mandatory. 
.. If there are related user stories that have some overlap in the problem domain or
.. that you perceive may partially share requirements or a solution, reference them
.. here.

Nova specs:
* https://review.openstack.org/#/c/184645/
* https://review.openstack.org/#/c/184637/
* https://review.openstack.org/#/c/137669/

Cinder blueprint:
* https://blueprints.launchpad.net/cinder/+spec/db-cleanup

*Requirements*
--------------
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

* Operator should be able to specify which policy to apply for deleted objects.
* Operator should be able to specify which policy to apply for deleted objects.
* Operator should be able to specify which policy to apply for different Tenants and even subtetants.
* At least two policy must be supported: permanent deletion and audit, where records are removed from database but stored for compliance interval duration in persistent storage.

*Gaps*
------
.. This section is optional.  
.. It might be useful to provide information in this 
.. section if there is already some functionality in OpenStack
.. that might seem to fit your user story on the surface but, in reality, does not
.. actually fulfill the needs of the user type or the objective.  If you choose to
.. complete this section, please be sure to include information about the gap AND
.. why you believe the current functionality does not meet the requirement. Please
.. replace "None currently known." with the appropriate data. This section can
.. often be left with "None currently known." It is the purpose of this working
.. group and repository to use the use cases presented here to identify what the
.. gaps are.

None currently known.

*Affected By*
-------------
.. This section is optional.  
.. This section should be used for prior records of 
.. activity inside OpenStack related to this user story
.. (bugs that need to be fixed, blueprints for prior attempts, etc.).  If
.. possible, please include links to the related specs, blueprints, or bug reports.
.. Please replace "None." with the appropriate data.

None.

*External References*
---------------------
.. This section is optional.
.. Please use this section to add references for standards or well-defined
.. mechanisms.  You can also use this section to reference existing functionality
.. that fits your user story outside of OpenStack.  If any of your requirements
.. specifically call for the implementation of a standard or protocol or other
.. well-defined mechanism, use this section to list them.

None.

Glossary
========
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
