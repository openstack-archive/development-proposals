Scheduler Simulator
==========================

*Problem description*
---------------------
Cloud Operators are often confronted with the need to perform what if scenarios on
proposed compute and block storage schedulers tweaks. As such they often want to
have access to a scheduler simulator, to make a series of "virtual" requests given a
specific scheduler configuration to see if the resulting virtual machine load
matches their expected or desired outcome.

User Stories
------------
*As a cloud operator, I want to be able to simulate my cloud's scheduler with a
variety of virtual machine request loads under a given scheduler configuration in
order to determine the optimal configuration for my desired outcome
*As a cloud operator, I want to be able to visualize the simulated scheduling of
virtual machines onto hosts in my environment so that I can quickly realize whether
a given configuration will result in my desired outcome

Usage Scenarios Examples
------------------------
1. Operator Runs Simulator
	a. Operator defines scheduler configuration
	b. Operator defines request load
	c. Simulator places load on "virtual" cloud given configuration
	d. Simulator provides results of that placement
	e. Simulator provides visual output of placement
	f. Operator determines if result is optimal and if not adjusts configuration
	
Opportunity/Justification
-------------------------
None.

Related User Stories
--------------------
None.

*Requirements*
--------------
None.

*Gaps*
------
None currently known.

*Affected By*
-------------
None.

*External References*
---------------------
None.