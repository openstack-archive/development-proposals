Fleet Management
================
Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

Problem Definition
++++++++++++++++++
While there are many open-source life-cycle management and deployment tools
for initial deployment of OpenStack (Day 1), there is a need for tools which
integrate with these projects to help cloud operators manage their environment
in the days after it is set up (Day 2 and beyond).

Today, this gap is filled through proprietary management tools provided either
by OpenStack distributors, third parties or bespoke code written by the
end-users operators themselves.

The use of these proprietary or bespoke tools and extensions creates either a
dependency and lock-in (if from a vendor) or a continuing maintenance task for
the end-user.

Opportunity/Justification
+++++++++++++++++++++++++
In user survey and market data complexity and uncertainty of day-two operations
is highlighted as a barrier to OpenStack adoption. Providing an in-community
option for Fleet Management would significantly lower the real and perceived
burden on operations teams responsible for keeping on OpenStack cloud running.

While there are available Operations management systems, most take a
traditional approach. An OpenStack fleet management system should be built on
the IaaS and cloud principles upon which OpenStack is based.

Many companies have already spoken publicly about their ongoing efforts in
writing and maintaining tools to manage their private OpenStack deployments.
Some have even started open-sourcing parts of their toolset to gather support
from community developers.

Rackspace has developed its own tools for use in the Rackspace Public Cloud,
and is actively considering open-sourcing parts of it, based on requests from
its Private Cloud customers. The new Watcher project within OpenStack is also
an attempt to address some aspects of this problem.

Use Cases
---------

Use Cases
+++++++++
* FLT001 - As a cloud operator, I need to track and utilize the status of
  physical resources in my OpenStack cloud - controller, network, compute,
  storage, and utility/logging nodes, and factors like power, temperature, CPU,
  memory, disk space, disk i/o, bandwidth (in/out) on each physical resources
  - so that I may monitor those metrics and maintain the health of my cloud

* FLT002 - As a cloud operator, I need to monitor the health of physical
  resources in my OpenStack cloud so that I can take automatic policy-driven
  remedial action and deliver on my SLAs

* FLT003 - As a cloud operator, I need to keep track of unused resource
  capacity so that I can free up resources and use them more efficiently

* FLT004 - As a cloud operator, I need to keep track of system alerts and
  messages, so that I can take remedial action and maintain the health of my
  cloud

* FLT005 - As a cloud operator, I need to check my deployed physical resources
  against a set of policies and rules, so that I can meet security,
  availability and other requirements

* FLT006 - As a cloud operator, I only want to have a human make an operational
  decision when it adds value or automation is not able to

* FLT007 - As a cloud operator, I need to utilize an automatic remediation
  system which identifies inconsistencies, determines if physical resources are
  in the appropriate state and takes remedial action if they are not

* FLT008 - As a cloud operator, I need to define and adjust automated remedial
  actions on physical resources so that they are least disruptive to my
  end-users

* FLT009 - As a cloud operator, I need to execute automated remedial actions as
  a result of my investigations into alerts

* FLT010 - As a cloud operator, I need to apply patches and updates to my
  physical resources, and maintain audit logs, so that I can keep my
  environment updated and secure, and roll back to prior validated
  configurations when something goes wrong with a patch or update

* FLT011 - As a cloud operator, I need to be able to retrieve the current state
  of my hardware resources and verify if there are any inconsistencies with
  respect to the right operating system, OpenStack services or other services
  installed.

* FLT012 - As a cloud operator, I should be able to leverage the deployment and
  life-cycle management tooling of my choice as the executor of my automated
  actions.

* FLT013 - As a cloud operator, I should be able to choose which components of
  the fleet management tooling (inventory, auditing, remediation, human
  interaction) I utilize

* FLT014 - As a cloud operator, I should be able to set a repeatability
  threshold for each alert so the resolving system does not take action on
  auditor alerts which happen repeatedly.

Use Case Prioritization
+++++++++++++++++++++++
**Phase 1** - Modularity and Inventory Management
 #. FLT013
 #. FLT002
 #. FLT001
 #. FLT004
 #. FLT003
**Phase 2** - Auditing and Automated Resolution
 #. FLT012
 #. FLT006
 #. FLT011
 #. FLT005
 #. FLT007
 #. FLT008
 #. FLT009
 #. FLT010
 #. FLT014

Usage Scenario Examples
+++++++++++++++++++++++
**Specific - Automated Security Hardening**

In this example an operator desires to apply a series of security best
practices to all of the hosts in their fleet.

* Cloud operator determines security requirements and derives or determines an
  `automation script`_ to apply requirements
* Cloud operator is already using inventory management to manage their fleet
* Cloud operator determines for which hosts the security requirements are
  applicable
* Cloud operator defines the desired states for specified hosts as compliant
  with automation script
