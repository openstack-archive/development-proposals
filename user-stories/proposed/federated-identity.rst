.. This template should be in ReSTructured text. Please do not delete any of
.. the sections in this template.  If you have nothing to say for a whole
.. section, just write: None.  For help with syntax, see
.. http://sphinx-doc.org/rest.html You can also use an online RST editor at
.. rst.ninjs.org to generate proper RST.
.. Contact saverio.proto@switch.ch for questions on this document
.. Originally bootstrapped as https://etherpad.openstack.org/p/scientific-wg-rome-federated-identity-user-story

Federated Identity in Research Computing
==========================
**Sections in** *italics* **are optional.**

.. In order to propose submitting a User Story as a cross project spec replace
.. 'Cross Project Spec - None' with 'Cross Project Spec - Ready for Submission'
.. after this change is accepted and merged then submit the Cross Project Spec
.. to the openstack/openstack-specs repository and replace 'Ready for
.. Submission' with a link to the review, and after merger of the Cross Project
.. spec with a link to the spec. Before proposing be sure to create and provide
.. a link to the User Story Tracker

Cross Project Spec - None

User Story Tracker - None

Problem description
-------------------

*Problem Definition*
++++++++++++++++++++
.. This section is optional.
.. Please use it to provide additional details (if available) about your user story
.. (if warranted) for further expansion for clarity.  A detailed description of the
.. problem. This should include the types of functions that you expect to run on
.. OpenStack and their interactions both with OpenStack and with external systems.
.. Please replace "None." with the problem description if you plan to use this
.. section.

Scientific collaborations and research groups are often composed of users from
different Home Organizations across different countries. NRENs and research
infrastructures in different countries across Europe would like to be able to
provide access to resources on their own Openstack services to users from other
Home Organisations and/or countries, and vice versa.
National Research and Education Networks (NREN) built SAML based Identity
Federations leveraging Universities and Research Institutions Identity
Providers. National Identity Federations are currently used to authenticate and
authorize milions of users and enable single sign on across thousands of
services.  Openstack based public cloud computing is enabled with Federated
Identity login.
NRENs offer public cloud services with Openstack, where end users belong to
institutions like universities and research institutes. We have three actors,
the NREN running the public cloud, the user and the university acting as an
identity provider.
Openstack services and dashboards need to be configured as Service Providers
within identity federations and have to be accessed like all other services.
As a manager of research computing infrastructure, I need to enable users  from
other institutions to Authenticate and get authorized on resources.



Opportunity/Justification
+++++++++++++++++++++++++
.. This section is mandatory.
.. Use this section to give opportunity details that support why
.. pursuing these user stories would help address key barriers to adoption or
.. operation.

.. Some examples of information that might be included here are applicable market
.. segments, workloads, user bases, etc. and any associated data.  Please replace
.. "None." with the appropriate data.

Effective collaboration between institutions is vital to success in research.
OpenStack is uniquely positioned.  Universities and research institutions use
OpenStack to deliver research computing services.  Through improved support for
identity federation, OpenStack can support collaboration between institutions.
Full  support for federations in the AAI  - implying support for multiple
sources of Authentication and federation protocols - would enable extending the
user base for Cloud services provided via openstack to the natural largest
possible set represented by the eduGAIN interfederation users; this would lead
to wider adoption of Cloud resources and services by the community of users,
and collaborations implemented across single, individual home organizations.


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

* As a user of the scientific collaboration, I want to use the OpenStack
  resources available to my collaboration that are spread between several
  service providers, using my home organization credentials

* As a user, I want to allow services and/or robots to act on my behalf,
  without exposing my home organization credentials.

* As a manager of research computing infrastructure, I need to enable users
  from other institutions to Authenticate and get authorized on resources.  I
  need to do this without compromising the security of my resources. I need to
  be able to manage arbitrary numbers of federated identity providers for my
  cloud infrastructure in a secure and convenient way.

* As a manager of computing services for researchers, I need to be able to
  provide a mechanism to authenticate my users to enable them to access
  resources in other institutions.

* As a manager of research computing infrastructure, I need to be able to audit
  and account for the usage of federated users from other institutions.

* As an Openstack admin I need to authorize users to different projects
  independently from their home organization identity provider

* As a Openstack admin, I need to create mappings between users and projects. A
  user that does not map to any project will not be able to access any
  resources even if his identity is verifiable. The projects are created by the
  cloud operator upon agreement with a project owner who is responsible for the
  resources cost. 

* Because in this model the resources are paid by projects and not by users, it
  is the responsibility of the project owner to revoke the rights of a user that
  leaves a project.

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

