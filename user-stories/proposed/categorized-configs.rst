Categorized Configuration
=========================

Cross Project Spec - https://review.openstack.org/#/c/295543 (WIP)

User Story Tracker - None

Problem description
-------------------

Problem Definition
++++++++++++++++++

Operators currently have to grapple with hundreds of configuration options
across tens of OpenStack services across multiple projects. In many cases
they also need to be aware of the relationships between the options.
In particular, this makes the initial deployment a very daunting task.

Opportunity/Justification
+++++++++++++++++++++++++

One of the largest barriers to adoption of OpenStack is perceived complexity.
This surfaces in attempting to understand and properly set configurations
on initial deployment, and again after upgrading.

Requirements Specification
--------------------------

Use Cases
+++++++++
This section utilizes the `OpenStack UX Personas`_.

* As `Rey the Cloud Operator`_, I should be able to understand how to use a configuration
  option by reading the documentation. There should be no need to read the
  code to understand what value to choose.
* As Rey doing an initial deployment, I want most options to have
  a useful default value, so they do not need to be considered or specified
  during the initial configuration of the system.
* As Rey doing an initial deployment, I should be able to quickly
  identify what configurations I must consider, and how I should determine
  their value for my deployment to be successful.
* As a Packager, I should be able to quickly identify what configuration
  options the packaging must set, and what options the operator needs to
  specify.
* As Rey scaling out a deployment, there should be minimal
  configuration changes required. For the small number of options that must
  be changed, it should be clear what values require tuning, what symptoms are
  caused by incorrect values and how to determine correct values.
* As Rey, the documentation should be clear on the relationship
  between configuration options. For example, if you select driver A by
  setting configuration option X, it should be clear what values should be
  set for any dependent configuration options within the same project.
* There may be some options that are very unlikely to be used, except by the
  most advanced users. By default, these advanced options should be marked as
  such and presented in such a way as to make the documentation less daunting.
  While remaining discoverable it's possible such options may require Rey to
  review additional documentation to fully understand their impact.
* As Rey doing an initial configuration, it should be easy to check
  that you have a valid configuration file. Checking for any unrecognized
  configuration options and any invalid values can help find typos.
* As Rey that has just completed an upgrade, it should be easy to
  check if you are making use of any deprecated configuration options, and
  determine what changes must be made before doing your next upgrade.

.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html
.. _Rey the Cloud Operator: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/cloud-ops.html#cloud-ops

Usage Scenario Examples
+++++++++++++++++++++++

1. Initial Configuration and Deployment

  a. Deployer reviews centralized config documentation for services selected
     for deployment
  #. Deployer quickly finds the configurations that need setting prior to
     deployment
  #. Deployer makes adjustments to configs and deploys, leaving most configs
     unset, for example, using their default values
  #. Deployment is performed successfully

2. Scaling Re-Configuration

  a. Deployer reviews centralized configuration documentation for services
     selected for scaling
  #. Deployer uses documentation to determine new configuration settings
     required for optimal performance at their future scale
  #. Deployer makes appropriate adjustments to configuration
  #. Deployer scales deployment successfully

3. Scaling Troubleshooting

  a. Deployer scales deployment and begins experiencing performance degradation
     with a specific service
  #. Deployer consults configuration documentation to determine if symptoms are
     caused by mis-configuration
  #. Deployer identifies configuration adjustment required
  #. Deployer makes required configuration adjustments
  #. Deployer successfully returns deployment to optimal performance

Related User Stories
++++++++++++++++++++

None.

Requirements
++++++++++++

None.

External References
+++++++++++++++++++

* `Nova - Centralize Config Options Spec <http://specs.openstack.org/openstack/nova-specs/specs/mitaka/approved/centralize-config-options.html>`_
* `Nova - Centralize Config Options Blueprint - Newton <https://blueprints.launchpad.net/nova/+spec/centralize-config-options-newton>`_
* `Oslo Config Generator <http://docs.openstack.org/developer/oslo.config/generator.html>`_
* `Nova - Sample Configuration <http://docs.openstack.org/developer/nova/sample_config.html>`_

Rejected User Stories / Usage Scenarios
---------------------------------------

None.

Glossary
--------

None.
