Add Use Cases to Code Snippets in Docs
======================================

Cross Project Spec - None

User Story Tracker - None

Problem Description
-------------------


*Problem Definition*
++++++++++++++++++++
Operators have noted that it is easier to learn the commands associated with
the different OpenStack projects if examples, or usage snippets, were provided
for specific usage patterns. Some of the specific feedback we heard from
operators was:

* “You could add examples to the output of the CLI help commands, but I don't
  think there was ‘anything that was unclear’ enough, and that might actually
  contribute to too much help clutter.”
* “Adding more examples in the documentation.”
* “It is a good client, adding examples to the help would be very helpful.”

The use case-based snippets provide two benefits to both operators and
application developers.  First, the snippets help users understand how code
is structured for the various OpenStack projects.  In addition, users are able
to re-use the snippets for their own needs.  This is why the snippets should
be based on common use cases.

Opportunity/Justification
+++++++++++++++++++++++++
Use case-based snippets can significantly reduce the learning curve
associated with learning both the commands and structure associated for
the various projects.  For example, operators mentioned during the
OpenStackClient usability studies in both Austin and Barcelona that it took
time to learn the command structure.  However, they were able to efficiently
use the client once they became familiar with the structure.

Requirements Specification
--------------------------

Use Cases
+++++++++
These user stories utilize the standard `OpenStack UX Personas`_.

* As `Rey the Cloud Operator`_, I would like to quickly learn commands and
  structure associated with each project. In addition, I would like to have
  snippets for common use cases that I can modify for my own purposes.
.. _Rey the Cloud Operator: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/cloud-ops.html
.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html

Usage Scenario Examples
+++++++++++++++++++++++
#. Rey has decided to explore the OpenStackClient (OSC) as an alternative to
   using the individual APIs
#. Rey opens the OpenStack documentation page
#. Rey opens the new Use Case chapter (page) and sees several snippets of
   code based on common use cases
#. Rey now understands how the commands and structure are used to
   complete common tasks

Note: The best analogy seems to be to learning to read.  A dictionary and an overview
of language structure is useful.  However, actually seeing both words and structure
used in a sentence ties everything together in a meaningful way.


Related User Stories
++++++++++++++++++++
None.

*Requirements*
++++++++++++++
None.

*External References*
+++++++++++++++++++++
* `Operator OpenStackClient Validation Study (Barcelona 2016)`_
* `Operator OpenStackClient Validation Study (Austin 2016)`_

.. _Operator OpenStackClient Validation Study (Barcelona 2016): https://docs.google.com/presentation/d/1K-XImqK4-ODUvA1dr9t2LiUGib54MMKh1ANJJ2pldhU/edit?usp=sharing
.. _Operator OpenStackClient Validation Study (Austin 2016): https://docs.google.com/presentation/d/19ef_3mG9p_G2ZsUcgTAj9hmOynxL5LAyQD7KlXIbYBU/edit?usp=sharing

*Rejected User Stories / Usage Scenarios*
-----------------------------------------
None.

Glossary
--------
None.
