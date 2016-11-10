Openstack Extreme Testing
==========================
**Sections in** *italics* **are optional.**

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

*Problem Definition*
++++++++++++++++++++

In order to provide competitive service to the customers, openstack operators
are upgrading components, integrating new hardware, scaling up, and making
lots of configuration changes in frequent manner. However, all of those
variations are not tested in current openstack test systems. Most of the
openstack cloud service providers conduct tests by their own before introduce
new changes to production. Those tests include integration testing, component
interface testing, operational acceptance testing, destructive testing,
concurrent testing, performance testing, etc.. Current openstack ecosystem
has unit, functional, and integration testing, and most of the above listed
tests are not or partially implemented in the ecosystem.


Opportunity/Justification
+++++++++++++++++++++++++

These test can significantly improve the overall quality of the OpenStack
and dramatically reduce the delivery time.


Use Cases
---------

User Stories
++++++++++++

* Destructive testing
  As a cloud operator, I would like to have all the openstack projects to be
  tested for destructive scenarios.

* Concurrent testing
  As a cloud operator, I would like to have all the openstack projects to be
  tested before stable release for concurrent testing.


Usage Scenario Examples
+++++++++++++++++++++++

* Destructive testing
  Destructive testing attempts to cause the part of system ( HW or SW ) fail
  and verifies that the system operates properly even in such conditions:

  - Shutdown a control node where api services are running and verify that API
    requests are processed as expected

  - Restart of network switches and verify that services can recover
    automatically

  - Restart some OpenStack services and verify that service can recover
    in expected downtime.

  - Generate DB/RabbitMQ downtime and verify that there are no request
    loss or non-recoverable errors in the system.



Related User Stories
++++++++++++++++++++

None.

*Requirements*
++++++++++++++

None.

*External References*
+++++++++++++++++++++

* `Destructive testing (os-faults library and Stepler framework) <https://etherpad.openstack.org/p/ocata-qa-destructive-testing>`_

* `HA Failure Test <https://github.com/avdhoot07/HA-Failure-TEST>`_

* `RBAC policy testing <https://etherpad.openstack.org/p/ocata-qa-policy-testing>`_


*Rejected User Stories / Usage Scenarios*
-----------------------------------------

None.

Glossary
--------
