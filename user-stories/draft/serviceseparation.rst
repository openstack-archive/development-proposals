OpenStack Service Separation
============================

*Problem description*
---------------------
We need separation between services to mitigate for library conflicts. This way 
instead of doing "openstack upgrade" we can do "nova upgrade" today, "neutron 
upgrade" tomorrow and on, and that approach simplifies things tremendously, 
because potential fallback is both easy and fast, and impact is much lower.

Biggest problems in upgradeable deployments are dependencies and speed of 
upgrade. Dependencies means, in case of shared libraries, several services might 
require same library, but often at different versions between major openstack 
releases. This will cause conflicts, and require us to do “all or nothing” 
upgrade. Sometimes we would like to use several maintenance windows to upgrade 
our deployment one service at the time. Also, we want this maintenance windows to 
be as short as possible, hence speed of deployment changes.

User Stories
------------
* As an OpenStack Operator, I select services to upgrade based upon the new 
features that have been implemented and bugs fixed. This will lead to different 
versions of Services running together my deployment. Different Services will be 
using different versions of system and 3rd party libraries.

Usage Scenarios Examples
------------------------
* Containers are new way to deploy microservices. Ever heard of Docker? Who
didn’t? We want to utilize containers flexibility, speed of deployment, and most
importantly, separation of services. With each service having its own library
base, we don’t have conflicts, and we can upgrade just one service at the time
without disruption of others.
 
* Kolla is project which does exactly that – containerize your openstack
services. By using Kolla you can utilize flexible container to be configured in a
way you ran your services for years, or, for those who want to start openstack
adventure, quick and easy way to set up production ready upgradable openstack
using ansible.

Opportunity/Justification
-------------------------
None.

Related User Stories
--------------------
None.

*Requirements*
--------------
* Ability to upgrade 1 OpenStack service, without having to upgrade all OpenStack
services
* Maintain overall system reliability when only 1 Service is upgraded
* Minimal or no downtime during upgrade

*Gaps*
------
None currently known.

*Affected By*
-------------
Real value can be realized using TripleO to deploy Kolla-based OpenStack. With
TripleO’s  baremetal and config management, and Kolla containers, deploying large
scale, upgradable, production ready OpenStack becomes an achievable use case.

*External References*
---------------------
None.

Glossary
========
None.