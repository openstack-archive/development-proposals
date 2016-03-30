Fleet Management
================
Cross Project Spec - None

User Story Tracker - None

Problem description
====================

Problem Definition
--------------------
While there are many open-source toolsets for initial deployment of OpenStack
(Day 1), there is a need for tools to help operators manage the environment
once it is set up (Day 2 and beyond)

Today, this gap is filled through proprietary management tools provided either
by OpenStack distributors or third parties or written by the end-users
themselves

The use of these proprietary or bespoke tools and extensions creates either a
dependency and lock-in (if from a vendor) or a continuing maintenance task for
the end-user. In many cases, it also acts as a roadblock for wider adoption of
OpenStack

Opportunity/Justification
-------------------------
Companies like PayPal and eBay have already spoken publicly about their ongoing
efforts in writing and maintaining tools to manage their OpenStack deployments.
They have even started open-sourcing parts of their toolset (see
http://github.com/paypal/cloudminion) to gather support from community
developers. 

Rackspace has developed its own tools for use in the Rackspace
Public Cloud, and is actively considering open-sourcing parts of it, based on requests from its 
Private Cloud customers. The new Watcher project within OpenStack is also an attempt to address 
some aspects of this problem.

Use Cases
=========

User Stories
------------
* As a sys admin I need to monitor status of resources in my OpenStack cloud - compute, network, and
storage nodes utilization, and factors like power, temperature, CPU and memory on each node - so 
that I may optimize usage of those resources and maintain the health of my cloud

* As a cloud operator, I need to monitor the health of my instances, services and tenant workloads 
so that I can take automatic policy-driven remedial action and deliver on my SLAs.

* As a sys admin, I need to keep track of unused VMs and IP addresses so that I can free up 
resources and use them more efficiently

* As a sys admin, I need to monitor the performance of the infrastructure databases, so that I can 
detect potential bottlenecks and take remedial action

* As a sys admin, I need to provision and manage VMs, bare metal servers and containers through a 
common interface, so that I can meet end user needs

* As a sys admin, I need to keep track of alerts and messages, so that I can take remedial action 
and keep my cloud resources in compliance

* As a sys admin, I need to check my deployed resources against a set of policies and rules for 
high availability and security, so that I can take remedial action and stay in compliance

* As a sys admin, I need to apply patches and updates to the services and VMs, and maintain audit 
logs, so that I can keep my environment updated and secure, and roll back to prior tested 
configurations when something goes wrong with a patch or update

Usage Scenario Examples
------------------------
TBD

Related User Stories
====================
* https://wiki.openstack.org/wiki/Watcher 

Requirements
==============
TBD

External References
=====================
* http://github.com/paypal/cloudminion

Rejected User Stories / Usage Scenarios
=======================================
None.

Glossary
========
.. Examples:
.. **reST** reStructuredText is a simple markup language
.. **TLA** Three-Letter Abbreviation is an abbreviation consisting of three letters
.. **xyz** Another example abbreviation
