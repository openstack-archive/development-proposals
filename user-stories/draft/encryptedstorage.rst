Encrypted Storage
==================

*Problem description* 
---------------------  
* Enterprises typically have their own data classification strategies. The types
of data stored typically include (but are not limited to): financial, personal,
health, and confidential business data. Some enterprises (especially finance and
health care industries) have stringent data requirements in order to be
compliant with regional law and regulations. For example, PCI DSS Requirement
3.4 states that credit card payment details must be rendered unreadable anywhere
they are persistently stored (including portable digital media, backup media and
logs). Applications (including database back-ends) that interact with these
classes of data need to be able to specify encrypted storage requirements when
an application is launched and interacts with some of these data classes. The
data must be encrypted both in flight as well as at rest. The application should
not require administrative privileges to specify or access encrypted storage.
In addition, proper key management processes need to be in place. The keys used
to encrypt/decrypt the data must be rotated on a regular basis and the access of
keys are restricted to authorized personnel only.

User Stories
------------
* As the Enterprise IT Manager, I must ensure the appropriate security for the
HR Department database containing employee records that services several
applications. I would like to migrate the database into our company's
OpenStack private cloud so that I do not need to maintain the system it
currently resides on. However, because of the sensitive nature of the
information in the database our company policy does not allow this 
information to reside on any shared system in an unencrypted form. To be able
to move the database into the private cloud I need to ensure that the
persistently stored data and all data in flight to/from the instance is
encrypted. While the HR Department would like to have improved uptime for
their database, they are used to having to manually restart/reboot as needed
and can live with this in the cloud as well.

* I am the Enterprise IT manager for an insurance company. My company
maintains a database with insurer’s credit card records for annual renewal
purposes. Our company would like to move the database into our OpenStack
private cloud. In order to comply with company data classification policy,
government law and financial regulations, I need to ensure that information
stored in the private cloud (including backups) is encrypted in flight and
at rest, and that keys used to encrypt the data are rotated annually.

Usage Scenarios Examples
------------------------
None.

Opportunity/Justification
-------------------------
None.

Related User Stories
--------------------
* An application needs to be able to specify networking requirements
* An application needs to be able to specify workload isolation requirements

*Requirements*
--------------

* A block & object storage solution that enables encryption/decryption at the
instance source
* A block & object storage solution that enables encryption/decryption for
data at rest
* A method for the application to specify that it requires a block storage
system that includes encryption/decryption at the instance
* A method for rotating the key used to encrypt/decrypt the data after a
specific period of time
* OpenStack services to enforce the storage requirements for the application
* The application needs to be able to specify that it requires an encrypted
storage system that supports either or both encryption/decryption at the
instance, in addition to at rest.


*Gaps*
------
**Cinder issues:**
* The storage encryption functionality exists, but requires admin status.
Creating encrypted volumes should not require admin status.
* Encryption keys are set at creation time, however it is not clear how to
rotate the key(s), once a volume is in use. Rotating keys is a requirement of
many data storage standards.

**Swift issues:**
* At present an application is responsible for encrypting Objects prior to
calling a PUT operation, swift will store any object that is in the PUT
request. Swift should reject object PUTs that are tagged to be encrypted by
the application.
* Development of a data at rest solution is currently under development,
however, this does not solve for in flight data.


*Affected By*
-------------

* At the Hong Kong summit there was a talk on barbican/cinder/nova for this
type of functionality. Don’t know if it was successfully integrated into
OpenStack yet. https://www.openstack.org/summit/openstack-summit-hong-
kong-2013/session-videos/presentation/encrypted-block-storage-technical-
walkthrough

* There is a spec located at: https://wiki.openstack.org/wiki/VolumeEncryption
for some early work and the current documentation is located at:
http://docs.openstack.org/liberty/config-reference/content/section_create-
encrypted-volume-type.html where it implies that admin privilege is required.

* There is a spec located at: https://wiki.openstack.org/wiki/ObjectEncryption
which documents the approach for object encryption (at rest).

*External References*
---------------------
None.

Glossary
--------
* Data in Flight - Data in transit between an instance and storage system
* Data at Rest - Data stored persistently on a storage system