1. Rick the researcher accesses Openstack Horizon with Federated Identity
a. In the browser Rick opens the Horizon Web Page of an OpenStack instance run by another organization, but where Rick has access
b. On the Login page, Rick selects the Federation option
c. Rick gets redirected to the a web page, where Rick selects his home organization
d. Rick gets redirected to his IdP
e. Rick logs in to his IdP
f. Rick gets redirected back to Horizon, and is logged in

2. Sally Scientist accessses Federated OpenStack resources using the CLI/API
a. Sally does usage scenario 1
b. When Sally is logged in to Horizon, Sally downloads or creates credentials for non-web use. These credentials are valid for this OpenStack instance.
c. Sally exposes the credentials to the OpenStack CLI
d. Sally is able to get a Keystone token using the credentials

.. (aloga) I don't understand this scenario. Step (b) is an ankward step from the user point of view. If the user has to manage several credentials for several OpenStack providers the federation does not exist.


3. (extended use case of 2) Sally Scientist accesses Federated OpenStack resources using the CLI/API
a. Sally does usage scenario 1
b. When Sally is logged in to Horizon, Sally links her local Horizon account to
   information from her Home Organisation. This link is valid for this OpenStack
   instance.
c. Sally authenticates herself using an unspecified side-channel method that
   does not expose her Home Organisation that allows Keystone to issue a token.
d. Sally is able to use the token to access services.
4. Which of these - or both?
4a. Adam administrator is deleting a user who has federated resources at other institutions
4b. Adam administrator has cloud resources with federated users from other institutions and wants to know if the users are still valid.


Related User Stories
++++++++++++++++++++
.. This section is mandatory.
.. If there are related user stories that have some overlap in the problem domain or
.. that you perceive may partially share requirements or a solution, reference them
.. here.

The Role Based Access user story is related.
http://specs.openstack.org/openstack/openstack-user-stories/user-stories/proposed/rolebasedaccess.html

The GSSAPI user story is related (for CLI access):
https://etherpad.openstack.org/p/JISC-GSSAPI

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

* Openstack Kilo is needed for this use case as Keystone Service Provider support is required
* 

None.

*External References*
+++++++++++++++++++++
.. This section is optional.
.. Please use this section to add references for standards or well-defined
.. mechanisms.  You can also use this section to reference existing functionality
.. that fits your user story outside of OpenStack.  If any of your requirements
.. specifically call for the implementation of a standard or protocol or other
.. well-defined mechanism, use this section to list them.

- The INDIGO Identity and Access Management (IAM) service: https://github.com/indigo-iam/iam
- INDIGO Keystone OpenID-Connect integration guide: https://www.gitbook.com/book/indigo-dc/openid-keystone

*Rejected User Stories / Usage Scenarios*
-----------------------------------------
.. This is optional
.. Please fill out this section after a User Story has been submitted as a
.. cross project spec to highlight any user stories deemed out of scope of the
.. relevant cross project spec.

None.

Glossary
--------

Home Organisation - The 'home' of a user, i.e. the university or research
institute that a researcher or student is a member of. The Home Organization
usually runs an IDP which its users authenticate against.

eduGain - An interfederation of national identity federations, designed to
allow services and identities to interoperate across these identity
federations. For the purpose of this use case, assume that eduGain means any
identity federation. See
http://www.geant.org/Services/Trust_identity_and_security/eduGAIN for more
information on eduGain.

NREN - National Research & Education Network. An organisation or physical
network operated by an organisation, to provide dedicated network resources to
the education and research sector in a country. In the context of this use
case, an NREN refers to an organisation (such as GARR, SURF, Jisc, CSC ...)

IDP - Identity Provider. A service that provides authentication for users,
often by username and password. In the context of this use case, this is a
server running either SAML or OIDC authentication software

SP - Service Provider. A resource providing a service. In the context of this
use case, this is a server providing a resource, i.e. Horizon, Keystone, a
hypervisor, a website...

Identity Federation - A set of IDPs and SPs with commonly defined priciples for
data usage, and for building trust relationships between IDPs and SPs (Uaually
on a national level)

SAML - Security Assertion Markup Language. The most common standard for
building Indetity Feredations

OIDC - OpenID Connect. A lightweight authentication and authorisation protocol,
popular for its ease of deployment. For more information on OIDC, see
http://openid.net/connect/

OAuth 2 - The OAuth delegated authorization framework. For more information, see https://oauth.net/2/

SCIM: The System for Cross-Doman Identity Management, a standard  to manage
user identity in cloud-based applications and services in a standardized way to
enable interoperability, security   and scalability. For more information, see
http://www.simplecloud.info/. SCIM is an enabling technology for identity
provisioning/deprovisioning.

AAI - Authentication and Authorisation Infrastructure. A collective term for
software stacks that provide authentication and authorisation. An extended term
of this is AAAI, which includes accounting.


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
