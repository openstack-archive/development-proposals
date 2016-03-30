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
developers. Rackspace has developed its own tools for use in the Rackspace
Public Cloud, and is actively considering open-sourcing parts of it. The new
Watcher project within OpenStack is also an attempt to address some aspects of
this problem.

Use Cases
=========

User Stories
------------
* As the sys admin I need to monitor status of resources in my OpenStack cloud
  - compute, network, and storage nodes, and their capabilities

* As a Public Cloud operator I have to be ably to comply with Government
  orders/investigations. This may require that I quarantine a VM (and
  associated resources) or that I make a VM (and associated resources)
  available to investigators for digital forensics.

Usage Scenario Examples
------------------------
TBD

Related User Stories
====================
* Life cycle management for Storage (does not exist yet)
* DB Hygiene (does not exist yet)

Requirements
==============
TBD

External References
=====================
None.

Rejected User Stories / Usage Scenarios
=======================================
None.

Glossary
========
.. Examples:
.. **reST** reStructuredText is a simple markup language
.. **TLA** Three-Letter Abbreviation is an abbreviation consisting of three letters
.. **xyz** Another example abbreviation
