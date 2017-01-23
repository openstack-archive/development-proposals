Provide Config for External FW Appliance
========================================

Cross Project Spec - None

User Story Tracker - None

Problem Description
-------------------

Problem Definition
++++++++++++++++++
As a deployer of an OpenStack cloud I have to provide a specific network
configuration file to my network security team in order to enable appropriate
traffic to my cloud. At the moment I have to cobble together this configuration
from my deployment configuration. It would be much easier to programmatically
generate the bulk of this information as part of the deployment process or from
an available OpenStack service on demand.

Opportunity/Justification
+++++++++++++++++++++++++
None.

Requirements Specification
--------------------------

Use Cases
+++++++++
This section utilizes the `OpenStack UX Personas`_.

* As `Rey the Cloud Operator`_, I want to be able to access a configuration description that I
  can provide to my network security team to properly configure any external
  firewalls so that my users can quickly begin accessing the cloud.
* As the network security team for Rey, I want to be able to easily
  consume the firewall configuration provided in a standard format, so that I
  have minimal effort required to appropriately configure the firewall

.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html
.. _Rey the Cloud Operator: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/cloud-ops.html#cloud-ops

Usage Scenarios Examples
++++++++++++++++++++++++
1. Initial Cloud Deployment
	a. Deploy cloud using deployment configuration
	b. Access templated firewall configuration from OpenStack service
	c. Provide configuration to internal network security team
	d. Network security team easily interprets configuration and configures FW

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
