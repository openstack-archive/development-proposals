This work is licensed under a Creative Commons Attribution 3.0 Unported License.
http://creativecommons.org/licenses/by/3.0/legalcode

Configuration for RefStack
=========================

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

Problem Definition
+++++++++++++++++++

Customer decision maker for a choice of OpenStack solution to acquire
often need configuration information that was used for certification
to decide which solution to choose that ensures interoperability with other openstack
environments, and/or portability of applications across OpenStack solutions.

OpenStack operators would like to setup a configuration for an OpenStack deployment that provides
interoperability support for their users. Thus, they need information from RefStack about the
configuration used for DefCore certification of vendor solution.

Opportunity/Justification
+++++++++++++++++++++++++

The goal of Openstack interoperability branding <www.openstack.org/brand/interop/> is to ensure
interoperability between OpenStack clouds to support portability of applications between them.
Unfortunately, this portability is heavily dependent on full openstack solution configuration
that consists of openstack configuration as well as underlying HW environment configuration.

The proposal is to provide information necessary for operators and decision makers to decide
which configuration(s) and which vendor solution will satisfy their interoperability
requirements. Configuration information requested is similar to the one that
many benchmarking groups, like TPC and SPEC, provide with their results.

Use Cases
---------

User Stories
++++++++++++

* Private Cloud

  * As a Cloud solution decision maker I want to choose private OpenStack solution that meet
    my application interoperability requirements. Thus, I need to ensure that my openstack solution
    configuration ensures interoperability.

  * As a Cloud solution decision maker I want to choose private OpenStack solution that meet
    my application interoperability requirements on HW vendor of my choice. Thus, I need to ensure
    that solution interoperability results are applicable on my HW choice.

  * As a Cloud solution decision maker I want to choose private OpenStack solution for PoC that meet
    my applications interoperability requirements on HW that is available in my lab now. Thus,
    I need to ensure that solution interoperability results are applicable on my HW choice.

  * As a Cloud solution decision maker I want to choose OpenStack solution that supports multiple
    hypervisors for my applications and meet interoperability requirements for all of them.

  * As a Cloud operator I want to choose hypervisor for my OpenStack solution configuration that
    provide application interoperability. Thus, as cloud operator I want to see which
    hypervisor was used by vendor for refstack result submissions.

  * As a Cloud operator I want to choose container management for my OpenStack solution
    configuration that provide application interoperability. Thus, as cloud operator
    I want to see which container management was used by vendor for refstack result submissions.

  * As a Cloud solution decision maker I want to choose OpenStack solution that supports
    interoperability for bare metal applications.

  * As a Cloud operator I want to configure my OpenStack solution configuration that ensures
    bare metal application interoperability. Thus, as cloud operator I want to see what
    configuration for OpenStack and what HW and its configuration
    used by vendor for refstack result submissions.

  * As a cloud operator I would like to replicate vendor interoperability results.
    This requiers exact configuration of complete OpenStack solution, including HW choices,
    its configuration, mapoing of openstack component to HW and OpenStack configuraion for
    each OpenStack projects.

* Public Cloud

  * As a Cloud solution decision maker I want to choose public OpenStack solution that meet
    my applications interoperability requirements. Thus, I need to ensure that public OpenStack
    solution provider deploys my applications on the same OpenStack configuration that was used
    for DevCore Logo certification.

  * As a Cloud solution decision maker I want to choose OpenStack solution that supports containers
    for my applications and meet interoperability requirements for them.

  * As a Cloud operator I want to choose hypervisor for my OpenStack solution configuration that
    provide application interoperability. Thus, as cloud operator I want to see which
    hypervisor was used by vendor for refstack result submissions.

  * As a Cloud operator I want to choose container management for my OpenStack solution
    configuration that provide application interoperability. Thus, as cloud operator
    I want to see which container management was used by vendor for refstack result submissions.

  * As a Cloud solution decision maker I want to choose OpenStack solution that supports
    interoperability for bare metal applications.

  * As a cloud operator I would like to replicate vendor interoperability results.
    This requiers exact configuration of complete OpenStack solution, including HW choices,
    its configuration, mapping of openstack component to HW and OpenStack configuraion for
    each OpenStack projects as chosen by vendor. While these choices are not visible to a user
    in public cloud, an identifier for an exact environment that was used for
    RefStack results by the vendor that can be used by
    the user can be used. That covers, HW choices, openstack projects configuration, environment
    in which it is running, Availability Zone, Host Aggregate, High Availability.

Usage Scenarios Examples
++++++++++++++++++++++++

*  I want to choose an OpenStack solution

  * I have a list of VM applications that are required to be portable

  * I have a list of docker container based applications that are required to be portable

  * I need to provide environment for my dev/QA team to develop portable applications

  * I have a short list of preferred HW partners

  * I review openstack vendors that have foundation logo for interoprability to see
    which ones passed certification on KVM.

  * I review openstack vendors that have foundation logo for interoprability to see
    which ones passed certficiation on docker containers.

  * I review HW partners logo at OpenStack interoperability list and choose ones that meet
    my container and hypervisor requirements

* I install a chosen vendor OpenStack product as admin in my organization.

  * I review vendor interoperability submission results to configure my deployment
    so it will pass interoperability testing

  * I run refstack interoperability on it as base validation.

  * I run refstack interoperability on OpenStack public cloud that has logo
    interoperability certification, say rackspace.

  * I compare results between themselves and between refstack results on record.

  * If results do not match expectations I send email to interop@openstack.org, a ticket get
    generated and the issue is escalated to proper level for resolution.

  * If results are successful, I deploy and run an application on my private cloud.

  * I deploy the same application at OpenStack public cloud that has logo interoperability
    certification, say rackspace.

  * I compare results of two runs to ensure that they are the same.

Related User Stories
++++++++++++++++++++

* <https://review.openstack.org/#/c/207209/8>

Requirements
++++++++++++

* Identification of configuration items and values that are important in parametarizing
  the interoperability of each specific implementation of OpenStack cloud.

* Tool to extract openstack configuration files, anonymize them for sensative information,
  like passwords, and combined them into reporting entity.

* Enhance RefStack client to use above tool to collect and report pertinent configuration
  information as defined by DevCore submission guidelines.

* Definition for unique OpenStack public cloud product+configuration that is submitted to RefStack
  with the configuration information that is queryable and discoverble by users.

External References
+++++++++++++++++++

None.

Rejected User Stories / Usage Scenarios
---------------------------------------

None.

Glossary
--------

* [TPC] `<www.tpc.org> - Transaction Processing Performance Council`

* [SPEC] `<www.spec.org> - Standard Performance Evaliation Corporation`
