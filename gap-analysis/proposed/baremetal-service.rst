.. This template should be in ReSTructured text. Please do not delete any of
.. the sections in this template.  If you have nothing to say for a whole
.. section, just write: None.  For help with syntax, see
.. http://sphinx-doc.org/rest.html You can also use an online RST editor at
.. rst.ninjs.org to generate proper RST.


Bare Metal Service Gap and Overlap Analysis
============================================================
.. Provide a link to the approved Development Proposal that this
.. gap and overlay analysis is referring to.
.. URL to the Development Proposal is mandatory.

`Bare Metal Service`_

.. _Bare Metal Service: https://github.com/openstack/openstack-user-stories/blob/master/development-proposals/proposed/baremetal-service.rst
.. TODO: update the above link to specs.opestack.org/openstack/openstack-user-stories <development-proposals> after the repo is changed to "development proposal"

Primary contact
---------------
.. Please use it to list the primary contacts for the gap and overlap analysis.
.. e.g. Name (Company, IRC: <irc_handle>)

* Kei Tokunaga (Fujitsu)
* Yih Leong Sun (Intel, IRC: leong)

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

* Problem Overview

  * **Baremetal machine configuration:** Bare metal machine can be configured with
    CPU specification, memory capacity, local storage drive type such as SATA
    or SSD and its capacity, and network iplink bandwidth. Infiniband or RoCEE
    may be needed to achieve network performance.

    * CPU specification, memory capacity, storage drivetype / capacity, network
      iplink bandwith, and Infiniband / RoCEE can be specified for bare metal
      deployment with using "Capability" property.
 
  * **Network isolation:** Networks for one tenant is isolated from other tenants.
    Network isolation consists of "Network flipping" and "Network switch port
    configuration". The former is implemented in Ironic, and the latter as
    Neutron ML2 driver.

    * Network flipping:

      * Ironic uses a "deployment network" while deploying a bare metal and
        switches it to a "tenant network" after the deployment is done. LAG
        support is also handled in the same RFE/SPEC.

      * This consists of an Ironic and Nova part. Both parts have been
        completed at Newton except for the LAG support. Ironic team is trying
        to merge LAG support at Newton, but it (especially its the Nova part)
        might be slipped to Ocata.

        * [RFE][Ironic] Ironic Neutron ML2 Integration

          https://bugs.launchpad.net/ironic/+bug/1526403


        * [SPEC][Ironic] Update of the Ironic Neutron Integration spec

          https://review.openstack.org/#/c/188528/

        * [BP][Nova] Tenant networking support for Ironic driver 

          https://blueprints.launchpad.net/nova/+spec/ironic-networks-support

        * [SPEC] [Nova] Tenant networking support for Ironic driver

          https://review.openstack.org/#/c/237067

    * Network Switch Port Configuration:

      * A Neutron ML2 driver configures VLAN setting on the network switch
        ports to realize multi-tenancy on bare metal deployment.

      * When will a network switch be able to be configured by a ML2 driver
        really depends on switch vendors, and there's no BP/SPEC for it.

    * Multiple Network For Bare Metal:

      * A bare metal can connect to multiple networks (VLANs) via one
        physical NIC. This is needed to assign a network to each container
        running on a deployed bare metal.

      * This consists of an Ironic and Nova part. Likely be completed at
        Ocata or later.
 
        * [RFE][Ironic] VLAN AwareBaremetal Instances

          https://bugs.launchpad.net/ironic/+bug/1543584

        * [SPEC] [Ironic] VLAN AwareBaremetal Instances

          https://review.openstack.org/#/c/277853

  * **Storage Service Integration:** Bare metal machine can be connected with block
    device service such as Cinder. Bare metal machine connects cinder backends
    dedicated to single tenant. Tenant can also back up internal storage of
    bare metal machine and recover from it.
     
    * SAN:

      * A bare metal can attach a Cinder volume. Likely be able to attach
        Cinder volumes atOcata or later.

    * SAN Boot:

      * A bare metal can boot from a Cinder volume. Likely be able to connect
        to Cinder volumes at Newton (iSCSI, FCoE, and NFS) and at Ocata (FC).
        Multi-tenancy will likely be completed at Ocata or later.

        * [RFE][Ironic] Add volume connection information into ironic db
  
          https://bugs.launchpad.net/ironic/+bug/1526231

        * [SPEC][Ironic] Volume connection information for Ironic nodes

          https://review.openstack.org/#/c/200496/

        * [RFE][Ironic] Boot from Volume - Reference Drivers

          https://bugs.launchpad.net/ironic/+bug/1559691

        * [SPEC][Ironic] Boot from Volume - Reference Drivers

          https://review.openstack.org/#/c/294995/

        * [BP][Nova] Add support for Ironic nodes to boot from Cinder volume

          https://blueprints.launchpad.net/nova/+spec/ironic-boot-from-volume

        * [SPEC][Nova] Add support booting bare metals from Cinder volume

          https://review.openstack.org/#/c/311696/

  * **Console:** Tenant can operate bare metal machine from console, see console
    log integrated with existing Horizon UI.

    * Serial Console:

      * The Ironic part will likely be completed at Newton. The Nova part will
        likely be completed at Ocata.

        * [RFE][Ironic] Nova serial console support for Ironic

          https://bugs.launchpad.net/ironic/+bug/1553083

        * [SPEC][Ironic] Nova compatible serial console support

          https://review.openstack.org/#/c/319505/

        * [BP][Nova] Ironic serialconsole support

          https://blueprints.launchpad.net/nova/+spec/ironic-serial-console-support

    * Graphical Console:

      * Likely to be completed at P-cycle or later.

    * Console Log:

      * Likely to be completed at P-cycle or later.

  * **NMI Injection:** When the OS on a bare metal has a problem (hungup, slow
    down, etc), tenant can issue a NMI to the OS to take a kernel memory dump
    so that they can investigate the root cause of the problem.

    * [BP][Nova] Support softreboot and poweroff in nova ironic driver

      https://blueprints.launchpad.net/nova/+spec/soft-reboot-poweroff

    * [SPEC][Nova] Support soft reboot and poweroff in nova ironic driver

      https://review.openstack.org/#/c/229282/

    * [BP][Nova] Introduce inject NMI interface in nova ironic driver

      https://blueprints.launchpad.net/nova/+spec/inject-nmi-ironic

    * [RFE][Ironic] Enhance Power Interface for Soft Power Off and
      Inject NMI

      https://bugs.launchpad.net/ironic/+bug/1526226

    * [SPEC][Ironic] Enhance Power Interface for Soft Power Off and
      Inject NMI

      https://review.openstack.org/#/c/186700

  * **Graceful Shutdown:** Tenant can gracefully shutdown the OS on a bare metal so
    that they can avoid data corruption that can occur by powering off.

    * See "NMI Injection" for links to BP/SPEC/RFE.

  * **Unified VM/BM Management:** Unified management of both VMs and BMs (bare
    metal machines) by software with the similar set of services or
    functionalities can be provided to users such as FWaaS, LBaaS, VPNaaS,
    Security Group, Block Storage, Backup, High Availability, Connection to VMs
    in virtual network (VXLAN), and Console.

    * FWaaS, LBaaS, VPNaaS: 
   
      * Can be used by Bare Metal today.

    * Security Group:

      * Depends on Neutron ML2 plugins fornetwork switches.
  
      * Work related to Network Isolation on Ironic will likely be completed at
        Ocata.

        * [RFE][Ironic] Security Groups support for baremetal servers

          https://bugs.launchpad.net/ironic/+bug/1594242

    * Block storage and backup:

      * See "Storage Service Integration" above.


    * High Availability:

      * [RFE][Ironic] Bare metal node N+1 redundancy

        https://bugs.launchpad.net/ironic/+bug/1526234

      * [SPEC][Ironic] Bare metal node N+1 redundancy

        https://review.openstack.org/#/c/259320

    * VXLAN:

      * Depends on Neutron ML2 plugins fornetwork switches.

    * Console:

      * See "Console" section above