* Fleet management system automatically audits status of automation script on
  hosts and remediates by running script where required
* Cloud operator is sure that future hosts added to fleet will have security
  requirements applied by fleet management system

.. _automation script: http://docs.openstack.org/developer/\
                      openstack-ansible-security/

**Specific - Automated Host OS Patching**

In this example a cloud operator desires to apply an updated patch for specified
hosts within their fleet.

* Cloud operator determines specified OS patch to update hosts with
* Cloud operator determines host group to update
* Cloud operator defines desired state for host group as including specified
  host OS patch
* Fleet management system audits host group to determine whether they have been
  patched with specified host OS patch
* Prior to taking any disruptive action, fleet management system will attempt
  to live migrate all workloads off of hosts and put a host into maintenance
  mode
* Fleet management resolves specified hosts who do not have patch by applying
  patch

**Specific - Automated Networking Maintenance**

In this example a cloud operator is performing a maintenance on a piece of
network hardware that will impact networking access to a series of hosts.

* Cloud operator determines networking hardware requires maintenance
* Cloud operator identifies networking hardware requiring maintenance to
  fleet management system
* Fleet management system takes remedial action to limit impact of maintenance
  including

  * Live migrating workloads from affected compute hosts
  * Deploy additional control plane instances to replace affected
    infrastructure hosts
  * Put compute hosts into maintenance mode
* After maintenance fleet management system returns affected hosts to available
  pool

**General Lifecycle**

In this process cloud operators are faced with three tasks: detection, trigger
and resolution. The lifecycle moves through the following phases.

#. Manual Detection, Manual Trigger, Manual Resolution
#. Automatic Detection, Manual Trigger, Manual Resolution
#. Automatic Detection, Manual Trigger, Automatic Resolution
#. Automatic Detection, Automatic Trigger, Automatic Resolution

Here is a real world description of this process:

* User reports an outage
* Cloud operator performs manual discovery and manual resolution
* During RCA cloud operator identifies method to automatically detect outage
* Cloud operator implements automatic detection in auditor system
* After repeated detection cloud operator describes method for automated
  remediation via code or run-book
* Cloud operator implements automatic remediation in resolver system
* Cloud operator implements automatic trigger from auditor to resolver system

**General - Automated Remediation**

* Monitoring triggers a warning on physical resources
* Auditing system determines physical resource in question is not in
  appropriate state for its resource type
* Where applicable, resolving system removes physical resources from production
  pool
* Resolving system returns physical resources to appropriate state
* Resolving system returns physical resources to production pool

**General - Operator Notification and Manual Remediation**

* Monitoring triggers a warning on physical resources
* Auditing system determines physical resource in question is in appropriate
  state
* Resolving system removes physical resources from production pool
* Resolving system informs cloud operator of need for investigation, removes
  resources from resolving system management
* Cloud operator investigates and determines cause of issue
* Cloud operator returns resource to resolving system management
* Resolving system returns physical resources to production pool

**General - Cloud Operator Definition or Adjustment of Automated Remediation**

* Cloud operator identifies pattern causing requirement for manual remediation
* Cloud operator easily programs known resolution into resolving system
* Cloud operator no longer has to handle manual remediation for that identified
  pattern

Related User Stories
++++++++++++++++++++
* `HA VM`

.. _`HA VM`:http://specs.openstack.org/openstack/openstack-user-stories/user-stories/proposed/ha_vm.html

Requirements
++++++++++++
TBD

External References
+++++++++++++++++++
* `OpenStack Watcher Project`_
* `Cloud Minion`_
* `OpenStack Ops Wiki`_

.. _`OpenStack Watcher Project`: https://wiki.openstack.org/wiki/Watcher
.. _`Cloud Minion`: http://github.com/paypal/cloudminion
.. _`OpenStack Ops Wiki`: https://wiki.openstack.org/wiki/Osops

Rejected User Stories / Usage Scenarios
---------------------------------------
None.

Glossary
--------
* **Virtual Resource** - Resources managed by OpenStack projects (vCPU,
  IP addresses, container bays, networks, ports, vms, images, etc)

* **Physical Resource** -Resources managed by deployment and operations tools
  (hosts, firewalls, load balancers, switches, etc)

* **Automated Remediation** - Actions taken on physical and virtual resources
  including upgrading openstack services, live migrating virtual machines and
  patching hosts. These actions are triggered automatically as opposed to
  manual remediation where an operator is involved in each occurrence.

* **Cloud Operator** - Cloud-wide operator responsible for maintaining
  availability of infrastructure services. This aligns with the "`Cloud Ops <https://wiki.openstack.org/wiki/OpenStack_Personas_2015_Cloud_Ops>`_"
  persona as defined by the OpenStack UX team.

* **RCA** - Root Cause Analysis
