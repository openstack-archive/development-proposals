Cloud Validator
==========================
Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

*Problem Definition*
++++++++++++++++++++
As an Enterprise deployer and operator of OpenStack I need to validate that my
cloud is operating appropriately. My cloud typically consists of multiple
hosts which might span multiple racks and switches. In order to verify that my
entire deployment was successful I need to execute common tasks that exercise
all the hosts in my environment.

Opportunity/Justification
+++++++++++++++++++++++++
Today many enterprise deployers of OpenStack are concerned about reliability.
This goes beyond ensuring that the software itself performs correctly and
includes the ability to ensure that the physical deployment is configured in
such a way that specific objectives can be accomplished. Providing a method for
deployers to validate their entire deployment would be valuable as it gives
operators a tool to develop confidence that their users will not encounter
errors post deployment.

Use Cases
---------

User Stories
++++++++++++
  * As a Cloud Operator, I want to validate the entire software and hardware
  environment which comprises my cloud so that my Cloud Admin, Project Admin
  and App Deployers are not the ones discovering errors
  * As a Cloud Operator, I want to perform validation after initial deployment,
  after upgrade and periodically throughout regular cloud operations
  * As an OpenStack Developer, I want to receive feedback from Cloud Operators
  on common errors encountered across an entire fleet deployment so that I can
  fix any bugs which are found

Usage Scenario Examples
+++++++++++++++++++++++
1. Initial deployment validation
   a. Deploy OpenStack cloud
   b. Run "Cloud Validator" against deployed cloud
   c. Remediate any issues with configuration, hardware or software identified
   d. Run "Cloud Validator" again
   e. Feel comfortable enabling projects and users in the new, validated
   OpenStack Cloud

2. Post upgrade validation
   a. Run "Cloud Validator" on running cloud prior to upgrade
   b. Perform upgrade
   c. Run "Cloud Validator" and ensure upgrade was successful and cloud is
   valid

3. Validator for Troubleshooting
   a. Run "Cloud Validator" on running cloud during the course of
   troubleshooting to determine if any issues can be pin-pointed


Related User Stories
++++++++++++++++++++
None.

*Requirements*
++++++++++++++
TBD.

*External References*
+++++++++++++++++++++
TBD.

*Rejected User Stories / Usage Scenarios*
-----------------------------------------
None.

Glossary
--------
TBD
