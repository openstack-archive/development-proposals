Improve error messages and logging
==========================================================

Personas Impacted
-----------------
*   Rey the Cloud Operator
*  Adrian the Infrastructure Architect

Cross Project Spec - None
User Story Tracker - None


Problem Description
-------------------
*Problem Definition*
++++++++++++++++++++
Operators and infrastructure architects have consistently noted that error
messages are not specific and therefore difficult to triage.

“Error messages returned to clients including horizon- command line- etc.”


“Logging - meaningful errors\Error reporting - stop giving users cryptic errors
which mean nothing to them”

“This is both for maintenance- upgrades and debugging. It's hard- since it's so
distributed- but e.g. better error messages- not only stack traces of RPC message
timeouts would already help operation.”

“it's more simpler things like receiving meaningless errors when a vm boot fails
because of a network issue as the error reason does not bubble up to the
compute manager.”

In addition, operators have also noted that log files are also difficult to use
because they are not specific and make difficult to find the root cause of issues
impacting their OpenStack clouds.  This is particularly problematic when issues
 span services.  For example, an issue with Nova is actually caused by a bug
in Neutron.

“I don’t have great logging or filters, so adding request IDs to a user call
that goes through all the services would be helpful to see in an error message.”

Opportunity/Justification
+++++++++++++++++++++++++
The ability to effectively triage issues related to OpenStack deployments
have a significant impact on operators and infrastructure architects.
Meaningful error codes are an important component of that process.


In addition, reviewing error codes are related with other with other activities
associated with triaging issues.  For example, meaningful errors codes
impact the usefulness of reviewing log files.  Finally, operators are able
to post errors codes to other operators through communication channels
such as IRC.

Use Cases
---------
User Stories
------------

*  As Rey the Cloud Operator, I would like to effectively triage issues
related to my OpenStack deployments by finding detailed information
associated with an error code.
*  As Rey the Cloud Operator, I would like to effectively triage issues
related to my OpenStack deployments by finding relevant and succinct
information to an error that may span services.

Usage Scenario Examples
+++++++++++++++++++++++
**Community help**
Rey has an issue that impacts the performance of their cloud
An error code is raised in either the log file or in the Horizon GUI
Rey posts the error code along with a short description to the community
IRC or email list
Another community responds with the correct answer


**Google help**
Rey has an issue that impacts the performance of their cloud
An error code is raised in either the log file or in the Horizon GUI
Rey posts the error code into Google
Google returns results that are relevant to the error code


**Triage log files**
Rey has an issue that impacts the performance of their cloud
Rey reviews the log file and finds the error code
Rey is able to track the code back to the actual service causing the error


Related User Stories
++++++++++++++++++++


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


None.


External References
Cloud Operator Interviews: Information Needs


`<https://docs.google.com/presentation/d/1LKxQx4Or4qOBwPQbt4jAZncGCLlk_Ez8ZRB_bGp19JU/edit?usp=sharing>`_


`<https://youtu.be/dktorTIqU5s>`_


These user stories utilize the standard OpenStack UX Personas
`<http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html>`_




Rejected User Stories / Usage Scenarios


None.


Glossary
