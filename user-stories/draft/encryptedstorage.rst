Encrypted Storage
==================

*Problem description*
---------------------
Each enterprise has its own data classification strategy. The types of data
include: financial data, personal data, health data, confidential business
data, etc. Some enterprise (especially in banking, finance and insurance
industry) has stringent data requirements in order to be compliant with laws
and regulations. For example, PCI DSS Requirement 3.4 states that credit card
personal account number must be rendered unreadable anywhere it is stored
(including portable digital media, backup media and logs). Applications
(including database) that interact with these classes of information need to be
able to specify encrypted storage requirements when the application is launched
and interacts with some of these classes. The data must be encrypted in motion
as well as at rest. The application should not require admin privileges to
access encrypted storage.
 
In addition, proper key management process need to be in place. The keys used
to encrypt/decrypt the data must be changed on a regular basis and the access
of keys are restricted to authorized personnel only.

User Stories
------------
* As the Enterprise IT Manager, I must ensure the appropriate security for the HR
department database with employee records that services several department
applications. I would like to move the database into our companies private cloud
so I don’t need to maintain the system it currently lives on. However, because of
the critical nature of the information in the database our company policy does
not allow this information to reside on any shared system in an unencrypted
state. To be able to move the database into the private cloud I need to ensure
that the stored data and all data in transit from/to the VM will be encrypted.
While the HR Department would love to have improved uptime for their database,
they are used to having to manually restart/reboot as needed and can live with
this in the cloud as well.

* I am the Enterprise IT manager for an insurance company. My company maintains a
database with insurer’s credit card records for annual renewal purpose. Our
company would like to move the database into our OpenStack private cloud. In
order to comply with company security policy, government laws and financial
regulations, I need to ensure that information stored in the private cloud
(including backup) is encrypted, and the keys used to encrypt the data are
rotated/changed annually.

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
* A block & object storage option that includes encryption / decryption at the VM
source.
*  A method for the application to specify that it requires a block storage
system that includes encryption / decryption at the VM source.
* OpenStack services to enforce the storage requirements for the application
* A method for changing the key used to encrypt/decrypt the data after a specific
period of time.
*The database application needs to be able to specify that it needs an encrypted
storage system that supports encryption / decryption at the VM source, in
addition to at rest.
*The storage system must be able to handle both Reads/Writes of persistent
encrypted block storage in excess of 1TB device to be backed up nightly.

*Gaps*
------
**Cinder issues:**
* The basic storage encryption functionality looks like it may exist, but
requires admin status. Creating encrypted volumes should not require admin
status.

*Affected By*
-------------
At the Hong kong summit there was a talk on barbican/cinder/nova for this type of
functionality. Don’t know if it was successfully integrated into OpenStack yet.
https://www.openstack.org/summit/openstack-summit-hong-kong-2013/session-videos/p
resentation/encrypted-block-storage-technical-walkthrough

* There is a spec located at: https://wiki.openstack.org/wiki/VolumeEncryption
for some early work and the current documentation is located at:
http://docs.openstack.org/juno/config-reference/content/section_create-encrypted-
volume-type.html where it implies that admin privilege is required.

*External References*
---------------------
None.

Glossary
========
None.