.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

==================
Event Waiting List
==================

This module extends the functionality of events to support registration of
attendees through a waiting list, using the CRM module and leads model.

Usage
=====

When maximum attendees to an event is limited, this module allows to flag the
event as using a Waiting list.
A smart button will then appear on the event to display linked crm.leads of
'event_waiting_list' type.

Known issues / Roadmap
======================

* Although some things we considered (rules, separated menus and actions),
  extensive testing is required if CRM is to be used next to this module.
* Actions from CRM Leads/Opportunities are available in waiting list tree view
* Advanced filters and groupby from CRM Leads/Opportunities are available in waiting list search view
* Linked crm.leads are left hanging when waiting_list is deactivated on the event.
* There's actually nothing to transform waiting list leads into attendees.

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
