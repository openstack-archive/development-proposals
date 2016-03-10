Security / Policy Enforcement for Enterprise IT
==========================
Cross Project Spec - None

User Story Tracker - None

Problem Description
====================

*Problem Definition*
--------------------
Many enterprise has stringent security requirements and the security policy
must be enforced by IT security. Such security policy must be enforced and applied to
all compute resources hosted in the enterprise environment.

Opportunity/Justification
-------------------------
TBD.

Use Cases
=========

User Stories
------------
* As an Enterprise IT security policy maker, I need to ensure that all compute
resources must adhere to the security policy as defined by the IT security
department so that the cloud resources are compliant to enterprise rules and
regulations.
* As an Enterprise IT security administrator, I have to create multiple security
policy for different corporate department or division. All cloud resources
provisioned for that particular department or division must be applied with
relevant security policy. Such policy (e.g firewall rules) cannot be removed
by the cloud users. A cloud users may add additional rules but cannot remove
any rules as defined by the IT security administrator.

Usage Scenarios Examples
------------------------
The Enterprise IT needs to enforce a corporate-wide or division-wide firewall
policy and rules. This firewall (or security group) must be applied to all
compute resources of a project/tenant within that division. This policy is
defined by the security administrator and must not be removed by the cloud
users.

For example, the security administrator create a security group with a set of
predefined rules. This security group must be automatically applied to all VM
whenever the VM is launched by the cloud users and cannot be removed.

Related User Stories
====================
None.

*Requirements*
==============
In order to support this user story, we need:
* A method for security administrator to create a
firewall or security policy and be able to enforce such policy to different
project tenant.
* A mechanism to automatically attached the fireall or
security policy to each network/VM created by the cloud users within the
project tenant.
* The rules defined in such fireall/security policy can only
be modified by the security administrator and must not be removed or modified
by cloud users. This might requires "role-based access control" to specific
type of resources and actions.

*External References*
=====================
TBD.

*Rejected User Stories / Usage Scenarios*
=========================================
None.

Glossary
========
TBD.
