Containerized OpenStack Management: Non Destructive OpenStack Lifecycle Management
===================

Cross Project Spec - None

User Story Tracker - None

Problem Description
-------------------

Problem Definition
++++++++++++++++++
When operating OpenStack based Cloud Services, especially based on a stable
version, it is often important to apply patches to running OpenStack
Environment.

Since OpenStack Community is doing great job back-porting
important enhancements and fixes into stable branch, it is critical for an
operator to apply those patches into running OpenStack production environment
so that its OpenStack can continuously run a stable version.
In addition, most of patches does not require the entire OpenStack services to
be updated. An operator wants to apply a patch only to relevant part of
OpenStack not touch other parts of OpenStack at all. Having said that, finding
a way to only update/change necessary process(es) on running OpenStack is
critical for an operator to keep its OpenStack production environment healthy
and safe.

In many cases, automation can provide update/upgrade capability for OpenStack.
However, it is difficult to find a capability from the existing automation
tool to provide "rollback" capability, especially per service. Although
Operators go through many sets of tests on stage environment before applying
any changes in production environment, there has always been unexpected
failures/errors when applying it to production environment due to various
environmental dependencies. In this sense, having rollback capability per
service can be a very helpful tool for operators to have.

Opportunity/Justification
+++++++++++++++++++++++++
Operating a production Openstack cloud in an efficient and scalable way is
critical for an organization to achieve the cost benefits and promise that a
private cloud strategy entails. For non-production and new operators a bare
metal - few servers type installation is sufficient and tearing down and
rebuilding the configuration is a normal course of business. However for
larger installations with high availability expectations that approach results
in too much work and at times an insurmountable barrier to keeping the cloud
current and usable by the cloud users.

Requirements Specification
--------------------------

Use Cases
+++++++++
This section utilizes the `OpenStack UX Personas`_.

* As `Rey the Cloud Operator`_, I want to easily deploy openstack without any
  deep knowledge about openstack itself and without any specific environmental
  dependencies on various deployment site so that I can have a single and
  unified way to quickly deploy openstack on various deployment site.
* As Rey after successful OpenStack deployment, I want to easily manage
  various types of OpenStack processes by recognizing each of them as part of
  discrete, versioned service components so that unrelated dependencies do not
  restrict my ability to upgrade or downgrade components to meet operational
  needs.
* As Rey after successful OpenStack deployment, I want to have a single
  unified method for managing the deployment lifecycle of OpenStack component
  services so that I do not have to manage multiple automation and
  availability supervisor tools in the course of deploying components to meet
  operational needs.
* As Rey after successful OpenStack deployment, I want to easily rollback when
  newly applied patches/updates cause problem on the running openstack service
  so that I can minimize possible service interruption when problem occurs
  with applied changes.
* As Rey after successful OpenStack deployment, I want to easily & safely
  upgrade running openstack.  Apply an update/upgrade to only necessary part
  of openstack without service downtime, so that I can run my openstack
  environment as stable as possible with all the recent patches and newly
  added features.

.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html
.. _Rey the Cloud Operator: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/cloud-ops.html#cloud-ops

Usage Scenarios Examples
++++++++++++++++++++++++
Scenario 1:
  1. A critical security patch is made available for Keystone with imminent
     damage / leak of information possible
  2. Operations team identifies numerous clouds (instances of openstack) which
     need to be patched
  3. Operations team updates the instance of record with the patched Keystone
  4. Operations team implements patch deployment routine which systemically
     brings down and replace all instances of keystone with the new

Scenario 2:
  1. Operations team is notified that a third-party actor was dependent on
     pre-upgrade behavior of a recently upgraded Keystone.
  2. A decision is made to immediately revert the Keystone version until a
     solution is found.
  3. Operations team update the required Keystone version in the deployment
     record for the affected cloud to the prior version
  4. Deployment platform replaces running Keystone instances with prior version.
  5. Operations team verifies that services is restored to third party actor.

Acceptance Criteria
+++++++++++++++++++
* Successful completion of this story would provide a coordinated set of
  projects to implement the functionality to run and upgrade OpenStack in a
  native containers
* A stable OpenStack deployment can be described in terms of version or build
  artifact references of all of the required service components, such that
  OpenStack can be deployed by supplying these component details to a deployment
  orchestration platform.
* A running OpenStack deployment can have individual components replaced with
  different versions by supplying component/artifact version details to a
  deployment orchestration platform

Related User Stories
++++++++++++++++++++
* `Rolling Upgrades <https://github.com/openstack/openstack-user-stories/blob/master/user-stories/proposed/rolling-upgrades.rst>`_
  Issue: The above User Story covers almost "everything" you need to have for
  "update/upgrade without downtime". That means, this story will have some level of overap with 'Rolling Upgrades" stroy.
* `Cloud Native <https://github.com/openstack/openstack-user-stories/blob/master/user-stories/proposed/cloud-native.rst>`_
  Issue: Cloud Native can be one of the architectural patterns to achieve this story.

Requirements
++++++++++++
None.

External References
+++++++++++++++++++
* `Kolla <https://wiki.openstack.org/wiki/Kolla>`_
* `openstack-helm <https://launchpad.net/openstack-helm>`_
* `OpenStack-Ansible <https://docs.openstack.org/developer/openstack-ansible/mitaka/install-guide/>`_

Rejected User Stories / Usage Scenarios
---------------------------------------
None.

Glossary
--------
None.

