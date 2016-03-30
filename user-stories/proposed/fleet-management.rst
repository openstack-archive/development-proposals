Fleet Management
================
Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

Problem Definition
++++++++++++++++++
While there are many open-source toolsets for initial deployment of OpenStack
(Day 1), there is a need for tools to help operators manage the environment
once it is set up (Day 2 and beyond).

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

User Stories
++++++++++++
* As a cloud operator, I need to monitor status of physical resources in my
  OpenStack cloud - compute, network, and storage nodes utilization, and
  factors like power, temperature, CPU and memory on each node - so that I may
  optimize usage of those resources and maintain the health of my cloud

* As a cloud operator, I need to monitor the health of my physical resources
  so that I can take automatic policy-driven remedial action and deliver on my
  SLAs

* As a cloud operator, I need to keep track of unused virtual resource capacity
  so that I can free up virtual resources and use them more efficiently

* As a cloud operator, I need to keep track of alerts and messages, so that I
  can take remedial action and keep my cloud resources in compliance

* As a cloud operator, I need to check my deployed physical resources against a
  set of policies and rules, so that I can meet security, availability and
  other requirements

* As a cloud operator, I need to limit the alerts presented to me to only those
  which require investigation

* As a cloud operator, I need to utilize an automatic remediation system which
  identifies inconsistencies, determines if physical resources are in the
  appropriate state and takes remedial action if they are not

* As a cloud operator, I need to carefully define automated remedial actions on
  physical resources so that they are least disruptive to my end-users

* As a cloud operator, I need to be able to easily define and adjust automated
  remedial actions as a result of my investigations into alerts

* As a cloud operator, I need to apply patches and updates to my physical
  resources, and maintain audit logs, so that I can keep my environment updated
  and secure, and roll back to prior tested configurations when something goes
  wrong with a patch or update

* As a cloud operator, I need to be able to retrieve the current state of my
  hardware resources

Usage Scenario Examples
+++++++++++++++++++++++
**Automated Remediation**

* Monitoring triggers a warning on physical resources
* Auditing system determines physical resource in question is not in
  appropriate state
* Resolving system removes physical resources from production pool
* Resolving system returns physical resources to appropriate state
* Resolving system returns physical resources to production pool

**Operator Notification and Manual Remediation**

* Monitoring triggers a warning on physical resources
* Auditing system determines physical resource in question is in appropriate
  state
* Resolving system removes physical resources from production pool
* Resolving system informs operator of need for investigation, removes
  resources from resolving system management
* Operator investigates and determines cause of issue
* Operator returns resource to resolving system management
* Resolving system returns physical resources to production pool

**Operator Definition or Adjustment of Automated Remediation**

* Operator identifies pattern causing requirement for manual remediation
* Operator easily programs known resolution into resolving system
* Operator no longer has to handle manual remediation for that identified
  pattern

Related User Stories
++++++++++++++++++++
TBD

Requirements
++++++++++++
TBD

External References
+++++++++++++++++++
* `<https://wiki.openstack.org/wiki/Watcher>`_

* `<http://github.com/paypal/cloudminion>`_

* `<https://wiki.openstack.org/wiki/Osops>`_

Rejected User Stories / Usage Scenarios
---------------------------------------
None.

Glossary
--------
* **Virtual Resource** - Resources managed by OpenStack projects (vCPU,
  IP addresses, container bays, networks, ports, etc)

* **Physical Resource** -Resources managed by deployment and operations tools
  (hosts, firewalls, load balancers, switches, etc)
