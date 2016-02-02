Rolling Updates and Upgrades
=============================

*Problem description*
---------------------
OpenStack operators often shy away from upgrading or updating OpenStack due to
concerns about the intrusiveness of upgrades. This prohibits operators from
realizing the complete value of their OpenStack cloud, specifically their
access to a constantly improving platform and interoperability with an
expanding OpenStack ecosystem.

The use cases below cover deployments based directly on the OpenStack upstream
code base. While some of the features may be utilized by distribution providers
to improve their support for non-disruptive updates and upgrades, they are not
specifically covered in this document.

User Stories
------------
* As a Cloud User, I want to experience a stable, regularly updated and
  upgraded OpenStack platform in order to utilize new features, bug fixes and
  security enhancements, so that my cloud development experience is
  consistently world-class.
* As a Cloud Operator, I want to provide my users a reliable and
  available OpenStack platform so that they do not experience any data
  plane or control plane downtime
* As a Cloud Operator, I want to have confidence in my ability to
  perform an OpenStack cloud update so that I can perform them on a
  monthly basis
* As a Cloud Operator, I want to be able to roll back the most recent cloud
  upgrade or update I initiate in the event of issues so that I can be
  confident that even in the case of errors I will still avoid data plane or
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
    e. Cloud Operator schedules next update for 1 month's time (or as needed)
       to take advantage of backports, bug fixes and security updates
2. Unsuccessful Update/Upgrade
    a. Cloud Operator schedules OpenStack upgrade to latest  6 month release
    b. While performing upgrade Cloud Operator notices an unexpected error
    c. Cloud Operator rolls back the upgrade or update to a previously known,
       error-free state
3. Immediate Update
    a. Cloud Operator is informed that a security vulnerability has been found
       in an OpenStack service and a patch is available for the current release
    b. Cloud Operator schedules an update to correct the vulnerability
    c. After successfully completed the Cloud Operator's cloud is no longer
       vulnerable
4. Rolling Upgrade on Dataplane
    a. Cloud Operator schedules an OpenStack upgrade or update for a security
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
7. **Upgrade Orchestration**- Orchestrating potential removal of older versions
   of a service and cleanup
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
* Neutron - Not Implemented
* Glance - Not Applicable
* Cinder - In Progress, Not Required
* Swift - Not Applicable
* Keystone - Not Applicable
* Horizon - Not Applicable
* Heat - Implemented
* Ceilometer - Alternatives Proposed

**Online Schema Migration**

Online schema migration, like versioned object support, is solved in a variety
of fashions. Some projects propose standard schema expansion and contraction to
happen over an entire development cycle rather than online at the time of
upgrade. The following is the status of online schema migration for common
OpenStack projects:

* Nova - Policy Implemented (Expand/Contract)
* Neutron - Implemented - Hardening Required
* Glance - Unknown
* Cinder - Policy Implemented (Expand/Contract)
* Swift - Unknown
* Keystone - Policy Implemented (Expand/Contract)
* Horizon - Unknown
* Heat - In Progress
* Ceilometer - Unknown

**Maintenance Mode**

Maintenance mode is only useful in those services where entire hosts are used
to create virtual resources. The following is the status of maintenance mode
for applicable OpenStack projects:

* Nova - Implemented
* Cinder - Implemented
* Neutron - Implemented
* Ceilometer - Unknown
* Swift - Implemented

**Live Migration**

Like maintenance mode, live migration is only applicable to those services
where hosts are providing resources. The following is the status of live
migration for applicable OpenStack projects:

* Nova - Implemented (needs some improvements)
* Cinder - Not Implemented (depends on backend)

**Graceful Shutdown**

Graceful shutdown is applicable to all common OpenStack services and should
result in services being able to be shutdown only after existing requests have
been processed. The following is the status of graceful shutdown across common
OpenStack projects:

* Nova - Implemented
* Neutron - Implemented
* Glance - Unknown
* Cinder - Implemented
* Swift - Unknown
* Keystone - Unknown
* Horizon - Unknown
* Heat - Unknown
* Ceilometer - Unknown

Other fronts require work in specific orchestration projects or OpenStack infra.

**Upgrade Orchestration**

Within OpenStack many of the cloud deployment mechanisms have made concerted
effort towards providing upgrade orchestration. Depending on the reference
architecture each deployment mechanism will determine the appropriate order and
methodology for performing a rolling upgrade. The status of each deployment
methods approach to rolling upgrades follows:

* Triple O - Unknown
* Fuel - Task Based Deployment
* OpenStack Puppet - Unknown
* OpenStack Ansible - Upgrade scripts
* OpenStack Chef - Unknown
* Kolla - In Progress

**Upgrade Gating**

OpenStack infra has not begun deploying upgrade tests into the general gate.
There is an available multi-node upgrade test framework called Grenade. Some
projects have begun including upgrade tests in their gates.

* Nova - Gated by multi-node Grenade test
* Neutron - None
* Glance - None
* Cinder - None
* Swift - Unknown
* Keystone - None
* Heat - None
* Ceilometer - None

**Project Tagging**

There are project meta data tags to signify that a given OpenStack project is
capable of performing a rolling upgrade.
* Status - Implemented

*Affected By*
-------------
None.

*External References*
---------------------
* `Dan Smith's Upgrade Blog Series <http://www.danplanet.com/blog/tag/nova-upgrade-details/>`_
* `Rolling Upgrades Project Meta Data Tag <https://github.com/openstack/governance/blob/master/reference/tags/assert_supports-rolling-upgrade.rst>`_
* `Grenade - OpenStack Upgrade Test Harness <https://wiki.openstack.org/wiki/Grenade>`_


Glossary
--------
* **Control Plane** Hosts or infrastructure which operate OpenStack services
  (e.g. nova-api)
* **Data Plane** Hosts or infrastructure which are managed by OpenStack
  services (e.g. VM running on the hypervisor)
* **Upgrade** Installing an entirely different OpenStack major software release
  with new versions available twice a year
* **Update** Installing new OpenStack software, typically from a stable branch,
  to gain access to bug fixes, security patches etc. These can happen as
  frequently as needed
* **Rollback** Performing an upgrade or update, and whether the result of errors,
  inconsistencies or lack of appropriate preparation subsequently returning to
  the pre-upgrade or update version. It is understood that any actions or data
  created after upgrade or update would likely be lost as the result of a
  rollback.