* User Stories

.. _Wei the project owner: https://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/project-owner.html
..

  * BMT001 - As `Wei the project owner`_, I want to use bare metal machine so
    that I get consistent performance not affected by another machine, nor
    impacted by hypervisor.

    * Bare Metal can be deployed with multi tenancy.

  * BMT002 - As Wei, I want to have a secure and clean bare
    metal machine deployed no matter who used it before.

    * HDD erasing is there already. BIOS reset should depend on Ironic
      drivers for servers.

  * BMT003 - As Wei, I want to create networks elastically so
    that I can use network like I have these networks not affected by other
    companies.

    * See above for development.

  * BMT004 - As Wei, I want to back up internal disk of bare
    metal and create a snapshot. This can be backed up to an external storage
    managed by Cinder.

    * See above for development.

  * BMT005 - As Wei, I want to use bare metal machine integrated
    with block storage service so that I can use external storage service.

    * See above for development.

  * BMT006 - As Wei, I want to see bare metal machine from
    console log and operate from console so that I can analyze problems at
    booting time and so on.

    * See above for development.

  * BMT007 - As Wei, I want to continue my operation immediately
    when a bare metal machine fails without any manual operations such as
    switchover. Similar to HA VM user story, The owner should not have to
    design the fail-over mechanism themselves. The system should monitor and
    detect bare metal machine failure and automatically fail-over to a spare
    bare metal machine.

    * See above for development.

  * BMT008 - As Wei, I want to use a bare metal machine with the
    network services such as FWaaS, LBaaS, Security Group, VPNaaS, and
    connection to VMs in virtual network(VXLAN) in the same manner of VMs.

    * See above for development.

