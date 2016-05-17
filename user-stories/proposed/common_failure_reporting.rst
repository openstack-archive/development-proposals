Centralized Failure Reporting
=============================
Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

Problem Definition
++++++++++++++++++
OpenStack operators largely trouble-shoot operational issues with their
deployments in silos. Many have developed their own run-books and failure
remediation methods that they believe are unique to their clouds. It is likely
many of these remediation methods and failure taxonomies are valuable to other
operators.

Operators should be able to publish their learnings in such a way as they are
actionable by others. In a similar fashion, new operators should be able to
to leverage the lessons learned from all those who have been operating
OpenStack clouds before them.

Opportunity/Justification
+++++++++++++++++++++++++
A common failure reporting mechanism would capitalize on one of OpenStack's
core strengths, namely its community of users around a free open-sourced
software. An ability to share common operational issues and their resolutions
would significantly lower the complexity barrier which plagues those
considering deploying OpenStack.

Use Cases
---------

User Stories
++++++++++++

* As a Cloud Operator, I want to be able to easily report failures in my
  deployment so that others can benefit from my experience

* As a Cloud Operator, I want to be able to easily report remediations for
  common failures in my deployment so that others can benefit from my
  experience

* As a Cloud Operator, I want to access a common set of reported failures
  and remediations so that I can build tooling to automatically remediate

* As a Cloud Operator, I want to access a set of known failure scenarios so
  so that I can speed the troubleshooting process in my own environment

* As a Cloud Operator, I want the known set of failure scenarios to be
  appropriately categorized so that I can easily identify patterns and
  similarities to my own environment

Usage Scenario Examples
+++++++++++++++++++++++
1. Minimally Viable Centralized Failure Reporting
  a. Operator X encounters failure
  b. Operator X reviews minimal set of required fields for submission
  c. Operator X complete submission of failure
  d. `OpenStack Failure Work Group`_ reviews and categorizes submission
  e. Failure Work Group identifies similarity between submission from
     Operator X and Operators A,B & C
  f.

2. Advanced Centralized Failure Reporting
  a.

3. Automated Usage of Centralized Failure Reporting
  a.

Related User Stories
++++++++++++++++++++
* `Fleet Management`_

*Requirements*
++++++++++++++
None.

*External References*
+++++++++++++++++++++
None.

*Rejected User Stories / Usage Scenarios*
-----------------------------------------
None.

Glossary
--------
* **Failure** - TBD
* **Remediation** - TBD
