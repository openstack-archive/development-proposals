Traceability in OpenStack services
==================================

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

*Problem Definition*
++++++++++++++++++++

OpenStack is built upon not only OpenStack service programs but also various
mandatory external components (MySQL, RabbitMQ..) and follows the
micro-services architecture. As it often happens, moving into the micro-services
architecture brings its own challenges. Among them is the loss of visibility
into the system, and the complex interactions that occurs between services.
Operators maintaining OpenStack somehow still hit some bumps in the road of
trouble-shooting the part of OpenStack system. There are two components
which their role and importance are essential in trouble-shooting: per-process
logging and metric monitoring, but neither can reconstruct the elaborate
journeys that transactions take as they propagate across the micro-services
architecture. This is where traceability in services thrives. The user stories in this use case focuses on the need of traceability in OpenStack and some
enhancements that can be applied.

Problems of current solutions for trouble-shooting are:

#. Logging is an important triage tool to help operators get out of the woods
   and it works well to some extent. Logging is suitable for recording events,
   especially error events, and with logging operators can know something wrong
   happens within/with current systems. However, for realizing reliable root
   cause and trouble-shooting as quick as possible, logging is not sufficient
   because in micro-services architecture, operators can't usually know why and
   how problems happened from the logs with enough evidences/clues. Operators
   need detailed data of process flow for that purpose, which is usually the
   role of tracing.

#. Information from logs are heavily depended on how developer intent to
   express the problems via coding. Therefore, one problem may be duplicated
   to multiple services with the same misleading information. Thus, operators
   must find another approach to analyze these information for finding the
   root cause of the problem in these flows. There are no such general
   solutions for auto-infering the root cause from misleading messages of
   every services.

We need another approach and solution that can ensure the information flow
correlation between micro-services and help us find the root cause as quick as
possible. Especially in OpenStack, the callee-caller information between micro
services becomes more important for trouble-shooting.

Opportunity/Justification
+++++++++++++++++++++++++

Cloud services providers really want a OpenStack tracability solutions that can
help operators quickly and easily finding a root cause of problems.
They want to have a consistency of view through hundred OpenStack services
enough for productive mining in operator works.

It can be easy to trouble-shoot simple OpenStack deployment (e.g without HA),
it can also be easier to trouble-shoot individual OpenStack service; but with
the common and complex OpenStack deployment model (e.g with HA, LB),
trouble-shoot can become nightmare task for any cloud operator.

There are some discussions in OpenStack deployment projects such as Kolla in
deprecating current implemented logging solutions (Heka) and find another ways
to enhance operator's logging experiences.

There are also a native library in OpenStack which support for profiling across
OpenStack services: OSProfiler. However, all OpenStack projects need to
completely integrate OSProfiler inside their code-base and users must enable
OSProfiler for profiling and tracing log requests. At this time, almost all
projects in OpenStack have finished integrating OSProfiler. There is also some
performance impact of OSProfiler because it will inject some meta-data for
tracing in each HTTP/DB/RPC requests.

Use Cases
---------

User Stories
++++++++++++

This section utilizes the `OpenStack UX Personas`_.

* TR001 - As `Rey the Cloud Operator`_, I want to find and investigate the root
  cause of problems in my system as quick as possible so that I can resolve it
  and ensure our business.

* TR002 - As `Rey the Cloud Operator`_, I want to have a trouble-shooting
  solution that requires less efforts in deploying, maintaining and have
  minimal impact in my business so that I can ensure the qualitative aspect of
  my core businesses.

* TR003 - As `Wei the Project Owner`_, I want to ensure the solving process of
  problems as quick as possible to so that I can run our appliances and systems
  with minimum (or even zero) downtime.

* TR004 - As `Wei the Project Owner`_, I want to reduce the efforts in human
  resources and technical aspects for trouble-shooting issues in my system so
  that I can focus on core value of project.

* TR005 - As `Taylor the Domain Operator`_, I want to limit and handle
  permissions to access to the logs and metrics in my system, so that I can
  restrict some specific and dangerous permissions to limited operators.

* TR006 - As `Taylor the Domain Operator`_, I want to spend less resources
  (computation, networking, storage,...) on manipulating log data, processing
  monitoring metrics for alarming/notifying, so that I can save resources to do
  other tasks.

.. _OpenStack UX Personas: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas.html
.. _Rey the Cloud Operator: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/cloud-ops.html
.. _Wei the Project Owner: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/project-owner.html
.. _Taylor the Domain Operator: http://docs.openstack.org/contributor-guide/ux-ui-guidelines/ux-personas/domain-operator.html

Usage Scenario Examples
+++++++++++++++++++++++

1. Easier root cause analysis in OpenStack system
  a. Enterprise cloud operator query all error tracing requests for quickly
     detecting problems.
  b. Enterprise cloud operator view/filter individual tracing request for
     finding the last traced element which is the root cause.

2. Always-on controlled tracing mechanism for trouble-shooting system
  a. Enterprise cloud operator enable tracing mechanism with controlled
     over-head performance for ensuring no impact in core business.
  b. Enterprise cloud operator can easily change the allocated resource for
     overhead control.

Related User Stories
++++++++++++++++++++

None.

*Requirements*
++++++++++++++

None.

*External References*
+++++++++++++++++++++

* `[SPEC] [Oslo] OSprofiler cross service & project profiling <https://specs.openstack.org/openstack/oslo-specs/specs/mitaka/osprofiler-cross-service-project-profiling.html>`_
* `[BP] [Nova] OSProfiler in Nova <https://blueprints.launchpad.net/nova/+spec/osprofiler-support-in-nova>`_
* `[BP] [Magnum] OSProfiler in Magnum <https://blueprints.launchpad.net/magnum/+spec/osprofiler-support-in-magnum>`_
* `[BP] [Manila] OSProfiler in Manila <https://blueprints.launchpad.net/manila/+spec/manila-os-profiler>`_
* `[BP] [Senlin] OSProfiler in Senlin <https://blueprints.launchpad.net/senlin/+spec/senlin-osprofiler>`_
* `[BP] [Horizon] OSProfiler in Horizon <https://blueprints.launchpad.net/horizon/+spec/openstack-profiler-at-developer-dashboard>`_

* `[BP] [OSProfiler] Overhead control in OSProfiler <https://blueprints.launchpad.net/osprofiler/+spec/osprofiler-overhead-control>`_
* `[LCOO-WG] [Logging] LCOO Logging Working <https://etherpad.openstack.org/p/LCOO-Working-Logging>`_
* `[LOG-WG] OpenStack Log Working Group <https://wiki.openstack.org/wiki/LogWorkingGroup>`_
* `Distributed tracing applied at Uber <https://eng.uber.com/distributed-tracing/>`_

*Rejected User Stories / Usage Scenarios*
-----------------------------------------

None.

Glossary
--------

TBD.
