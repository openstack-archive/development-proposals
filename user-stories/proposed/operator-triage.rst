Improve triaging for operators
==========================================================


Personas Impacted
-----------------
*  Rey the Cloud Operator
*  Adrian the Infrastructure Architect

Cross Project Spec - None
User Story Tracker - None


Problem Description
-------------------
*Problem Definition*
++++++++++++++++++++
The ability to triage an issue within a deployment has a significant impact
on operators; particularly if the deployment becomes unusable to their
customers. However, documentation has been consistently identified as an
issue by operators in the OpenStack user surveys.


To better understand any issues related to documentation he OpenStack
UX team conducted a series of interviews with operators and discovered
the challenge to operators is not exclusive to OpenStack documentation.
In fact, operators follow a predictable process from “googling” an issue,
leveraging tribal knowledge within an enterprise, reaching-out to the entire
OpenStack community via IRC or email lists and finally reviewing the
code for potential bugs. In effect, this is a “information finding” issue
rather than specific to documentation.


“Information can be in so many different places. I want one search engine
to rule them all. Right now, the closest thing to that is Google.”


“I prefer to put a question out on a forum or mailing list, so people can
answer when they feel like it. It can feel presumptuous to ask for help in
IRC due to the expectation of a more immediate response.”


“By the time I look at the code, I’ve exhausted all other methods and
have to fix it myself.”


Opportunity/Justification
+++++++++++++++++++++++++
The ability to triage an issue within a deployment has a significant impact
on operators; particularly if the deployment becomes unusable to their
customers.
Use Cases
---------
User Stories
------------
*  As Rey the Cloud Operator, I need to be able to use Google and find
results that are relevant to my specific issue.
*  As Rey the Cloud Operator, I need to be able to reach-out to the
community and find solutions to hard problems.
*  As Rey the Cloud Operator, I should not have to look directly at code
to identify bugs.

Usage Scenario Examples
+++++++++++++++++++++++

**Relevant search results**
#. Rey has an issue that is impacting the performance their OpenStack cloud
#. Rey identifies the specific error code from the log file
#. Rey copies and pastes the error code to Google
#. The search results from Google are specifically relevant to the issue and
can include OpenStack docs, ask.openstack.com, blog postings and
discussion groups.
#. Rey clicks on the top result and finds information that enable them to
resolve the issue quickly.

Note: this is likely a SEO issue.

**Community support**
#. Rey has an issue that is impacting the performance their OpenStack cloud.
This is a challenging problem and requires significant expertise with OpenStack.
#. Rey posts a question to the operator IRC channel or email list with a
description of an issue and asks for help
#. Someone responds to the question with a detailed answer
#. Rey leverages the response and is able to resolve the issue with their cloud

Note: This is a deceptively difficult problem because it includes both technical
and behavioral components.

Related User Stories
++++++++++++++++++++
Update Ask OpenStack
https://specs.openstack.org/openstack/openstack-user-stories/user-stories/proposed/ask-openstack-update.html 

*Requirements*
++++++++++++++

None.


*External References*
+++++++++++++++++++++

Cloud Operator Interviews: Information Needs

`<https://docs.google.com/presentation/d/1LKxQx4Or4qOBwPQbt4jAZncGCLlk_Ez8ZRB_bGp19JU/edit?usp=sharing>`_

`<https://youtu.be/dktorTIqU5s>`_

OpenStack April 2016 User Survey

`<https://www.openstack.org/assets/survey/April-2016-User-Survey-Report.pdf>`_

These user stories utilize the standard OpenStack UX Personas

`<http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html>`_


*Rejected User Stories / Usage Scenarios*
-----------------------------------------

None.

Glossary
--------

