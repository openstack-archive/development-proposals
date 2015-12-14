Workflow
=======
Where Feature/Improvements Come From
------------------------------------
Feature or improvement ideas typically start from a few ways:

* User feedback collected by the product working group.
* IRC or Mailing list discussion.
* A patch within a project that's recognized as benefiting other projects.

How to Propose Feature/Improvements in OpenStack
-----------------------------------------------
Blueprints
^^^^^^^^^^
To formally propose a feature or improvement to an OpenStack project, you need
to create a Blueprint. Blueprints allow the community to track initiatives and
potentially mark them to a milestone in a release being developed. Some of the
information tracked is who is implementing it, current progress, and `more <https://wiki.openstack.org/wiki/Blueprints#Blueprints_reference>`_

`Read entire flow <https://wiki.openstack.org/wiki/Blueprints#Blueprints_only_lifecycle>`_

Project Specifications
^^^^^^^^^^^^^^^^^^^^^^
Some projects go a step futher with blueprints and ask for a set of information
up front to know whether a certain initiative is a good idea. This set of
information can be technical information such as:

* Application Programming Interface (API) impact
* Database impact
* Upgrade impact
* User impact

Specification information is not standard across the different OpenStack
projects, but you can see if a project does specifications by going to
https://github.com/openstack/<project>-specs and find their template file to
see what questions you need to answer.

Keep in mind not all ideas need a specification, so find out from the project
members if a certain idea warrants a full spec, or just a blueprint.

`Read entire flow <https://wiki.openstack.org/wiki/Blueprints#Spec_.2B_Blueprints_lifecycle>`_

Cross-Project Specifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If an idea spans to more than one project, it should be introduced in the
`OpenStack Specs repo <https://github.com/openstack/openstack-specs>`_ instead
a project specific Specification.

Each project that is involved with the specification should have a blueprint
registered, and the blueprint URL should be included in the OpenStack
Specification.

Product Working Group Liaisons Role
-----------------------------------
Introducing A Feature/Improvement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It should be assumed introducing a feature/improvement depending on
availability resources and other priorities, it'll likely require a notice of
a release or two with project teams before any work can begin. Therefore
planning and discussion should happen as soon as possible. A liaison will be
assigned to oversee an idea cross-project with the following responsibilities:

1. Create or have someone create the technical OpenStack specification.
2. CC cross-project spec liaisons of projects to specification for attention.
   If needed email cross-project spec liaisons for attention.
3. If any specifications needs additional attention, you can add an item to the
   `cross-project meeting agenda
   <https://wiki.openstack.org/wiki/Meetings/CrossProjectMeeting#Proposed_agenda>`_, 
   and have it be discussed realtime.
4. Specify in the cross-project spec the `topic branch
   <http://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows#Topic-Branches>`_
   for work to be carried out on. This will allow all development work in
   `gerrit <https://review.openstack.org>`_ to be found easily with the topic
   filter across the different projects.
4. Once enough consensus is met by the cross-project spec liaisons of the
   necessary projects, the specification will be passed to the Technical
   Committee for approval.


Tracking Feature/Improvement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. The Product Working Group Liaison should identify with each project involved
   who will actually implement the feature/improvement.
2. Alignment with each project implementing the feature/improvement in the same
   release is a nice to have. It should be fine to have some projects start
   early, but should be considered incomplete until all necessary projects are
   done implementing.
3. The Product Working Group liaison should continue to communicate with the
   implementers on each project to track progress. It's up to the liaison to
   identify when things are stalling and working with the project team on
   someone to carry on the work. If the implementer is unresponsive, a meeting
   with the project team should be called to find a new implementer.
