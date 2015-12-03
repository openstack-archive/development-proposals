Capacity Control
===============

Problem description
---------------------

Deprecation of Flavors
``````````````````````

The cloud operator has old flavor types that are being replaced by newer flavor
types. Within the desired short term time frame T, it is not preferred to
disable new flavor types for all accounts (or projects), as existing accounts
may have deployments and automation scripts which require the older flavor
types. At the same time, there isn’t sufficient capacity to continue making the
flavor type for all accounts for the duration of T.

The cloud operator needs a way to selectively disable flavor types for a subset
of accounts - based on certain criteria. The subset of accounts needs to be
changed dynamically, without disruption to the rest of the system. This will
allow selected accounts to continue using older flavor types, without exposing
them to all accounts. Over time, all accounts will have the flavor type
disabled.

Limiting Flavor Allocation
``````````````````````````

The cloud operator has limited capacities of each flavor type, and this does not
allow all accounts (or projects) to use all flavor types as needed. The
different projects are used for different applications, and have different
flavor type needs.

The cloud operator needs a way to limit the number of servers of each flavor
type allowed for each project. With this, each project has sufficient quota of
the needed flavor type, and a more constrained quota for flavor types non
critical to the project.

Beta Testing Flavors
````````````````````

The cloud operator is introducing new flavor types, which will be beta tested by
a whitelisted set of customers. Other customers do not have access to the flavor
types, and there isn’t sufficient capacity to enable the new flavor type for all
users.

The cloud operator needs a way to selectively present the new flavor types to
only the beta accounts. and to selectively limit the number of new flavor type
servers a customer can build.

User Stories
------------

* As a cloud operator, I want to gradually replace the flavors available in my
  cloud so that I can deprecate them while minimizing end user impact.

* As a cloud operator, I want to limit the allocation of instances of a given
  flavor across my cloud to avoid running out of capacity.

* As an operator, I want to make some flavors available to only a subset of
  users so that I can trial new flavor types with a limited subset of tenants.

Usage Scenarios Examples
------------------------

#. Deprecation of Flavors

   a. Disable creation of instances of flavor X for all new tenants.
   b. Disable creation of instances of flavor X for existing tenants 1x1.
   c. Remove flavor X.

#. Limiting Flavor Allocation
#. Beta Testing Flavors


Opportunity/Justification
-------------------------
.. This section is mandatory.
.. Use this section to give opportunity details that support why
.. pursuing these user stories would help address key barriers to adoption or
.. operation.

.. Some examples of information that might be included here are applicable market
.. segments, workloads, user bases, etc. and any associated data.  Please replace
.. "None." with the appropriate data.

None.

Related User Stories
--------------------
.. This section is mandatory.
.. If there are related user stories that have some overlap in the problem domain or
.. that you perceive may partially share requirements or a solution, reference them
.. here.

None.

Requirements
------------

#. Flavor is presented to the user in the GET response to the flavor list, but
   there is a limited quota available for each flavor in the list.
#. Flavor is not presented to the user in the GET response to the flavor list,
   but user can still build if he attempts to create a new server of the flavor
   type.
#. Flavor is not present in the flavor list, and the user can not build a new
   server of the flavor type.

*Gaps*
------
.. This section is optional.
.. It might be useful to provide information in this
.. section if there is already some functionality in OpenStack
.. that might seem to fit your user story on the surface but, in reality, does not
.. actually fulfill the needs of the user type or the objective.  If you choose to
.. complete this section, please be sure to include information about the gap AND
.. why you believe the current functionality does not meet the requirement. Please
.. replace "None currently known." with the appropriate data. This section can
.. often be left with "None currently known." It is the purpose of this working
.. group and repository to use the use cases presented here to identify what the
.. gaps are.

None currently known.

*Affected By*
-------------
.. This section is optional.
.. This section should be used for prior records of
.. activity inside OpenStack related to this user story
.. (bugs that need to be fixed, blueprints for prior attempts, etc.).  If
.. possible, please include links to the related specs, blueprints, or bug reports.
.. Please replace "None." with the appropriate data.

None.

*External References*
---------------------
.. This section is optional.
.. Please use this section to add references for standards or well-defined
.. mechanisms.  You can also use this section to reference existing functionality
.. that fits your user story outside of OpenStack.  If any of your requirements
.. specifically call for the implementation of a standard or protocol or other
.. well-defined mechanism, use this section to list them.

None.

Glossary
--------
.. This section is optional.
.. It is highly suggested that you define any terms,
.. abbreviations that are not   commonly used in order to ensure
.. that your user story is understood properly.

.. Provide a list of acronyms, their expansions, and what they actually mean in
.. general language here. Define any terms that are specific to your problem
.. domain. If there are devices, appliances, or software stacks that you expect to
.. interact with OpenStack, list them here.

.. Remember: OpenStack is used for a large number of deployments, and the better
.. you communicate your user story, the more likely it is to be considered by the
.. project teams and the product working group.

.. Examples:
.. **reST** reStructuredText is a simple markup language
.. **TLA** Three-Letter Abbreviation is an abbreviation consisting of three letters
.. **xyz** Another example abbreviation
