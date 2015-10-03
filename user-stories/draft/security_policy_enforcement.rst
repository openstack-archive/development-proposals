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
* 1st Requirement : a method for security administrator to create a
firewall or security policy and be able to enforce such policy to different
project tenant.
* 2nd Requirement : a mechanism to automatically attached the fireall or 
security policy to each network/VM created by the cloud users within the
project tenant.
* 3rd Requirement : The rules defined in such fireall/security policy can only
be modified by the security administrator and must not be removed or modified
by cloud users. This might requires "role-based access control" to specific
type of resources and actions.


*Gaps*
------
None currently known.

*Affected By*
-------------
None.

*External References*
---------------------
None.

Glossary
========
None.
