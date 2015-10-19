Database cleanup of deleted object
============================================

*Problem description*
---------------------
Each operator of the openstack need an ability to clean up openstack database
of the objects that has been deleted. Currently a new record is created in
OpenStack database when an object (project, user, VM, network, volume, swift
object, etc.) is created. When an object is deleted by a user/admin its record
in database remains but is marked as deleted.  As Openstack cloud stays in
operation over time the number of records in database continues to grow with
deleted objects record and database becomes too large consuming resources on
controller node(s) and impacting responsiveness of database, or even crushing
controller(s).

While a record for deletion of an object is needed to cloud governance it does
not require that this record remain in database. Thus, some tool is needed for
openstack operator to cleanup database from records of deleted objects.

* As part of PoC of OpenStack cloud an operator needs a tool to purge database
of deleted records. That is need to be able to rerun the same test tool that
would create the same objects every run as well as testing actual grown of
database for operational condition not OpenStack implementation artifacts.

* As an operator of OpenStack cloud I need an ability to remove records of
deleted objects from database. But I need to store records for audit purpose.

* As a cloud deployment engineer, I need to be able to re-run the same tests
(with same objects) in a repeatable manner so that I can have a high certainty
in the outcome of my proof of concept and cloud functionality.

* As a cloud deployment engineer, I need only the appropriate records in my
database so that I can complete my upgrade in the allocated down time.

Usage Scenarios Examples
------------------------
TBD

Opportunity/Justification
-------------------------
None.

Related User Stories
--------------------
Nova specs:
* https://review.openstack.org/#/c/184645/
* https://review.openstack.org/#/c/184637/
* https://review.openstack.org/#/c/137669/

Cinder blueprint:
* https://blueprints.launchpad.net/cinder/+spec/db-cleanup

*Requirements*
--------------
* Operator should be able to specify which policy to apply for deleted objects
* Operator should be able to specify which policy to apply for deleted objects
* Operator should be able to specify which policy to apply for different 
Tenants and even subtetants.
* At least two policy must be supported: permanent deletion and audit, where
records are removed from database but stored for compliance interval duration
in persistent storage.

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
--------
None.

