======================================
Product WG User Story Tracker Overview
======================================

This file provides an overview of the fields that should be included
when building a new tracker using the `sample tracker template <https://github.com/openstack/openstack-user-stories/blob/master/user-story-tracker.json>`_ located in this repository.

Hierarchy of tracker data
-------------------------

::

                         [ User_Story_Tracker_ID ]
                                     |
                                     |
                               -------------
                              |             |
                              |             |
                           [ task ]      [ task ]
                              |
                    [ cross-project spec ]
                              |
                         -----------
                        |           |
                   [ project ] [ project ]
                        |
                 --------------
                |              |
            [ spec ]     [ blueprints ]
                               |
                         --------------
                        |              |
                  [ blueprint ]  [ blueprint ]

Each user story can consist of multiple tasks, cross-project spec per task, multiple projects per task, spec per project, and multiple blueprints per project.

Any field that requires ``status`` should be one of the following values:

- ``none`` (this item is not required for the task)
- ``pending`` (this item is required but has not been created)
- ``in-progress`` (this item is being implemented)
- ``complete`` (this item has been implemented)


Description of fields used in the tracker:
------------------------------------------
``id``: this field should be unique in the repository

``date:`` date the tracker was created in MM-DD-YYYY format 

``description:`` user story title + " tracker"

``source``: URI (uniform resource identifier) for user story RST file

``status``: the first occurrence of status indicates the implementation status for the overall user story

``tasks``: names of cross-project specs associated with user story (comma-delimited)

- each value in provided for "tasks" becomes a section under tasks_status

``cross-project spec``: URI for cross-project spec RST file

``gerrit-topic``: topic to be used for submitting code that implements the cross-project spec

``xp_status``: indicates the implementation status for the overall task

``projects``: names of projects associated with this task/cross-project spec

- each value in provided for "projects" becomes a section under projects_status

``bp_name``: name of blueprint(s) that need to be implemented per project

``bp_status``: indicates the implementation status for for blueprint(s)

``spec``: URI for project spec RST file

``spec_status``: indicates the implementation status for the project spec

Example
-------

::

 {
    "id": "sample_tracker",
    "date": "02-05-2016",
    "description": "user-story tracker",
    "source": "https://github.com/openstack/openstack-user-stories/blob/master/user-story-tracker.json",
    "status": "in-progress",
    "tasks": [
        "cross-project-spec-name1"
    ],
    "tasks_status": {
        "cross-project-spec-name1": {
            "cross-project spec": "https://github.com/openstack/openstack-specs/blob/master/specs/cross-project-spec-1.rst",
            "gerrit-topic": "sample_tracker/cross_proj_1",
            "xp_status": "in-progress",
            "projects": [
                "cinder",
                "tacker"
            ],
            "projects_status": {
                "cinder": {
                    "blueprints": {
                        "cinder-bp-1": "pending",
                        "cinder-bp-2": "in-progress"
                    },
                    "spec": "https://github.com/openstack/cinder-specs/blob/master/specs/newton/cinder-spec-1.rst",
                    "spec_status": "in-progress"
                },
                "tacker": {
                    "blueprints": {
                        "tacker-bp-1": "pending"
                    },
                    "spec": "none",
                    "spec_status": "pending"
               }
            }
        }
    }
 }
