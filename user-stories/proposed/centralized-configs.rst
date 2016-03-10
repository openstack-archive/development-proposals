Centralized Configuration
==========================
Cross Project Spec - None

User Story Tracker - None

Problem description
====================

Problem Definition
------------------
Operators often have to grapple with hundreds of configuration options across
tens of OpenStack services across multiple projects. This can be a daunting
task if the configuration files are not simplified, centralized and
understandable within a given project.

Opportunity/Justification
-------------------------
One of the largest barriers to adoption of OpenStack is perceived complexity.
This surfaces both in attempting to understand and properly set configurations
on initial deployment. Centralizing and simplifying the configurable settings
and the initial configuration process for each project would dramatically
simplify deployment for deployers and operators.

Use Cases
=========

User Stories
------------
* As an Operator, I should be able to review one set of configuration files for
  each service in order to make initial configuration simple.
* As an Operator, I should be able to generate a standard set of configuration
  defaults which represents the best-practices for a given project in order to
  speed initial configuration.
* As an Operator, I should be able to quickly identify what configurations will
  require adjustment and how I should determine their value for my deployment
  to be successful in order to speed initial deployment.

Usage Scenario Examples
------------------------
1. Initial Configuration and Deployment

  a. Deployer reviews central configs for services selected for deployment
  b. Deployer quickly finds configurations which require adjustment prior to
     deployment
  c. Deployer makes adjustments and deploys largely with supplied defaults
  d. Deployment is performed successfully

Related User Stories
====================
None.

Requirements
============
None.

External References
===================
* `Nova - Centralize Config Options Spec <http://specs.openstack.org/openstack/nova-specs/specs/mitaka/approved/centralize-config-options.html>`_
* `Nova - Centralize Config Options Blueprint - Newton <https://blueprints.launchpad.net/nova/+spec/centralize-config-options-newton>`_
* `Oslo Config Generator <http://docs.openstack.org/developer/oslo.config/generator.html>`_

Rejected User Stories / Usage Scenarios
=======================================
None.

Glossary
========
None.
