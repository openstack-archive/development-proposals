OpenStack Extreme Testing
==========================

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

*Problem Definition*
++++++++++++++++++++

In order to provide competitive service to the customers, OpenStack operators
are upgrading components, integrating new hardware, scaling up, and making
configuration changes in frequent manner. However, all of those
variations are not tested in current OpenStack test systems. Most of the
OpenStack cloud service providers conduct tests by themselves before introducing
new changes to production. Those tests include integration testing, component
interface testing, operational acceptance testing, destructive testing,
concurrent testing, performance testing, etc.. Currently the OpenStack ecosystem
has unit, functional, and integration testing, and most of the above listed
tests are missing or only partially implemented in the ecosystem.


Opportunity/Justification
+++++++++++++++++++++++++

These extended tests can significantly improve the overall quality of the
OpenStack and dramatically reduce the delivery time to introduce a new release
or new changes to production environment. Tests will be run before stable
release by the QA team or even more collaboratively by the 3rd
parties CI interface, spreading the cost of pre-stable testing and increasing
the amount of issues reported for fix before release.
However, testing upstream code with all possible combinations of HW and
configurations is not practical. One possible solution is, QA team will
run these extended tests on few pre-selected reference architectures and
other architectures will be added as 3rd party CIs.
After release the tests can be used by each distributor in their stabilization
processes and finally each operator as they stabilize their configuration
and each deployment. Currently operators are doing these extended tests
by themselves and not collaborating and taking advantage of each other.


Requirements Specification
--------------------------

Use Cases
+++++++++

This section utilizes the `OpenStack UX Personas`_.


* Destructive testing

  As `Rey the Cloud Operator`_, I would like to have all the OpenStack projects
  to be tested for destructive scenarios on OpenStack cloud system with
  `High Availability <http://docs.openstack.org/ha-guide/>`_ configurations
  such as controller node high availability, Networking, Storage, Compute
  service high availability etc..
  So that as we deploy OpenStack into production we have fewer situations in
  which OpenStack functions themselves fail (bugs fixed beforehand) and
  for others we avoid or can plan to mitigate with our specific configurations.

  .. todo:: Add the details of reference architecture for Destructive testing

* Concurrent testing

  As Rey, I would like to have following OpenStack projects to be
  tested before stable release for concurrent testing. So that as we deploy
  OpenStack into production environments we are confident that a real world
  situation of simultaneous function calls does not fail.

  Openstack Projects for extended testing
   * Nova
   * Cinder
   * Glance
   * Keystone
   * Neutron
   * Swift


.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html
.. _Rey the Cloud Operator: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/cloud-ops.html#cloud-ops

Usage Scenario Examples
+++++++++++++++++++++++

**Destructive testing**

Destructive testing simulates when part of the underlying OpenStack
infrastructure (HW or SW) or a component of OpenStack itself fails
or needs to be restarted and verifies that the system operates
properly even in such conditions:

* Shutdown a control node where API services are running and verify that API
  requests are processed as expected
* Restart of network switches and verify that services can recover
  automatically
* Restart some OpenStack services and verify that service can recover
  in expected downtime.
* Generate DB/RabbitMQ downtime and verify that there are no request
  loss or non-recoverable errors in the system.
* Shut  off a hardware blade

  .. todo:: Add more details to each test case
	    (ref: Destructive testing reference architecture)

**Concurrent testing**

Concurrent testing issues requests to a functioning OpenStack cloud more
than 1 at a time. This can be the same functional request but for 2
different users or different functional requests but accessing the
same resource. Expected result is that the functions complete in the
same manner as they did when not issued simultaneously.
Openstack Rally can use to conduct these concurrent tests.

* Tenants added at the same moment
* Networks requested at the same moment
* In a constrained storage environment a release of storage and request
  for that storage happen at the same time.
* Simultaneously shelve and migrate instance and then unshelve the instance
* Simultaneously create multiple snapshots from an instance


Related User Stories
++++++++++++++++++++

None.

*Requirements*
++++++++++++++

None.

*External References*
+++++++++++++++++++++

* `Destructive testing (os-faults library and Stepler framework) <https://etherpad.openstack.org/p/ocata-qa-destructive-testing>`_

* `OS Faults <https://github.com/openstack/os-faults>`_

* `HA Failure Test <https://github.com/avdhoot07/HA-Failure-TEST>`_

* `RBAC policy testing <https://etherpad.openstack.org/p/ocata-qa-policy-testing>`_

* `Cloud99 <https://github.com/cisco-oss-eng/Cloud99>`_


*Rejected User Stories / Usage Scenarios*
-----------------------------------------

None.

Glossary
--------

None.
