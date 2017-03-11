.. This template should be in ReSTructured text. Please do not delete any of
.. the sections in this template.  If you have nothing to say for a whole
.. section, just write: None.  For help with syntax, see
.. http://sphinx-doc.org/rest.html You can also use an online RST editor at
.. rst.ninjs.org to generate proper RST.


DB Hygiene Gap and Overlap Analysis
==================================================
**Sections in** *italics* **are optional.**

.. Provide a link to the approved User Story that this gap and overlay analysis
.. is referring to. URL to the User Story is mandatory.

'Database Cleanup of Deleted Object'`

.. _Database Cleanup of Deleted Object: http://specs.openstack.org/openstack/openstack-user-stories/user-stories/proposed/db-hygiene.html

*Primary contact*
-----------------

.. This section is optional.
.. Please use it to list the primary contacts for the gap and overlap analysis.
.. e.g. Name (Company, IRC: Name)

* Arkady Kanevsky (Dell EMC, IRC: arkady-kanevsky)

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

.. **EXAMPLE 1**:

.. * BMT001 Network Isolation:

..  Networks for one tenant is isolated from other tenants. Network Isolation
..  consists of “Network flipping” and “Network switch port configuration”.
..  The former is implemented in Ironic, and the latter as Neutron ML2 driver.

..  * Network Flipping:

..   * Ironic uses a “deployment network” while deploying a bare metal and
..     switches it to a “tenant network” after the deployment is done.

..    * [bug] [Ironic] Ironic Neutron ML2 Integration
..      `<https://bugs.launchpad.net/ironic/+bug/1526403>`_
..    * [spec] [Ironic] Update of the Ironic Neutron Integration spec
..      `<https://review.openstack.org/#/c/188528/>`_
..    * [blueprint] [Nova] Tenant networking support for Ironic driver
..      `<https://blueprints.launchpad.net/nova/+spec/ironic-networks-support>`_

..  * Network Switch Port Configuration:

..   * A Neutron ML2 driver configures VLAN setting on the network switch ports
..     to realize multi-tenancy on bare metal deployment.
..   * When will a network switch be able to be configured by a ML2 driver really
..     depends on switch vendors, and there’s no blueprint nor spec for it.


.. **EXAMPLE 2**

.. * CRM001 As Wei, I want to be able to query/update/terminate a RUR
..   at any point in time.

..  * Description: Blazar allows only start/end time of RUR to be updated.

..   * [blueprint] [Blazar] Update reserved resource capacity
..     `<https://blueprints.launchpad.net/blazar/+spec/update-reserved-capacity>`_

This section utilizes the `OpenStack UX Personas`_.

* DBH001 As `Rey the Cloud Operator`_, I need an ability to remove records of
  deleted objects from the database after storing those records for audit purposes.

  * a. As an Operator I need an ability to archieve records of deleted objects from
       all projects databases  into persistent and unmutable storage

    * This has been discussed in Nova only but was not implemented. Need to be done
      across all projects.

         * [Nova] [blueprint] Database Archival Framework
            https://blueprints.launchpad.net/nova/+spec/archival-framework

    * TBD

* DBH002 As `Adrian the infrastructure architect`_, I need to be able to re-run the same tests
  (with same objects) in a repeatable manner so that I can have a high certainty
  in the outcome of my proof of concept and cloud functionality.

  * a. As an developer or tester I need an ability to delete specific records
       of deleted objects from any project databases if they are soft deleted.

    * TBD

* As Rey, I need only the appropriate records in my
  database so that I can complete my upgrade in the allocated down time.

  * a. As an Operator I need an ability to delete records of deleted objects from
       all projects databases

   * This has been approved by Cinder

    * [Cinder] [blueprint] Cleanup work with DB in Cinder
         https://blueprints.launchpad.net/cinder/+spec/db-cleanup

    * This have been discussed but abandonen for Nova since they removed soft delete
      option.

       * [Nova] [blueprint] Purge Soft Deleted Raw
         https://blueprints.launchpad.net/nova/+spec/purge-soft-deleted-rows

    * TBD

  * b. As an operator I need an ability to specify if records of deleted objects
       should be deleted or soft deleted for all projects

    * Nova team decided to remove soft delete option for operators and it has been
      implemented.

       * [Nova] [blueprint] Remove SoftDeleteMixin option
         https://blueprints.launchpad.net/nova/+spec/no-more-soft-delete

    * TBD

.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html
.. _Adrian the infrastructure architect: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/infrastructure-arch.html
.. _Rey the cloud operator: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/cloud-ops.html


Appendix
------------

.. This section is optional.
