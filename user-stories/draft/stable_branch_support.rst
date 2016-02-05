Stable Branch Support
=====================

*Problem description*
---------------------
According to the current OpenStack release policy, any release will be
maintained by the OpenStack community for 13 months. In the Enterprise IT
environment, we can't move this fast. We need 4-6 months to first qualify a
new release, then there might be migration or integration issues that might
take longer time (e.g. 3-4 months to move). And vendor's distros come out
ranging from 1-6 or more months after a new OpenStack release is available.
This could totally take up to 18 months. Once we finally get a new release
finalized, we need to keep it stable for awhile before we move again.

The current OpenStack release model is not viable for all Enterprise IT or
Service Providers. In the Enterprise or Service Providers world, we need more
stability. Today, each distro vendor will provide their own maintenance and
support for EOL OpenStack releases, which will eventually create various
branches of EOL OpenStack out in the product environments. This will
eventually cost more work for the operators and vendors, and eventually slow
down the overall OpenStack adoption.

A few companies/vendors are willing to commit engineering resources to
support the stable branch work. Therefore, given significant business
justification, the OpenStack Community needs to find a process to maintain
releases for longer than one year.

User Stories
------------
As a cloud operator, I would like to run my OpenStack Cloud on a particular
release for more than a year while still receiving updates and patches for the
release that I use.

Usage Scenarios Examples
------------------------
* Operator's view
Infrastructure just moved from Gerrit 2.8 to Gerrit 2.11.
They were on 2.8 for two years before the switch, and it took them six
months to make it work. Operators require 4-6 months to first qualify a
new release, then another 3-4 months (minimum) to move. Vendor distros come
out 1-6 months after the OpenStack release. A longer support cycle will ensure
operators will still get bug fix and security enhancements while they upgrade on
in a time-frame that makes operational sense for them.

* Distro vendor's view
It is our goal to support our customers in their real-life situation.
Enterprise customers generally don't upgrade to a new release every 6 months.
We are willing to provide resources to the stable branch work. For example,
for Juno, the vendors were willing to provide resources but unfortunately TC
still decided to EOL Juno. By supporting a longer term stable release, all distro
vendors will be able to contribute to the code base in a coordinated way, eliminating
duplicate efforts and ensuring that customers can benefit from maintenance irrespective
of how they receive code.

Opportunity/Justification
-------------------------
The current enterprise adoption for OpenStack is not ideal. We believe that
the current model (only 2 concurrently supported releases) is one of the barriers for adoption.
OpenStack needs to be perceived as an "Enterprise-ready" platform. By addressing this perception,
we can increase the number of enterprises that would consider OpenStack to be a platform with
Enterprise levels of stablity and worth consideration for production deployment.

Similarly, by providing a long term release, more vendors would be willing to coordinate
support making it easier for the community to manage a single code base. This will increase
productivity while at the same time providing the stable solution that operators are looking for.

Related User Stories
--------------------
TBD.

*Requirements*
--------------
TBD

*Gaps*
------
There is no official process to qualify and support and EOL release in the
OpenStack community.

*Affected By*
-------------
The current TC decision making for this issue.

*External References*
---------------------
TBD.

Glossary
--------
None.
