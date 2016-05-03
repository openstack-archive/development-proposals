================================
Feature Classification Framework
================================
Cross Project Spec - Ready for Submission

User Story Tracker - None

Problem description
-------------------

Problem Definition
++++++++++++++++++
Operators and Users lack centralized visibility into the status of the
completeness, stability and documentation of features. They also lack knowledge
of the effects of configuration decisions on these features and their
classification. This prevents Operators from making optimal decisions when
configuring their clouds and leaves their users unsure of the maturity and
stability of features they might choose to use in their applications and
workloads.

Opportunity/Justification
+++++++++++++++++++++++++
The configuration and use of OpenStack services can be simplified by:

* providing a centralized framework for classifying features, and
* documenting their completeness, maturity and documentation against specific
  configuration sets

Use Cases
---------

User Stories
++++++++++++

* As an Operator, I want to understand what features are complete,
  well-documented and stable so that I can ensure a good experience for my
  user community in recommending features for use.
* As an Operator, I want to understand the effects my configuration choices
  might have on specific feature classifications so that I can make optimal
  decisions when defining my cloud's configuration.
* As a User, I want to understand which features are stable and mature so that
  I choose appropriate features for use in my applications.
* As a User, I want to be able to reference a common set of feature
  classification definitions that span all OpenStack projects so that I don't
  have to understand differing definitions across multiple projects.
* As an OpenStack Developer, I want to understand which features lack
  stability, completeness and documentation so that I can direct my attention
  to improving those deficient features.

Usage Scenario Examples
+++++++++++++++++++++++
**User Feature Selection**

* User begins developing an application which utilizes OpenStack services
* User reviews Feature Classification Definitions to familiarize them self with
  classification terms
* User reviews Feature Classification Framework for available services to
  determine which features are complete and mature enough to be utilized by
  their application
* User selects those features deemed appropriate for use

**Operator Configuration Selection**

* Operator collects requirements for an IaaS platform from user community
* Operator references Feature Classification Definitions to determine minimum
  classification required to support a given feature in their cloud
* Operator references Feature Classification Framework to determine appropriate
  configuration choices for the services they've selected to deploy

**OpenStack Developer Improvement Selection**

* OpenStack Developer reviews Feature Classification Definitions to determine
  deficient classifications they'd like to target (docs, stability,
  completeness).
* OpenStack Developer reviews Feature Classification Framework for their target
  project and identifies deficient features to work on.
* After OpenStack Developer's work is complete they have materially changed the
  classification for their chosen feature and that update is available to other
  developers and users immediately after the change is merged.

**Provider Validates Available Feature Set**

* OpenStack Provider is interested in validating their service has a specific
  feature set available.
* OpenStack Provider develops a third party CI to submit their configuration to
  the Feature Classification Framework.
* OpenStack Provider references the Feature Classification Framework as
  validation to their users that the desired feature set is available and
  stable, complete and well documented.

Related User Stories
++++++++++++++++++++
None.

Requirements
++++++++++++

* Third Party CI Reporting submitted by Configuration
* Initial Mapping of Tempest UUIDs to Features
* Documented "Feature" Definition Across All Projects
* Documented Classification Criteria Across All Projects

Example Matrix
++++++++++++++
Below is an example matrix to illustrate what a Feature Classification Matrix
might look like.

=============================  ===== ===== ===== ===
Feature Classification Matrix     Configurations
-----------------------------  ---------------------
Features                       Conf1 Conf2 Conf3 ...
=============================  ===== ===== ===== ===
Feature 1 (S,M,D)                Y     N     ?    .
Feature 2 (S,M)                  Y     Y     Y    .
=============================  ===== ===== ===== ===

S=Stable, M=Mature, D=Documented

External References
+++++++++++++++++++
* `Nova - Feature Classification <http://docs.openstack.org/developer/nova/feature_classification.html>`_

Rejected User Stories / Usage Scenarios
---------------------------------------
None.

Glossary
--------
None.
