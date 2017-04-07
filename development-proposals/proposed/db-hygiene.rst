Database cleanup of deleted object
==================================

Cross Project Spec - None

User Story Tracker - None

Problem Description
-------------------

Problem Definition
++++++++++++++++++
Each operator of an OpenStack cloud needs the ability to clean up the OpenStack
database of objects which have been deleted. Currently a new record is created in
the OpenStack database when an object (project, user, VM, network, volume, swift
object, etc.) is created. When an object is deleted its record in the database
remains but is marked as deleted.  As an OpenStack cloud stays in operation over
time, the number of records in the database fills with deleted object records and
soon the database becomes too large. This can result in the database consuming
significant resources on the controller node(s) and impacting responsiveness of
the database, even bringing down controller(s).

While a record for deletion of an object is needed for cloud governance it is
not a requirement for the database to retain this record. Thus, some tool is
needed for OpenStack operators to cleanup the database of records from deleted
objects.

* As part of a PoC of an OpenStack cloud, an operator needs a tool to purge the
database of deleted records. This is needed in order to be able to rerun the same
test tool that would create objects every run as well as testing actual growth of
the database for operational conditions not OpenStack implementation artifacts.

* As an operator of an OpenStack cloud I need an ability to remove records of
deleted objects from the database after storing those records for audit purposes.

* As a cloud deployment engineer, I need to be able to re-run the same tests
(with same objects) in a repeatable manner so that I can have a high certainty
in the outcome of my proof of concept and cloud functionality.

* As a cloud deployment engineer, I need only the appropriate records in my
database so that I can complete my upgrade in the allocated down time.

Opportunity/Justification
+++++++++++++++++++++++++
DB hygiene is required for handling OpenStack performance, operational and
upgrade issues. This ensures that historical records of deleted items are not
impacting operational performance and such deleted items are not polluted by
upgrades.

Requirements Specification
--------------------------

Use Cases
+++++++++
This section utilizes the `OpenStack UX Personas`_.

* As `Rey the Cloud Operator`_, I need an ability to remove records of
  deleted objects from the database after storing those records for audit purposes.

* As `Adrian the infrastructure architect`_, I need to be able to re-run the same tests
  (with same objects) in a repeatable manner so that I can have a high certainty
  in the outcome of my proof of concept and cloud functionality.

* As Rey, I need only the appropriate records in my
  database so that I can complete my upgrade in the allocated down time.

.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html
.. _Adrian the infrastructure architect: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/infrastructure-arch.html
.. _Rey the cloud operator: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/cloud-ops.html

Usage Scenarios Examples
++++++++++++++++++++++++
WIP

Related User Stories
++++++++++++++++++++
Nova specs:

* https://review.openstack.org/#/c/184645/
* https://review.openstack.org/#/c/184637/
* https://review.openstack.org/#/c/137669/

Cinder blueprint:

* https://blueprints.launchpad.net/cinder/+spec/db-cleanup

Requirements
++++++++++++
* Operator should be able to specify which policy to apply for deleted objects
* Operator should be able to specify which policy to apply for different tenants
  and sub-tenants.
* At least two policies must be supported: Policy 1 - Archive the records in
  other persistent storage for a specific interval duration; Policy 2 - Remove
  the records from database permanently.

External References
+++++++++++++++++++
None.

Rejected User Stories / Usage Scenarios
---------------------------------------
None.

Glossary
--------
None.
