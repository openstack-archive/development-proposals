Database cleanup of deleted object
============================================

*Problem description*
---------------------
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
* Operator should be able to specify which policy to apply for different tenants 
and sub-tenants.
* At least two policies must be supported: permanent deletion and audit, where
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