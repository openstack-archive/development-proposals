{
    "id": "0001",
    "date": "02-02-2017",
    "submitted_by": {
        "name": "Arkady Kanevsky",
        "email": "arkady_kanevsky@dell.com"
    },
    "description": "DB Hygiene",
    "source": "",
    "status": "in-progress",
    "tasks": [
        "DB Cleanup driver"
        "Per Project Cleanup"
    ],
    "tasks_status": {
        "DB Cleanup driver": {
            "cross-project spec": "",
            "gerrit-topic": "",
            "xp_status": "",
            "projects": [
                ""
            ],
            }
      },
      "Per Project Clenaup": {
          "cross-project spec": "",
          "gerrit-topic": "",
          "xp_status": "in-progress",
          "projects": [
              "nova",
              "cinder",
              "keystone",
              "glance",
              "neutron",
              "ironic",
              "tripleO",
              "telemetry",
              "heat"
          ],
          "projects_status": {
              "nova": {
                  "blueprints": {
                      "No more soft delete": "completed"
                  },
                  "spec": "https://blueprints.launchpad.net/nova/+spec/no-more-soft-delete",
                  "spec_status": "completed",
                  "blueprints": {
                      "Purge Soft Deleted Rows": "in-progress"
                  },
                  "spec": "https://blueprints.launchpad.net/nova/+spec/purge-soft-deleted-rows",
                  "spec_status": "temporarily abandon",
                  "blueprints": {
                      "Archival Framework": "not started"
                  },
                  "spec": "https://blueprints.launchpad.net/nova/+spec/archival-framework",
                  "spec_status": "abandon",
              },
              "cinder": {
                  "blueprints": {
                      "DB cleanup": "completed"
                  },
                  "spec": "https://blueprints.launchpad.net/cinder/+spec/db-cleanup",
                  "spec_status": "completed"
              },
              "keystone": {
                  "blueprints": {
                      "": ""
                  },
                  "spec": "",
                  "spec_status": ""
              }
              "glance": {
                  "blueprints": {
                      "": ""
                  },
                  "spec": "",
                  "spec_status": ""
              }
              "neutron": {
                  "blueprints": {
                      "": ""
                  },
                  "spec": "",
                  "spec_status": ""
              }
              "ironic": {
                  "blueprints": {
                      "": ""
                  },
                  "spec": "",
                  "spec_status": ""
              }
              "tripleO": {
                  "blueprints": {
                      "": ""
                  },
                  "spec": "",
                  "spec_status": ""
              }
              "telemetry": {
                  "blueprints": {
                      "": ""
                  },
                  "spec": "",
                  "spec_status": ""
              }
              "heat": {
                  "blueprints": {
                      "": ""
                  },
                  "spec": "",
                  "spec_status": ""
              }
          }
      }
  }
}
