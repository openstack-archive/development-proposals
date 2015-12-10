Rolling Upgrades
=============================

*Problem description*
---------------------
OpenStack operators often shy away from upgrading to the latest OpenStack
release due to concerns about the intrusiveness of upgrades. This prohibits
operators from realizing the complete value of their OpenStack cloud,
specifically their access to a constantly improving platform.

User Stories
------------
* As a Cloud User, I want to experience a stable, regularly updated
  OpenStack platform in order to utilize new features, bug fixes and
  security enhancements, so that my cloud development experience is
  consistently world-class.
* As a Cloud Operator, I want to provide my users a reliable and
  available OpenStack platform so that they do not experience any data
  plane or control plane downtime
* As a Cloud Operator, I want to have confidence in my ability to
  perform an OpenStack cloud upgrade so that I can perform them on a
  monthly basis
* As a Cloud Operator, I want to be able to roll back the most recent cloud
  upgrade I initiate in the event of issues so that I can be confident
  that even in the case of errors I will still avoid data plane or
  control plane downtime
* As a Cloud Operator, I want to be able to define characteristics of
  a rolling reboot of my data and control plane hosts so that my users
  are not impacted by a rolling upgrade

Usage Scenarios Examples
------------------------
1. Successful upgrade
    a. Cloud Operator schedules OpenStack upgrade to latest release
    b. Cloud Operator can be assured that API contracts are backwards 
       compatible
    c. Cloud Operator performs upgrade following simple documentation
    d. Cloud Operator notifies users of successful upgrade and new feature and
       enhancement availability
    e. Cloud Operator schedules next upgrade for 1 month's time to take
       advantage of backports and security updates
2. Unsuccessful upgrade
    a. Cloud Operator schedules OpenStack upgrade to latest  6 month release
    b. While performing upgrade Cloud Operator notices an unexpected error
    c. Cloud Operator rolls back the upgrade to a previously known, error-free
       state
3. Immediate Upgrade
    a. Cloud Operator is informed that a security vulnerability has been found
       in an OpenStack service and a patch is available for the current release
    b. Cloud Operator schedules an upgrade to the newest update
    c. After successfully completed the Cloud Operator's cloud is no longer
       vulnerable
4. Rolling Upgrade on Dataplane
    a. Cloud Operator schedules an OpenStack upgrade for a security
       vulnerability which requires reboots of the entire fleet of data-plane
       hosts
    b. Cloud Operator initiates the upgrade and performs the reboots of the
       dataplane hosts in an automated, configurable process
    c. Cloud Users are unaffected by the reboots

Opportunity/Justification
-------------------------
This is a large reason why enterprises fail to gain the full value of their
OpenStack cloud. **Upgrades have never been easy and in many environments
require downtime of both the control and dataplane.** This is an inherently
un-cloudy characteristic of the OpenStack platform. Fixing upgrades so would
clear up many concerns which limit OpenStack adoption today.

Related User Stories
--------------------
None.

*Requirements*
--------------
None.

*Gaps*
------
Upgrades today require downtime in the data plane, network connectivity and 
often control plane.

The current gaps preventing rolling upgrades span a number of fronts which can 
best be illustrated via a process for performing a rolling upgrade.

1. **Maintenance Mode**- Preventing the scheduling of additional instances on a
   host
2. **Live Migration**- Improvements to live migrating existing resources from
   hosts
3. **Upgrade Orchestration**- Orchestrating deployment of upgraded or new 
   versions of a service
4. **Versioned Objects**- Enabling communication between different versions of 
   the same OpenStack Service
5. **Online Schema Migration**- Enable database schema migrations without 
   requiring service downtime
6. **Graceful Shutdown**- Ensure services can be shut down without interrupting 
   requests in process
7. **Upgrade Orchestration**- Orchestrating removal of older versions of a 
   service
8. **Upgrade Orchestration**- Ease of use tools for performing upgrades across
   control and data plane hosts
9. **Upgrade Gating**- Gating projects on successful rolling upgrades
10. **Project Tagging**- Informing operators which projects can successfully
   perform rolling upgrades

For operators, a successful cloud upgrade involves all OpenStack services
deployed in a cloud. For that reason a number of these fronts require
enhancements to all projects likely deployed by operators. We'll review these
items first:

**Versioned Objects**
A version objects library exists in Oslo. Each individual project must consider
whether or not versioned objects is the right tool for the rolling upgrades
job. The following is the status of versioned objects for common OpenStack
projects:
* Nova - Implemented
* Neutron - Implemented
* Glance - Not Implemented
* Cinder - Implemented
* Swift - Not Applicable
* Keystone - Not Implemented
* Horizon - Not Implemented
* Heat - Implemented
* Ceilometer - Alternatives Proposed

**Online Schema Migration**
Online schema migration, like versioned object support, is solved in a variety
of fashions. Some projects propose standard schema expansion and contraction to
happen over an entire development cycle rather than online at the time of
upgrade. The following is the status of online schema migration for common
OpenStack projects:
* Nova - Alternative Adopted
* Neutron - Not Implemented
* Glance - Unknown
* Cinder - Not Implemented
* Swift - Unknown
* Keystone - Unknown
* Horizon - Unknown
* Heat - Unknown
* Ceilometer - Unknown

**Maintenance Mode**
Maintenance mode is only useful in those services where entire hosts are used
to create virtual resources. The following is the status of maintenance mode
for applicable OpenStack projects:
* Nova - Implemented
* Cinder - Not Implemented
* Swift - Implemented

**Live Migration**
Like maintenance mode, live migration is only applicable to those services
where hosts are providing resources. The following is the status of live
migration for applicable OpenStack projects:
* Nova - Implemented (needs some improvements)
* Cinder - Not Implemented
* Swift - Implemented

**Graceful Shutdown**
* Nova - Implemented
* Neutron - Implemented
* Glance - Unknown
* Cinder - Implemented
* Swift - Unknown
* Keystone - Unknown
* Horizon - Unknown
* Heat - Unknown
* Ceilometer - Unknown

Other fronts require work in specific orchestration projects or OpenStack infra
.

**Upgrade Orchestration**
Within OpenStack many of the cloud deployment mechanisms have made concerted
effort towards providing upgrade orchestration. The status of each deployment
methods approach to rolling upgrades follows:
* Triple O - Unknown
* Fuel - Unknown
* OpenStack Puppet - Unknown
* OpenStack Ansible - Upgrade scripts
* OpenStack Chef - Unknown

**Upgrade Gating**
OpenStack infra has not begun deploying upgrade tests, there is an available
project called grenade, into the gates for every project. 

**Project Tagging**
There is no project meta data tag to signify that a given OpenStack project is
capable of performing a rolling upgrade.

*Affected By*
-------------
None.

*External References*
---------------------
None.

Glossary
--------
**Control Plane** Hosts or infrastructure which operate OpenStack services
**Data Plane** Hosts or infrastructure which are managed by OpenStack services
