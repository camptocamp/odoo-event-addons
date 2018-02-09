# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Event first name and last name',
    'version': '11.0.1.0.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'author': 'Camptocamp',
    'website': 'https://github.com/camptocamp/odoo-event-addons',
    'depends': [
        'event',
        'partner_firstname',
    ],
    'data': [
        'views/event_registration.xml',
    ],
}
