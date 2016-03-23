Enterprise Test Strategy
========================
Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

Problem Definition
++++++++++++++++++
Enterprise users expect a variety of capabilities from their OpenStack clouds.
These include capabilities such as cloud size scalability, cloud usage
scalability and upgradeability. At present some of those capabilities are left
untested, leaving Enterprise evaluators without documented evidence to support
their comparisons to alternatives.

Opportunity/Justification
+++++++++++++++++++++++++
Providing access to reliable test results which validate OpenStack's
capabilities will increase adoption of OpenStack. Lack of information on
the software's ability to perform in large enterprise environments is a barrier
to adoption for enterprises.

Use Cases
---------

User Stories
++++++++++++
* As an Enterprise Evaluator of OpenStack, I expect to be able to review
  credible test results which verify the following:

    * The scalability characteristics of OpenStack
    * The upgradability characteristics of OpenStack
    * The performance characteristics of OpenStack

  in order to assist in my evaluation against competitive platforms.
* As an OpenStack Developer, I expect to be able to identify scalability,
  upgradeability and performance bottlenecks in order to target improvements
  effectively
* As an OpenStack Operator, I expect to be able to review credible test results
  which verify the scalability, upgradeability and performance characteristics
  of a given OpenStack release in order to justify upgrade or update my
  environment to a newer version.


Usage Scenario Examples
+++++++++++++++++++++++
* Enterprise Evaluator

  #. Evaluator begins evaluation of OpenStack and competitive options
  #. Evaluator is able to obtain credible test results for competitors AND
     OpenStack from their respective companies/communities
  #. Evaluator ensures minimum requirements for scalability, performance and
     upgradeability are met and weighs capability advantages and disadvantages
     between options
  #. Evaluator chooses OpenStack and begins a starter deployment.

* OpenStack Operator

  #. Operator considers upgrading their OpenStack deployment to the newest
     major version
  #. Operator consults OpenStack documentation for capability comparisons
     between their current version and the newest major version
  #. Due to verifiable performance improvements Operator moves forward with
     upgrade

* OpenStack Developer

  #. Developer wishes to target scalability improvements in the Nova project
  #. Developer consults scalability test results to identify known bottlenecks
  #. Developer works to improve the code and is assured that his improvements
     have a material effect on scalability by reviewing test results after
     his code has merged

Related User Stories
++++++++++++++++++++
None.

Requirements
++++++++++++
TBD

External References
+++++++++++++++++++
TBD

Rejected User Stories / Usage Scenarios
---------------------------------------
None.

Glossary
--------
* **Scalability Characteristics** - Ability for the OpenStack control plane to
  perform as the number of physical resources (nodes) under management grows.
* **Performance Characteristics** - Ability for the OpenStack control plane to
  perform as the number of control plane interactions (resource requests)
  grows.
* **Upgradeability Characteristics** - Ability for the OpenStack control plane
  to upgrade between minor and major releases without causing downtime.
