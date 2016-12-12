Improve error messages and logging
==========================================================
Cross Project Spec - None

User Story Tracker - None


Problem Description
-------------------

*Problem Definition*
++++++++++++++++++++

Operators and infrastructure architects have consistently noted that error
messages are not specific and therefore difficult to triage. Here is some
feedback collected on this subject from operators:

* “Error messages returned to clients including horizon- command line- etc.”
* “Logging - meaningful errors\Error reporting - stop giving users cryptic
  errors which mean nothing to them”
* “This is both for maintenance- upgrades and debugging. It's hard- since it's
  so distributed- but e.g. better error messages- not only stack traces of RPC
  message timeouts would already help operation.”
* “It's more simpler things like receiving meaningless errors when a vm boot
  fails because of a network issue as the error reason does not bubble up to
  the compute manager.”
* “I don’t have great logging or filters, so adding request IDs to a user call
  that goes through all the services would be helpful to see in an error message.”

In addition, operators have also noted that log files are also difficult to use
because they are not specific and make difficult to find the root cause of
issues impacting their OpenStack clouds. This is particularly problematic when
issues span services. For example, an issue with Nova is actually caused by a
bug in Neutron.

Opportunity/Justification
+++++++++++++++++++++++++
The ability to effectively triage issues related to OpenStack environments
has a significant impact on operators and infrastructure architects.
Meaningful error codes are an important component of that process.

In addition, reviewing error codes is related to other activities associated
with triaging issues.  For example, meaningful error codes impact the
usefulness of reviewing log files and meaningful errors codes enable operators
to effectively communicate about issues in various channels including IRC, and
online forums.

Use Cases
---------
User Stories
------------
This section utilizes the `OpenStack UX Personas`_.

* As `Rey the Cloud Operator`_, I would like to effectively triage issues
  related to my OpenStack deployments by finding detailed information
  associated with an error code.
* As Rey, I would like to effectively triage issues related to my OpenStack
  deployments by finding relevant and succinct information to an error that may
  span services (eg. live migration, volume attach, and upgrade scenarios).

.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html
.. _Rey the Cloud Operator: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/cloud-ops

Usage Scenario Examples
+++++++++++++++++++++++

**Self Identification**
* Rey has an issue that impacts their cloud
* An error code and easily understandable message is raised in either the log
  file or in the Horizon GUI
* Rey quickly retrieves the appropriate log
* Rey is capable of interpreting the message and correctly determine the
  solution

**Community Help**

* Rey has an issue that impacts their cloud
* An error code and easily understandable message is raised in either the log
  file or in the Horizon GUI
* Rey quickly retrieves the appropriate log
* Rey posts the error code along with a short description to the community IRC
  or email list
* Another community member responds with the correct answer


**Google Help**

* Rey has an issue that impacts their cloud
* An error code and easily understandable message is raised in either the log
  file or in the Horizon GUI
* Rey quickly retrieves the appropriate log
* Rey posts the error code into Google
* Google returns results that are relevant to the error code


**Triage log files**

* Rey has an issue that impacts their cloud
* Rey reviews the log file and finds the error code
* Rey is able to track the code back to the actual service causing the error


Related User Stories
++++++++++++++++++++
None.

*External References*
+++++++++++++++++++++
* `Cloud Operator Interviews - Information Needs`_ (`video`_)
* `OpenStack April 2016 User Survey`_

.. _Cloud Operator Interviews - Information Needs: https://docs.google.com/presentation/d/1LKxQx4Or4qOBwPQbt4jAZncGCLlk_Ez8ZRB_bGp19JU/edit?usp=sharing
.. _video: https://youtu.be/dktorTIqU5s
.. _OpenStack April 2016 User Survey: https://www.openstack.org/assets/survey/April-2016-User-Survey-Report.pdf

*Rejected User Stories / Usage Scenarios*
-----------------------------------------
None.

Glossary
--------
None.