Appendix
--------
.. This section is optional.

* Network Isolation

  * [Ironic] Operator documentation for multitenancy [UNDER DEVELOPMENT]

    https://review.openstack.org/228496

  * [Ironic] Add portgroups to support LAG interfaces - API [UNDER DEVELOPMENT]

    https://review.openstack.org/332177

  * [Ironic] Add classes for Portgroups API enablement [UNDER DEVELOPMENT]

    https://review.openstack.org/347549

  * [Ironic] Add api-ref for new port fields [MERGED]
 
    https://review.openstack.org/325299

  * [Ironic] Follow-up to 317392 [MERGED]

    https://review.openstack.org/342477

  * [Ironic] Expose node's network_interface field in API [MERGED]

    https://review.openstack.org/317392

  * [Ironic] Add multitenancy-related fields to port API object [MERGED]

    https://review.openstack.org/206244

  * [Ironic] Update the deploy drivers with network flipping logic [MERGED]

    https://review.openstack.org/213262

  * [Ironic] Add 'neutron' network interface [MERGED]

    https://review.openstack.org/317393

  * [Ironic] Add network interface to base driver class [MERGED]

    https://review.openstack.org/285852

  * [Ironic] Add internal_info field to ports and portgroups [MERGED]

    https://review.openstack.org/338417

  * [Ironic] Add network_interface node field to DB and object [MERGED]

    https://review.openstack.org/317391

  * [Ironic] Refactor ironic enroll-node code [MERGED]

    https://review.openstack.org/256364

  * [Ironic] Create common neutron module [MERGED]

    https://review.openstack.org/317390

  * [Ironic] Add API reference for portgroups [MERGED]

    https://review.openstack.org/322796

  * [Ironic] Fix API node name updates [MERGED]

    https://review.openstack.org/300983

  * [Ironic] Correct api version check conditional for node.name [MERGED]

    https://review.openstack.org/299264

  * [Ironic] Add portgroups to support LAG interfaces - RPC [MERGED]

    https://review.openstack.org/206243

  * [Ironic] Add portgroups to support LAG interfaces - net [MERGED]

    https://review.openstack.org/206245

  * [Ironic] Add portgroups to support LAG interfaces - objs [MERGED]

    https://review.openstack.org/206238

  * [Ironic] Add portgroups to support LAG interfaces - DB [MERGED]

    https://review.openstack.org/206232

  * [Ironic] devstack 'cleanup-node' script should delete OVS bridges [MERGED]

    https://review.openstack.org/263508

  * [Ironic] Add possibility to work with portgroups [UNDER DEVELOPMENT]

    https://review.openstack.org/335964

  * [Ironic] Updates supporting ironic-neutron integration [MERGED]

    https://review.openstack.org/206144

  * [Nova] Ironic: use portgroups [UNDERDEVELOPMENT]

    https://review.openstack.org/206163

  * [Nova] Ironic: enable multitenant networking [MERGED]

    https://review.openstack.org/297895

  * [Nova] Allow virt driver to define binding:host_id [MERGED]

    https://review.openstack.org/194413

  * [Nova] Adding a new vnic_type for Ironic/Neutron/Nova integration [MERGED]

    https://review.openstack.org/213264

