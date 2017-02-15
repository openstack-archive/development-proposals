Capacity Management Gap and Overlap Analysis
============================================
**Sections in** *italics* **are optional.**

.. Provide a link to the approved User Story that this gap and overlay analysis
.. is referring to. URL to the User Story is mandatory.

`Quotas, Usage Plans, and Capacity Management`_

.. _Quotas, Usage Plans, and Capacity Management: http://specs.openstack.org/openstack/openstack-user-stories/user-stories/proposed/capacity_management.html


Primary contact
---------------

.. This section is optional.
.. Please use it to list the primary contacts for the gap and overlap analysis.
.. e.g. Name (Company, IRC: Name)

* Hiroaki Kobayashi (NTT, IRC: hiro-kobayashi),
* Bertrand Souville (DOCOMO Euro-Labs, IRC: bertys)
* Masahito Muroi (NTT, Blazar PTL, IRC: masahito)


Gap analysis
------------

.. This section is mandatory.
.. Use this section to list and describe the gaps and
.. identify related bugs, blueprints and specs in OpenStack.
.. For each use case and requirement of your user story there should be a
.. description of the identified gap and, if available, links to related
.. activities / documents / patches.

.. Please for each gap, if possible, clearly refer to the corresponding use
.. case or requirement in the user story.

.. You can create sub-sections to structure the gap analysis,
.. e.g. distinguish between gaps on the "problem definition", gaps
.. on the "user cases", or gaps on the "requirements" of your user story.
.. In particular, you may want to make use of sub-sections if the gap analysis
.. contains a long lists of gaps.

.. Please see existing gap analysis for examples.

.. Ideally, use below or a similar format for the gap analysis:

.. * XXX### Name of the gap - alternatively repeat the (use case) text this gap
..   refers to
..   Note: provide an identifier (three character reference and three digit
..   number for each gap that can be used to uniquely refer to the gap)

..  * Detailed description of the gap (may span multiple bullet points)
..    Ideally, refer to the related use case or requirement.
..  * You can also divide big gaps into smaller sub-gaps.

..   * (optional) If there are related bugs, blueprints and specs, please
..     list all of them in the following format including a reference/link:
..     [<Type>] [<project>] <Title> `<reference>`_

.. Note: the following gap analysis do not cover ALL of user stories of
.. capacity management user story. They are expected to be added in the future.

* *[TBD]* CRM001 As `Wei the project owner of a Telco operator`_, I want to
  specify my resource usage request (RUR) in a way that will enable automated
  processing by the CSP, so that my RUR will be handled more quickly and
  accurately.

* *[TBD]* CRM002 As `Adrian the infrastructure architect`_, I want to be able to
  automate the processing of RURs so that I can meet my user SLAs and gain more
  timely and accurate data input to my capacity management and planning systems.

