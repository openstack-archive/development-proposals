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

This system also has the potential of building a closed-loop feedback mechanism
whereby operating OpenStack clouds can have their failures centrally reported
in a place where other operators, users and developers can react. This reaction
can take the form of adopting known remediations, improving code to prevent
further failures and adapting code to provide resiliency around known failure
scenarios.

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

* As a Cloud Developer, I want to access the known reported failures and
  recovery strategy so I can build the appropriate detection mechanisms and
  resiliency into my design.

* As an OpenStack Developer, I want to have access to known reported failures
  and recovery strategy so I can improve my code in such a way to limit
  failures.

Usage Scenario Examples
+++++++++++++++++++++++
1. Minimally Viable Centralized Failure Reporting
  a. Operator X encounters failure
  b. Operator X reviews minimal set of required fields for submission
  c. Operator X complete submission of failure
  d. `OpenStack Failure Work Group`_ reviews and categorizes submission
  e. Failure Work Group identifies similarity between submission from
     Operator X and Operators A,B & C
  f. Failure Work Group publishes known remediation common between reported
     submissions

2. Advanced Centralized Failure Reporting
  a. Operator X, Y and Z encounter similar failures and report them to Failure
     Work Group database
  b. Operator A provides a known remediation to the failure to the Failure Work
     Group database
  c. Failure Work Group members reviews reports and determines reports from X,
     Y and Z are symptomatic of the failure and remediation provided by A
  d. Failure Work Group publishes A's known working remediation to the database
  e. Future similar failure events in Operator X,Y,Z and A's clouds are
    automatically remediated using the known working remediation

3. Automated Usage of Centralized Failure Reporting
  a. Operators W,X,Y and Z report a common failure to the Failure Work Group
     database
  b. Operator B reports a known remediation for the common failure to the
     Failure work group database.
  c. The Failure Work Group database recognizes the common reports are in fact
     common
  d. The Failure Work Group system verifies the remediation submitted by
     Operator B remediates the common failure
  e. The Failure work Group system publishes the known remediation to all
     subscribed OpenStack Clouds, including W, X, Y and Z and all incorporate
     the automatic remediation and no longer have to manually resolve the
     failure

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
* **Failure** - An operational incident which results in performance or
  functional degradation of service.
* **Remediation** - An operational process by which a failure is identified,
  triaged and removed.

..  _Fleet Management: http://specs.openstack.org/openstack/openstack-user-stories/user-stories/proposed/fleet-management.html
..  _OpenStack Failure Work Group: https://etherpad.openstack.org/p/Fault_Genes-WG
