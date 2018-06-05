.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

==================
Event Waiting List
==================

This module extends the functionality of events to support registration of
attendees through a waiting list.

Usage
=====

TODO Fixme : it's only backend here

To use this module, you need to add a link to the waiting list registration
controller on your event.
URL for waiting list registration is defined by ```/event/<model("event.event"):event>/waiting_list_registration```.

Known issues / Roadmap
======================

TODO Fixme

* There is no registration order on the waiting list yet. Add a sequence or use a date ?
* Actions from CRM Leads/Opportunities are available in waiting list tree view
* Advanced filters and groupby from CRM Leads/Opportunities are available in waiting list search view
* What to do with linked crm.leads when waiting_list is deactivated on the event ?
* Add a wizard to transform waiting list leads in attendees ?
* Add security groups ? ir.rules to separate waiting list from leads/opportunities
* Check side effects on CRM module ?

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/camptocamp/odoo-event-addons/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://odoo-community.org/logo.png>`_.

Contributors
------------

* Akim Juillerat <akim.juillerat@camptocamp.com>

Do not contact contributors directly about support or help with technical issues.

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
