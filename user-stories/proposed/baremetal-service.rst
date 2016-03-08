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
machines in multi-tenant model, and integrate with storage service.
The administrator also requires a Console to integrate with existing Horizon
UI. In order to support this use case, we need:

#. Network Isolation: Multiple virtual networks can be created by each tenant.

#. Storage Service Integration: Baremetal machine can be connected with block
   device service such as Cinder. Tenant can also back up internal storage of
   baremetal machine.

#. Console: Tenant can operate baremetal machine from console integrated with
   existing Horizon UI.

#. Unified VM/BM Management: Unified management of both VMs and BMs (Bare
   metal machines) by software with the same set of services can be provided
   to users.

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
  consistent performance not affected by another machine.

* As an enterprise user, I want to have a secure and clean bare metal
  deployed no matter who used it before.

* As an Enterprise user, I want to create networks elastically so that I can
  use network like I have these networks not affected by other companies.

* As an operator, I want to back up internal disk of bare metal machine.

* As an Enterprise user, I want to use bare metal machine integrated with
  block storage service so that I can use external storage service.

* As an operator, I want to operate baremetal machine from console so that I
  can analyze problems at booting time and so on.

* As an enterprise user, I want to continue my operation immediately when
  a bare metal fails without any manual operations such as switchover.

* As an enterprise user, I want to use a bare metal with the network
  services such as FWaaS, LBaaS, Security Group, VPNaaS, virtual routers
  in the same manner of VMs.

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