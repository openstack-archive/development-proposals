Role Based Access
=================

*Problem description*
---------------------
OpenStack doesn’t have a hierarchical permission structure that allows an
Operator to assign different permissions for different activities or access to
resources to different users.

User Stories
------------
*As a cloud operator I want to enable my team to be able to see all Admin level
alerts, but not to be able to change their status. That requires review and
approval by the IT manager.

Usage Scenarios Examples
------------------------
None.

Opportunity/Justification
-------------------------
Role Based Access is a basic Enterprise requirement. This capability enables
Enterprise IT Managers to set read and write permissions to different elements of
the IT infrastructure for different people/positions in the organization.
Enterprise security requires separate access UI/ API for Network, Security,
Storage management, User Management, and Instance management.

Related User Stories
--------------------
None.

*Requirements*
--------------
* Enterprise security requires separate access UI/ API for Network, Security,
Storage management, User Management, and Instance management.
* Includes grouping actions into roles, assign roles to users, create hierarchy
of roles, etc.
* OpenStack includes an enforcement piece of access control, but no management
piece.
* Very important that admin type roles need to be tested thoroughly because of
the code bleed-in where actions are exposed if  "is-admin".
* As we expand the roles need some tool that can report out on what access the
newly defined role has - want to make sure you don’t inadvertently create a
superuser problem (newly created role inherit these rights)

*Gaps*
------
**Keystone**
* Need to add a new role.
* Modify code that makes checks such as context admin, is-admin.
**All Projects**
* Need to review code in other projects to find hardcoded reference to Admin and
replace them with Keystone references.
* Modify the policy.json file to use this new role. Add test cases to confirm
behavior is as expected. Code in all projects need to be searched for is-admin
type tests and code modified to ensure that admin-read-only is tested as
necessary.
* One approach: Expose the policy.json files of each of the projects via horizon
and allow it to be modified.
* May need a bug to fix such as: is-admin evaluations to use only roles in the
code,  towards making policy.json the true controller.
**Horizon**
*To expose policy.json via Horizon will need to be allowed to only cloud-admins,
and any change checked for syntactic correctness at the least.
* Further Horizon today is "pulling" the policy files to determine which
buttons/links exposed to users to guide them down the correct path.

*Affected By*
-------------
None.

*External References*
---------------------
From looking at other solutions, generally there are 3 immutable system roles:
administrator, read-only, no-access. With support for specifying roles on objects
and their hierarchy. There is a notion of "folder", data center, host, VMs on a
host, disk etc. Some actions are sort of atomic -- create a disk. While others
encompass multiple steps, needing a variety of privileges. Thus the role that
permits the complex action must contain the full set of necessary privileges. For
example launching a VM needs access to the datastore, OS images files, disks,
ability to create them and/or read an existing one etc.

Glossary
========
None.