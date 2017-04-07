Scheduler Simulator
===================

Cross Project Spec - None

User Story Tracker - None

Problem Description
-------------------

Problem Definition
++++++++++++++++++
Cloud Operators are often confronted with the need to perform what if scenarios
on proposed compute and block storage schedulers tweaks. As such they often
want to have access to a scheduler simulator, to make a series of "virtual"
requests given a specific scheduler configuration to see if the resulting
virtual machine load matches their expected or desired outcome.

Opportunity/Justification
+++++++++++++++++++++++++
This user story is valuable to cloud operators because it allows them to tune
the scheduler without having to run the configurations in real world
environments.

Requirements Specification
--------------------------

Use Cases
+++++++++
This section utilizes the `OpenStack UX Personas`_.

* As `Rey the Cloud Operator`_, I want to be able to simulate my cloud's scheduler with
  a variety of virtual machine request loads under a given scheduler
  configuration in order to determine the optimal configuration for my desired
  outcome
* As Rey, I want to be able to visualize the simulated scheduling
  of virtual machines onto hosts in my environment so that I can quickly
  realize whether a given configuration will result in my desired outcome

.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html
.. _Rey the Cloud Operator: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/cloud-ops.html#cloud-ops

Usage Scenarios Examples
++++++++++++++++++++++++
1. Operator Runs Simulator
	a. Operator defines scheduler configuration
	b. Operator defines request load
	c. Simulator places load on "virtual" cloud given configuration
	d. Simulator provides results of that placement
	e. Simulator provides visual output of placement
	f. Operator determines if result is optimal and if not adjusts configuration

Related User Stories
++++++++++++++++++++
None.

Requirements
++++++++++++
None.

External References
+++++++++++++++++++
None.

Rejected User Stories / Usage Scenarios
---------------------------------------
None.

Glossary
--------
None.
