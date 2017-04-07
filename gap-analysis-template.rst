.. This template should be in ReSTructured text. Please do not delete any of
.. the sections in this template.  If you have nothing to say for a whole
.. section, just write: None.  For help with syntax, see
.. http://sphinx-doc.org/rest.html You can also use an online RST editor at
.. rst.ninjs.org to generate proper RST.


<Title of the Development Proposal> Gap and Overlap Analysis
============================================================
.. Provide a link to the approved Development Proposal that this
.. gap and overlay analysis is referring to.
.. URL to the Development Proposal is mandatory.

`Development Proposal - <url>`

Primary contact
---------------
.. Please use it to list the primary contacts for the gap and overlap analysis.
.. e.g. Name (Company, IRC: <irc_handle>)

Name (Company, IRC: <irc_handle>)

Gap analysis
------------
.. This section is mandatory.
.. Use this section to list and describe the gaps and
.. identify related bugs, blueprints and specs in OpenStack.
.. For each use case and requirement of your Development Proposal,
.. there should be a description of the identified gap and, if available,
.. links to related activities / documents / patches.

.. Please for each gap, if possible, clearly refer to the corresponding use
.. case or requirement in the Development Proposal.

.. You can create sub-sections to structure the gap analysis,
.. e.g. distinguish between gaps on the "problem overview", gaps
.. on the "user cases", or gaps on the "requirements" of your
.. Development Proposal. In particular, you may want to make use of
.. sub-sections if the gap analysis contains a long lists of gaps.

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

Mandatory section. See rst comment in this doc.


Appendix
--------
.. This section is optional.
