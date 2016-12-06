Improve quota management at production scale for operators
==========================================================

Personas Impacted
-----------------
* Cross Project Spec - None
* User Story Tracker - None


Problem Description
-------------------

*Problem Definition*
++++++++++++++++++++

Operators have identified quota management across projects within production
scale deployments as inefficient.  One of the issues is that managing quotas
unnecessarily takes time away from other, more important, activities related to
their cloud.

    “Quotas are a very boring task. We manage things through Horizon, which
    requires many steps. I need to assign myself as an admin to see a user’s
    resources and calculate an increase from there.”

In addition, the amount of time required to adjust quotas also impacts cloud consumers, e.g.,
application developers, because of delays in updating the project.

    “I’d like it all to be self-service, even quota modification. Using tickets
    creates a delay that doesn’t have to be there. Tickets are still a manual
    process, and it doesn’t have to be that way.”

Operators have also expressed frustration that quotas are handled
inconsistently across projects:

    “The biggest problem is inconsistency. There are overlapping quotas in some
    projects and then none in Glance.”

    “It’s terrible. If someone requests floating IP in Nova, you need to change
    it in both Nova and Neutron. The UI finds the overlap, but if you use the
    API there is a mismatch.”

    “One user gave the example of Nova and Neutron offering per-project quotas
    while Glance had a single global quota for image size. “It really boils
    down to having OpenStack act more like a single initiative, versus a
    collection of projects.””

Additional data was taken from the 2016 OpenStack User Survey.


Opportunity/Justification
+++++++++++++++++++++++++

Quotas have a significant impact on operators to efficiently manage their
clouds. First, the time to adjust quotas in production environments, where
there can be thousands of projects, can be time-consuming.  In addition, the
time to adjust quotas can create unnecessary delays for cloud consumers.

Use Cases
---------

User Stories
------------

* As Rey the Cloud Operator, I would like to adjust quotas for my projects
  efficiently so I can focus on more complex issues.

* As Quinn the Application Developer, I would like to have my project quotas
  adjusted more quickly so I can focus on other value-added activities
  such as developing applications.


Usage Scenario Examples
+++++++++++++++++++++++

**Scenario: Streamlining quota management via a centralized tool kit**
This may improve inconsistent semantics through use of APIs, the delimiter
library, and the OpenStack Client. It also can help automate tasks that would
otherwise be manual.

**Scenario: Delegating control to domain operators**
Delegating quota management to domain ops allows them to allocate via nested
projects.

* Rey manages an OpenStack cloud for several domains within their enterrpise.
* Rey alloctes a "bucket" of resources to each domain
* Taylor has priviledges to assign quota to project swith their domain from
the bucket allocated by Rey.

**Scenario: Adding quota flavor to a new project**
Consistency across quota flavors will add extra benefit on top of the tool
kit’s consistency within the code.

* Rey is asked to add a project for a team
* Rey starts to create a new project workflow and adds the required
   information such as project name, members, and member roles.
* Rey also adds a specific quota flavor as part of the workflow based
   on the workloads required for the project. This is similar to an instance
   flavor, but specifies values for specific operational limits associated
   with each service.

**Scenario: Monitoring quota across projects**

1. Rey opens Horizon and navigates to the project panel where there is a list
   of all projects by row with information


Related User Stories
++++++++++++++++++++

None.


*Requirements*
++++++++++++++

None.


*External References*
+++++++++++++++++++++

Cloud Operator Interviews: Quota Management at Scale

* `<https://docs.google.com/presentation/d/1J6-8MwUGGOwy6-A_w1EaQcZQ1Bq2YWeB-kw4vCFxbwM/edit?usp=sharing>`_

* `<https://youtu.be/OobZWrDtFSM>`_

These user stories utilize the standard OpenStack UX Personas:

* `<http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html>`_


*Rejected User Stories / Usage Scenarios*
-----------------------------------------

None.


Glossary
--------
