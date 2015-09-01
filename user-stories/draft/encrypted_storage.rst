..  This template should be in ReSTructured text. Please do not delete any of
.. the sections in this template.  If you have nothing to say for a whole section,
.. just write: None.  For help with syntax, see http://sphinx-doc.org/rest.html You
.. can also use an online RST editor at rst.ninjs.org to generate proper RST.


Encrypted Storeage
==========================
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

Each Enterprise has its own data classification strategy. The types of data include: financial data, personal data, health data, confidential business data, etc. Some Enterprises (esp in banking, finance and insurance industry) has stringent data requiirements in order to be compliant with laws and regulations. For example PCI DSS Requirement 3.4 states that credit card and personal account number must be rendered unreadable anywhere it is stored (including portable digital media, backup media and logs). Applications (including database) that interact with these classes of information need to be able to specify encrypted storage requirements when the application is launched and interacts with some of these classes. The data must be encrypted in motion as well as at rest. [2] The application should not require admin privilideges to access encrypted storage [3].

In addition, proper key management process need to be in place. The keys used to encrypt/decrypt the data must be changed on a regulare basis and the access of keys are restricted to authorized personnel only.

User Stories
------------
..  This section is mandatory. You may submit multiple
.. user stories in a single submission as long as they are inter-related and can be
.. associated with a single epic and/or function.  If the user stories are
.. explaining goals that fall under different epics/themes then please complete a
.. separate submission for each group of user stories.  Please replace "None." with
.. the appropriate data.

.. A list of user stories ideally in this or a similar format:

.. * As a <type of user>, I want to <goal> so that <benefit>

As the Enterprise IT Manager, I must ensure the appropriate security for the HR department database with employee records that services several department applications. I would like to move the database into our company's private cloud so I don't nee dot maintain the system it currently lives on. However, because of the critical nature of the inormation in the database our company policy does not allow this information to reside in any shared system in an unencrypted state. To be able to mveo the database into the private cloud I need to ensure that the stored data and all data in transit from/to the VM will be encrypted. While the HR Department would love to have improved uptime for their database, they are used to having to manually restart/reboot as needed and can live with this in the cloud as well.

I am the Enterprise IT manger for an insurance company. My company maintains a database with the insurer's credit card records for annual renewal purpose. Our company would like to move the database into our OpenStack private cloud. In order to comply with the company security policy, government laws and financial regulations, I need to ensure that information stored in the provate cloud (including backup) is encrypted, and the keys used to encrypt the data are rotated/changed annually.

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

At the Hing Kong summit there was talk on the barbican/cinder/nova for this type of functionality. Don't know the status of this: https://www.openstack.org/summit/openstack-summit-hong-kong-2013/session-videos/presentation/encrypted-block-storage-technical-walkthroughs

There is a spec located at: https://wiki.openstack.org/wiki/VolumeEncryption for some early work and the current documentation is located at: http://docs.openstack.org/juno/config-reference/content/section_create-encrypted-volume-type.html where it implies that admin priviledge is required.

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

1. A block and object storage option that includes encryption/decryption at the VM source.
2. A method for the applciation to specify that it requires a block storage system that includes encryption/decryption at the VM Source.
3. A method for changing the key used to encrypt/decrypt the data after the specific period of time.
4. The database applications needs to be able to specify that it needs an encrypted storage system that support encryption/decryption athe VM source, in addition to at rest.
5. The Storage system must be able to handle both reads/writes of persistent encrypted block storage in excess of 1TB device to be backed up nightly.

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

Cinder issues: The basic storage encryption functionality may exist, but requires admin status. Also, cannot boot from an encrypted volume.

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
