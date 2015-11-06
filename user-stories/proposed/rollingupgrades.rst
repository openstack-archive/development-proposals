Rolling Upgrades
=============================
**Sections in** *italics* **are optional.**

*Problem description*
---------------------
OpenStack operators often shy away from upgrading to the latest OpenStack
release due to concerns about the intrusiveness of upgrades. This prohibits
operators from realizing the complete value of their OpenStack cloud,
specifically their access to a constantly improving platform.

User Stories
------------
* As a Cloud User, I want to experience a consistently updated
  OpenStack platform in order to utilize new features, bug fixes and
  security enhancements, so that my cloud development experience is
  consistently world-class.
* As a Cloud Operator, I want to provide my users a reliable and
  available OpenStack platform so that they do not experience any data
  plane or control plane downtime
* As a Cloud Operator, I want to have confidence in my ability to
  perform an OpenStack cloud upgrade so that I can perform them on a
  monthly basis
* As a Cloud Operator, I want to be able to roll back any cloud
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
    b. Cloud Operator can be assured that API contracts are backwards compatible
    c. Cloud Operator performs upgrade following simple documentation
    d. Cloud Operator notifies users of successful upgrade and new feature and
       enhancement availability
    e. Cloud Operator schedules next upgrade for 1 month's time to take
       advantage of backports and security updates
2. Unsuccessful upgrade
    a. Cloud Operator schedules OpenStack upgrade to latest release
    b. While performing upgrade Cloud Operator notices an unexpected error
    c. Cloud Operator rolls back the upgrade to a previously known, error-free
       state
3. Immediate Upgrade
    a. Cloud Operator is informed that a security vulnerability has been found
       in an OpenStack service and a patch is available for the current release
    b. Cloud Operator schedules an upgrade to the newest release
    c. After successfully completed the Cloud Operator's cloud is no longer
       vulnerable
4. Rolling Upgrade on Dataplane
    a. Cloud Operator schedules an OpenStack upgrade for a security
       vulnerability which requires reboots of the entire dataplane hosts
    b. Cloud Operator initiates the upgrade and performs the reboots of the
       dataplane hosts in an automated, configurable process
    c. Cloud Users are unaffected by the reboots

Opportunity/Justification
-------------------------
This is a large reason why enterprises fail to gain the full value of their
OpenStack cloud. Upgrades have never been easy and in many environments require
**downtime of both the control and dataplane.** This is an inherently un-cloudy
characteristic of the OpenStack platform. Fixing upgrades so would clear up
many concerns which limit OpenStack adoption today.

Related User Stories
--------------------
None.

*Requirements*
--------------
None.

*Gaps*
------
Upgrades today require downtime in the data plane, network connectivity and often
control plane.

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
