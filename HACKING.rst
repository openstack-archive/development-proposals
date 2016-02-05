openstack-user-stories Style Commandments
===============================================

- **Step 1**: Read the OpenStack Style Commandments http://docs.openstack.org/developer/hacking/
- **Step 2**: Read the following Product WG documents in recommended order:

  - `Product WG Wiki/Overview Page <https://wiki.openstack.org/wiki/ProductTeam#Mission>`_
  - `Product WG Taxonomy <doc/source/workflow/taxonomy.rst>`_
  - `Product WG Workflow <doc/source/workflow/workflow.rst>`_
- **Step 3**: Read HACKING.rst (this doc)

Product WG User Story Submission Process
----------------------------------------

- Follow instructions at `Documentation/HowTo/FirstTimers <https://wiki.openstack.org/wiki/Documentation/HowTo/FirstTimers>`_
    - This page will help you configure your local environment
- Clone openstack-user-stories using "git clone https://github.com/openstack/openstack-user-stories" and create a branch using "git checkout -b <branch>"
- Document your user story using our `approved template <user-story-template.rst>`_
- Save the user story in the "user-stories" directory with a unique name
- Document relevant information about the submission in a tracker using JSON.  Here is a link to the `tracker template <user-story-tracker.json>`_
    - For more information on the tracker format, you can read the `Tracker Overview <doc/source/tracker_overview.rst>`_
- Save the tracker file (with as much information as you are able to provide) in the "trackers" directory using the same unique name as the user-story but ending with a .json extension
- A member of the Product WG might contact you to review the submission using the email address associated with your Gerrit user.

User Story Endorsement Process
------------------------------
We might often have a user story in the repository that might be beneficial to multiple working groups or community members.  If you find a user story that applies to you or your SIG (Special Interest Group) then please endorse the user story.  Endorsement shows that the user story has importance to multiple groups and can help it earn a higher priority.

- Follow instructions at `Documentation/HowTo/FirstTimers <https://wiki.openstack.org/wiki/Documentation/HowTo/FirstTimers>`_
    - This page will help you configure your local environment
- Clone openstack-user-stories using "git clone https://github.com/openstack/openstack-user-stories" and create a branch using "git checkout -b <branch>"
- Find associated tracker for the user story in the "trackers" directory
- Modify the 'supporting working groups' or 'supporting individual members' accordingly

User Story Tracker
------------------------------
The tracker file for the user story has to be updated once a user story has gone through the workflow and has blueprints associated with it.

- Follow instructions at `Documentation/HowTo/FirstTimers <https://wiki.openstack.org/wiki/Documentation/HowTo/FirstTimers>`_
    - This page will help you configure your local environment
- Clone openstack-user-stories using "git clone https://github.com/openstack/openstack-user-stories" and create a branch using "git checkout -b <branch>"
- Find associated tracker for the user story in the "trackers" directory
- Modify the 'blueprints/specs' with the following information:
    - Project Blueprint/Spec Pertains To
    - Link to Blueprint/Spec
    - Status of Blueprint/Spec
- The overall completion for a user story is determined by number of blueprints/specs in completed status versus the overall number of blueprints/specs submitted against a user story.
