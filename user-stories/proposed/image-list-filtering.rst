Operator controlled image list filtering
========================================

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

*Problem Definition*
++++++++++++++++++++

The problem outlined below has been raised with the Glance team by various
operators.  Although it's not a cross-project effort, we are bringing it to the
Product Working Group as a place where product people and operators can refine
the user stories to the point where a Glance spec could usefully be written.
At this point, the Glance team has some ideas, but we'd prefer this effort to
be product/operator-driven rather than developer-driven.

Opportunity/Justification
+++++++++++++++++++++++++

Cloud operators supply *public images* that can be used by end users to boot
servers.  An example is an image containing the CentOS 7 operating system.
Such images must be updated as security concerns, etc., are addressed.  In
Glance, however, image data is immutable, so each update results in a new
public image.  Further, operators do not want to delete the "old" public
images, as end users may require them for server rebuilds.  As a result, the
default image-list for end users becomes very large.  Further, the default
image-list may contain multiple CentOS 7 images, for example, making it
difficult for end users to determine which image to use.

The current practice is to address this by putting a custom property on an
image, for example, ``"is_current": "yes"``, but this is operator-specific and
not interoperable.  This only solves part of the problem, however, because end
users must be educated to look for the ``"is_current"`` image property.  It
would be better if *only* those images with ``"is_current": "yes"`` were
included in the end user's default image-list in the first place.

That's the basic problem.  In addition, there are some related issues requiring
some thought:

* Image-show should work for the "retired" images, that is, an end user can see
  the image detail response if the end user knows the image ID.

* Image discovery of "retired" images should be possible, that is, and end user
  could find such images by adding an appropriate filter to the image-list call.

* Expanded default image-list: specific end users have more public images in
  their default image-list response.  Example: members of a "expert" group.

* Constricted image-list: specific end users have fewer public images in their
  default image-list response.  Example: members of a "novice" group.

There are cross-project implications of this scenario.  For example, an
operator might not want only to restrict the viewing of specific images in the
default image-list, but additionally prohibit specific users from using those
images (or, alternately, only allow specific users to use those images).
Should this be enforced by Glance, or by the services that would consume the
images?

Use Cases
---------

User Stories
++++++++++++
..  This section is mandatory. You may submit multiple
.. user stories in a single submission as long as they are inter-related and can be
.. associated with a single epic and/or function.  If the user stories are
.. explaining goals that fall under different epics/themes then please complete a
.. separate submission for each group of user stories.  Please replace "None." with
.. the appropriate data.

.. A list of user stories ideally in this or a similar format:

.. * As a <type of user>, I want to <goal> so that <benefit>

None.

Usage Scenario Examples
+++++++++++++++++++++++
.. This section is mandatory.
.. In order to explain your user stories, if possible, provide an example in the
.. form of a scenario to show how the specified user type might interact with the
.. user story and what they might expect.  An example of a usage scenario can be
.. found at http://agilemodeling.com/artifacts/usageScenario.htm of a currently
.. implemented or documented planned solution.  Please replace "None." with the
.. appropriate data.

.. If you have multiple usage scenarios/examples (the more the merrier) you may
.. want to use a numbered list with a title for each one, like the following:

.. 1. Usage Scenario Title a. 1st Step b. 2nd Step 2. Usage Scenario Title a. 1st
.. Step b. 2nd Step 3. [...]

None.

Related User Stories
++++++++++++++++++++
.. This section is mandatory.
.. If there are related user stories that have some overlap in the problem domain or
.. that you perceive may partially share requirements or a solution, reference them
.. here.

None.

*Requirements*
++++++++++++++
.. This section is optional.  It might be useful to specify
.. additional requirements that should be considered but may not be
.. apparent through the user story and usage examples.  This information will help
.. the development be aware of any additional known constraints that need to be met
.. for adoption of the newly implemented features/functionality.  Use this section
.. to define tahe functions that must be available or any specific technical
.. requirementsthat exist in order to successfully support your use case. If there
.. are requirements that are external to OpenStack, note them as such. Please
.. always add a comprehensible description to ensure that people understand your
.. need.

.. * 1st Requirement
.. * 2nd Requirement
.. * [...]

None.

*External References*
+++++++++++++++++++++
.. This section is optional.
.. Please use this section to add references for standards or well-defined
.. mechanisms.  You can also use this section to reference existing functionality
.. that fits your user story outside of OpenStack.  If any of your requirements
.. specifically call for the implementation of a standard or protocol or other
.. well-defined mechanism, use this section to list them.

None.

*Rejected User Stories / Usage Scenarios*
-----------------------------------------
.. This is optional
.. Please fill out this section after a User Story has been submitted as a
.. cross project spec to highlight any user stories deemed out of scope of the
.. relevant cross project spec.

None.

Glossary
--------

base image
    An operator-provided virtual machine image which users can utilize to boot
    VMs.  In the OpenStack Images v2 API, these are called "public" images and
    can be recognized by having the value ``public`` for the image property
    ``visibility``.  In OpenStack deployments, these images also have an image
    property named ``image_type`` defined on them with the value ``base``.

default image-list
    The default image-list is the content of the response to an unqualified
    (that is, without query string) ``GET v2/images`` call in the Images v2
    API.

    In the Images v2 API, the default image-list consists of the union of the
    following:

    * All public images
    * All images owned by the tenant of the user making the call (also known
      as "private" images)
    * All images shared with the tenant of the user making the call which have
      been "accepted" by the tenant 

    In the Newton release, the default image-list will also contain "community"
    images.

image property
    A key:value pair on an image.  Such entities are called "image properties"
    in the Images v2 API, but are called "image metadata" in the Compute v2
    API.

image-show
    The operation that allows a user to view the image record (the JSON
    representation of the the set of image properties defined on that image).
    In the Images v2 API, this is the ``GET v2/images/{image_id}`` call.

public image
    See **base image**.

