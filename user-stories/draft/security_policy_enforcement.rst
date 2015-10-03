Security / Policy Enforcement for Enterprise IT
==========================

*Problem description*
---------------------
Many enterprise has stringent security requirements and the security policy
must be enforced by IT. such security policy must be enforced and applied to
all compute resources hosted in the enterprise environment.


User Stories
------------
The Enterprise IT needs to enforce a corporate-wide or division-wide firewall
policy and rules. This firewall (or security group) must be applied to all
network or compute resources of a project/tenant within that division. This
policy is defined by the security administrator and must not be
removed/modified by the cloud users.

For example, the security administrator create a security group with a set of
predefined rules. This security group must be automatically applied to all VM
whenever the VM is launched by the cloud users.


Usage Scenarios Examples
------------------------
None.

Opportunity/Justification
-------------------------
None.

Related User Stories
--------------------
None.

*Requirements*
--------------
In order to support this user story, we need:
* 1st Requirement : a method for security administrator to create a firewall/security group and be able to enforece such policy to different project tenant.
* 2nd Requirement : a mechanism to automatically attached the firewall/security policy to each network/VM created by the cloud users within the project tenant.
* 3rd Requirement : The rules defined in such firewall/security policy can only be modified by the security administrator and must not be removed or modified by cloud users. This might requires "role-based access control" to specific type of resources and actions.

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