* Storage ServiceIntegration

  * [Ironic] [WIP] Add storage_interface DB field and object [UNDER DEVELOPMENT]

    https://review.openstack.org/348005

  * [Ironic] Introduce new RPCs to support volume target operations [UNDER DEVELOPMENT]

    https://review.openstack.org/285220

  * [Ironic] Introduce VolumeTarget object [UNDER DEVELOPMENT]

    https://review.openstack.org/285219

  * [Ironic] Add volume_targets table to save target information [UNDER DEVELOPMENT]

	https://review.openstack.org/285218

  * [Ironic] Introduce new RPCs to support volume connector operation [UNDER DEVELOPMENT]

    https://review.openstack.org/214585

  * [Ironic] Introduce VolumeConnector object [UNDER DEVELOPMENT]

    https://review.openstack.org/214584

  * [Ironic] Add volume_connector table to save connector information [UNDER DEVELOPMENT]

    https://review.openstack.org/200983

  * [Ironic] Add REST API for volume connector and volume targetoperation [UNDER DEVELOPMENT]

    https://review.openstack.org/214586

  * [Ironic] Add volume_target support [UNDER DEVELOPMENT]

    https://review.openstack.org/285233

  * [Ironic] Add volume_connector support [UNDER DEVELOPMENT]

    https://review.openstack.org/214786

  * [Ironic] Add REST API for volume target operation [UNDER DEVELOPMENT]

    https://review.openstack.org/285221

* Console

  * [Ironic] Add node serial console installation howto [UNDER DEVELOPMENT]

    https://review.openstack.org/293872

  * [Ironic] IPMITool: add IPMISocatConsole and IPMIConsole class [MERGED]

    https://review.openstack.org/293873

  * [Ironic] Nova-compatible serial console: socat console_utils [MERGED]

    https://review.openstack.org/328168

  * [Nova] Ironic Driver: override get_serial_console() [UNDER DEVELOPMENT]

    https://review.openstack.org/328157

* NMI Injection / GracefulShutdown

  * [Ironic] Ipmitool power driver for soft reboot and soft power off [UNDER DEVELOPMENT]

    https://review.openstack.org/216738

  * [Ironic] Generic power I/F for soft reboot and soft power off [UNDER DEVELOPMENT]

    https://review.openstack.org/216730

  * [Ironic] iRMC power driver for soft reboot and soft power off [UNDER DEVELOPMENT]

    https://review.openstack.org/216743

  * [Ironic] iRMC management driver for Inject NMI [UNDER DEVELOPMENT]

    https://review.openstack.org/348732

  * [Ironic] Ipmitool management driver for Inject NMI [UNDER DEVELOPMENT]

    https://review.openstack.org/348721

  * [Ironic] Generic management I/F for Inject NMI [UNDER DEVELOPMENT]

    https://review.openstack.org/348191

  * [Ironic] Overrides get_supported_power_states() for WOL Power [UNDER DEVELOPMENT]

    https://review.openstack.org/293293

  * [Ironic] Add soft reboot/poweroff power states [UNDER DEVELOPMENT]

    https://review.openstack.org/247904

  * [Ironic] Add a new command "ironic node-inject-nmi" [UNDER DEVELOPMENT]

    https://review.openstack.org/247905/

  * [Nova] Add soft power off support to ironic driver. [UNDER DEVELOPMENT]

    https://review.openstack.org/248585

  * [Nova] Translate power state strings with dict fornodes.set_power_state().[UNDERDEVELOPMENT]

    https://review.openstack.org/248584

  * [Nova] Add soft reboot support to ironic driver. [UNDER DEVELOPMENT]

    https://review.openstack.org/248586

  * [Nova] Add inject NMI support to ironic driver. [UNDER DEVELOPMENT]

    https://review.openstack.org/283411



