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

In addition, the amount of time required to adjust quotas also impacts cloud consumers, eg application developers, because of delays in updating the project. 

    “I’d like it all to be self-service, even quota modification. Using tickets
     creates a delay that doesn’t have to be there. Tickets are still a manual
     process, and it doesn’t have to be that way.”

Operators have also expressed frustration that quotas are handled
inconsistently across projects:

::

    “The biggest problem is inconsistency. There are overlapping quotas in some
     projects and then none in Glance.”

::

    “It’s terrible. If someone requests floating IP in Nova, you need to change
     it in both Nova and Neutron. The UI finds the overlap, but if you use the
     API there is a mismatch.” 

::

    “One user gave the example of Nova and Neutron offering per-project quotas
     while Glance had a single global quota for image size. “It really boils
     down to having OpenStack act more like a single initiative, versus a
     collection of projects.””


The OpenStack UX project conducted a series of interviews to investigate pain
points associated with managing quotas which is providing data for this
specific user story.  The study results deck_ and video_ presentation can be
found at:

    .. _deck: https://docs.google.com/presentation/d/1J6-8MwUGGOwy6-A_w1EaQcZQ1Bq2YWeB-kw4vCFxbwM/edit?usp=sharing 
    
    .. _video: https://youtu.be/OobZWrDtFSM


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

These user stories utilize the standard OpenStack UX Personas:
http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html 

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

**Scenario: Adding quota flavor to a new project**
Consistency across quota flavors will add extra benefit on top of the tool
kit’s consistency within the code.

1. Rey is asked to add a project for a team that is doing data analysis to
correlate workplace injury and illness costs with specific causes such as back
injuries.
2. Rey logs into Horizon and opens the Identity tab. Under the Identity
tab, there is a page called Projects.
3. Rey clicks on the new project button and
begins adding the required information such as name, members, and member roles
for the new project.
4. Rey clicks on the new Project Flavor tab in the modal and
sees a UI that is not unlike the flavors tab for create instances.  Each quota
flavor has specific values based on the needs of the different projects.  For
example, there is a “Data Analysis” favor that includes more storage than the
other flavors.
5. In this case, Rey selects the Data Analysis quota flavor and applies it to
the new project. This prevents Rey from having to select each item, such as
RAM, individually which can be time intensive. 


**Scenario: Updating quota flavor for an existing project**

1. Rey has received a ticket to increase quota for a project.  
2. Rey opens Horizon and navigates to the Quotas Monitoring tab.  In this UI,
the projects are rows while the individual quotas, such as RAM, are located in
columns.   
3. Rey uses searchlight to find the correct project 
4. Rey then uses the dropdown at the right of the row to select the update
flavor action
5. A modal opens that is similar to the new project modal, but lands on the
project flavors tab with the current project flavor selected.
6. Rey selects a flavor with additional project quota and selects the update
project button.


**Scenario: Monitoring quota across projects**

1. Rey opens Horizon and navigates to the project panel where there is a list of
all projects by row with information 


Related User Stories
++++++++++++++++++++

None.


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
