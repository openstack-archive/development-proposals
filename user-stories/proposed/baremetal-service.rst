Bare Metal Service
==================

Cross Project Spec - None

User Story Tracker - None

Problem description
====================

*Problem Definition*
--------------------

For a specific Enterprise industry, the company needs to support Enterprise
business requirements. Such requirements requires to provision baremetal
machines in multi-tenant model, and intergrate with storage service.
The administrator also requires a Console to integrate with existing Horizon
UI. In order to support this use case, we need:

#. Network Isolation: Multiple virtual networks can be created by each tenant.

#. Storage Service Integration: Baremetal machine can be connected with block
   device service such as Cinder. Tenant can also back up internal storage of
   baremetal machine.

#. Console: Tenant can operate baremetal machine from console integrated with
   existing Horizon UI.

Opportunity/Justification
-------------------------

Cloud service provider wants to support bare metal machine, but they are in
dilemma about not providing bare metal with elastic as the same as providing
virtual machine.

Use Cases
=========

User Stories
------------

* As an Enterprise user, I want to use bare metal machine so that I get
  inconsistent performance not affected by another machine.

* As an Enterprise user, I want to create networks elastically so that I can
  use network like I have these networks not affected by other companies.

* As a operator, I want to back up internal disk of bare metal machine.

* As an Enterprise user, I want to use bare metal machine integrated with
  block storage service so that I can use external storage service.

* As a operator, I want to operate baremetal mechine from console so that I
  can analyze problems at booting time and so on.

Usage Scenario Examples
------------------------

TBD.


Related User Stories
====================

None.

*Requirements*
==============

None.

*External References*
=====================

None.

*Rejected User Stories / Usage Scenarios*
=========================================

None.

Glossary
========

TBD.