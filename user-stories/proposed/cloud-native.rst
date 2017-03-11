Enabling cloud-native OpenStack deployment, operation and life-cycle management
===============================================================================

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

*Problem Definition*
++++++++++++++++++++
This proposal specifies principles from recent application
architecture guidelines to guide application designers in separating out
their application functionality.  The purpose is to support running in a more granular and stateless manner conducive to distributed internet based computing.

While OpenStack is inherently meant to support this style of application, 
in many original projects OpenStack was not designed following some of 
these principles. This user story is meant to assist in identifying, 
prioritizing and tracking areas of OpenStack to benefit from a redesign.

Opportunity/Justification
+++++++++++++++++++++++++
Scale the key business and technical functions enabled by our software to
meet point in time demand. Scaling means designing the functions to operate
in small and discrete units that can be instantiated in a manner which can
increase and decrease in response to demand. This creates an efficient but
operationally flexible and hands off product.

Requirements Specification
--------------------------

Use Cases
+++++++++
.. This section is mandatory. You may submit multiple use cases in a single
.. submission as long as they are inter-related and can be associated with a
.. single epic and/or function.  If the use cases are explaining goals that
.. fall under different epics/themes then please complete a separate submission
.. for each group of use cases.  Please replace "None." with the appropriate
.. data.

.. Please provide a unique three character reference and three digit number for
.. each use case

.. A list of use cases targeted at OpenStack UX Personas, ideally in this
.. or a similar format:

.. * XXX### As `<type of user>`_, I want to <goal> so that <benefit>

This section utilizes the `OpenStack UX Personas`_.


* CLN001 As `Adrian`_ - infrastructure architect I need to break out my Open 
  Stack installation footprint to modularized / componentized workloads.  I 
  need a shift from vertical scaling to horizontal scaling in elastic cloud
  environments supporting small clouds, very large and multi-clouds with a
  mixture of both.

* CLN002 As `Rey`_ - cloud operator, for the purposes of most quickly 
  responding to business growth, need to move from single-threaded designs 
  to multi-threaded designs. This removes single point of contention 
  affinity so throughput can be spread across more resources (CPUs, racks, 
  centers). With a multi-threaded design, the application can better utilize 
  the underlying processing platform to achieve the best possible throughput.

* CLN003 As `Adrian`_ - infrastructure architect I need to show that 
  OpenStack can multi-task across centers. 

* CLN004 As `Adrian`_ - infrastructure architect I need the ability to scale 
  data horizontally rather than only vertically. This is needed to improves 
  availability by reducing failure surface for data (failure occurs on one, 
  not many partitions). 

* CLN005 As `Adrian`_ - infrastructure architect I need 
  to improve scalability by allowing parallelism across multiple compute and 
  storage resources vs. vertical scaling through faster CPUs. It requires 
  smaller code and memory footprint. It reduces I/O requirement impacts.

* CLN006 As `Quinn`_ - application developer and Rey - cloud operator, as we 
  don't know at the time the application is developed where various 
  dependent projects will run (different servers or different centers), we 
  need to reduce sensitivity to non-critical latency in app to app service 
  calls to allow more flexible placement in cloud datacenters. (reduce co-
  location requirements). This will allow more flexibility in geographic 
  location to align with currently available cloud capacity.

* CLN007 As `Wei`_ - project owner I need service level performance 
  instrumentation and metrics around each service with automated alerting to 
  capture deviations from expected service levels during migration and post 
  migration to the clouds. This ensures that software is performing at 
  expected levels and provides the basis for autoscaling.

* CLN008 As `Rey`_ - cloud operator, I need project level automated
  procedures to ensure the project reports and facilitates software currency 
  (i.e. versions and patches maintained) including underlying cloud services
  and 3rd party software and tools (n, n-1) This facilitates improved
  portability and adaption to cloud deployments and standards and reduced
  security risk.

* CLN009 As As `Adrian`_ - infrastructure architect I need the OpenStack 
  Control Plane to have automated service-discovery so that as new control
  plane services are deployed in a microservice fashion they can be auto 
  recognized and used by other microservices without redeployment.  See 
  `nginx.com blog about Microservice Implementation`_ for reference on this 
  need. This supports the continuous delivery of new control plane
  functionality without waiting and going through the full release testing 
  and upgrade processes.

.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html
.. _Adrian: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/Adrian
.. _Quinn: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/Quinn
.. _Rey: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/Rey
.. _Wei: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/Wei
.. _nginx.com blog about Microservice Implementation: https://www.nginx.com/blog/service-discovery-in-a-microservices-architecture/


Usage Scenario Examples
+++++++++++++++++++++++


**Scenario 1** - Operator expands from 1 to multi-sites

1. Management lets Adrian know that they need to expand cloud operations
   from the 1 initial site to 3 to support expanded business operations.
2. Rey scans for and analyzes the current production projects for running
   components and versions and implements copies of the same in new sites
   though at an initially small footprint.
3. Wei signs in and increases users base and thus expands into the new sites.

**Scenario 2:** Operator needs to rollback after an upgrade

1. Rey upgrades a project to a new version with improvements specified and
   needed by Quinn - Application Developer
2. Once the upgrade is complete Wei notifies Rey that there is an issue with
   his workloads in the traditional and older tenants and needs the upgrade
   rolled back. These same issues are not seen by Quinn who is successfully
   using the new functions.
3. Rey is able to drop and reinstantiate the previous version for Wei and
   leave the new function in place for Quinn.  For Quinn no rollback 
   occurs.  
4. Wei monitors and is aware of any service level exceptions in the new
   sites.
5. Rey monitors and expands underlying resources as the projects auto ramp up
   in terms of instances to meet demand.

Acceptance Criteria
+++++++++++++++++++
An instantiated OpenStack Cloud  scales virtualized resources at the VM and 
container level based on triggers like CPU usage, memory utilization, disk 
space available and network bandwidth. The project automatically detects and
responds to elastic conditions defined by the developer. As example the 
inability to handle a service response quickly would result in addtional 
micro-service instances. Beyond the example, these conditions
contemplate business or technical transactions, communications and
indicators which are more complex than traditional infrastructure
instrumentation.

Related User Stories
++++++++++++++++++++
* `Capacity Management`_  resource usage request (RUR) as described there is 
  a possible type of business trigger.
* `Containerized Openstack Management`_ specifies the operational 
  requirements of containerization software/approach.  Somewhat overlaps
  CLN009, though they are meant to point to different parts of openstack. 
  This proposal to the projects and that at the containerization tools. 

.. _Capacity Management: https://github.com/openstack/openstack-user-stories/blob/master/user-stories/proposed/capacity-management.rst
.. _Containerized Openstack Management: https://review.openstack.org/445386



*Requirements*
++++++++++++++

None.

*External References*
+++++++++++++++++++++

None.

*Rejected User Stories / Usage Scenarios*
-----------------------------------------

None.

Glossary
--------
See definitions of Cloud Native Applications and Micro-services: https://blog.sysaid.com/entry/demystifying-the-latest-cloud-terminology-part-1/ 