* CRM003 As Wei, I want to be able to describe the temporal characteristics of
  my RUR, so that the CSP can plan capacity more accurately and reduce the
  chances of a resource request failure. My CSP may also offer me better pricing
  for more accurate usage prediction. Some examples of time-based RURs:

  * a. I plan to use up to 60 vCPUs and 240 GB of RAM from 6/1/2018 to
    8/14/2018.

    * Similar operations are supported by Blazar. CPU specification, memory
      capacity, and storage capacity of a host, the min/max number of hosts,
      and start/end time of resource usage can be specified with RUR for Blazar
      host reservation feature.

  * b. I plan to use 200GB of object storage starting on 8/14/2016, increasing
    by 100GB every calendar month thereafter.

    * A Possible way to reserve object storage capacity in current OpenStack is
      preparing project's private HDD/SSD and creating 'storage policies' for
      using the disks, then associating it to the project. However, there is no
      way for the object storage to be increased by 100GB every calendar month
      thereafter.

      * http://docs.openstack.org/developer/swift/overview_policies.html

  * c. I want guaranteed access to 30 vCPUs and 200GB of RAM for my project.
    In addition, during October-December, I want to be able to increase my
    usage to 150 vCPUs and 1TB of RAM.

    * Blazar guarantees access for the requested resource if there is enough
      capacity at the time of RUR.
    * It is not possible to increase resource capacity.

      * [blueprint] [Blazar] Update reserved resource capacity
        https://blueprints.launchpad.net/blazar/+spec/update-reserved-capacity

  * d. I want guaranteed access to 4 instances with 1 vCPU and 1GB of RAM and
    10GB of disk and a guaranteed minimum bandwidth of 1Gbps between the
    instances. This example is similar to what would be described in the VNFD.

    * A instance reservation feature used to be supported by Blazar. However,
      it is not available in current release because it depends on Nova API
      extensions - v2 of which was deprecated in Liberty and the API extension
      itself was completely removed in Ocata. Alternatively, There is a new
      instance reservatin blueprint in Blazar.

      * [spec] [Nova] Support nested resource providers
        https://blueprints.launchpad.net/nova/+spec/nested-resource-providers
      * [spec] [Nova] Remove support for API extensions
        https://specs.openstack.org/openstack/nova-specs/specs/newton/implemented/api-no-more-extensions.html
      * [blueprint] [Blazar] Get the instance reservation feature back
	https://blueprints.launchpad.net/blazar/+spec/new-instance-reservation

    * Network bandwidth between instances cannot be guaranteed for now.

      * [bug] [Neutron] Minimum bandwidth support (egress)
        https://bugs.launchpad.net/neutron/+bug/1560963
      * [bug] [Neutron] Strict minimum bandwidth support (egress)
        https://bugs.launchpad.net/neutron/+bug/1578989
      * [blueprint] [Blazar] Implement Basic network plugin for network
        resources management
        https://blueprints.launchpad.net/blazar/+spec/basic-network-plugin

* *[TBD]* CRM004 As Wei, I want to be able to submit an updated version of a
  rolling RUR for my project every month, so that my CSP has accurate
  information and can give me the best price and SLA.

* *[TBD]* CRM005 As Wei, I want to be able to take advantage of pricing and
  other offers from my CSP in order to meet the business objectives for my
  project. For example:

  a. I want 60 vCPUs for a minimum of one hour. After that time, the CSP may
     shut down all my instances if the resources are needed elsewhere. (I assume
     that the price is lower on such instances.)
  b. I want up to 100 vCPUs for the next 24 hours. Tell me how many I can have.

* *[TBD]* CRM006 As Adrian, I want to be able to automate the construction and
  interpretation of a time-based resource usage plan so that I can schedule the
  most cost-effective actions to maintain my SLA. Some examples of actions:

  a. Schedule the provisioning of additional infrastructure.
  b. Repurpose existing allocated infrastructure.
  c. Assign a new project to one of a number of regions based on usage
     projections.
  d. Add “burst capacity” from a federation partner or reseller.
  e. Modify or defer another project.

* CRM007 As Wei, I want to be able to query/update/terminate a RUR at any point
  in time.

  * Blazar allows RUR to be queried at any point of time.
  * Blazar allows only start/end time of RUR to be updated for now

    * [blueprint] [Blazar] Update reserved resource capacity
      https://blueprints.launchpad.net/blazar/+spec/update-reserved-capacity

  * Blazar does not allow RUR to be terminated on demand after start time of the
    RUR.

    * [blueprint] [Blazar] Terminate lease at any time
      https://blueprints.launchpad.net/blazar/+spec/terminate-lease-at-anytime


* CRM008 As Wei, I want to receive an appropriate error message in case the a
  RUR is not successful. In case of a failure of RUR I want the environment to
  be reverted back to pre-RUR state.
  In other words, RUR transaction should be Atomic. In case of RUR failure, the
  error message should contain sufficient information such that user can take
  actions to modify the RUR.

  * Blazar plans to support atomic transactions.

    * [blueprint] [Blazar] Support atomic transactions
      https://blueprints.launchpad.net/blazar/+spec/atomic-transaction

  * In case of a failure of RUR, information about the cause of error is
    contained in the response messages from Blazar.
