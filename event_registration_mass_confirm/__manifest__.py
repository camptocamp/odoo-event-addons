# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Event registration mass confirm',
    'version': '11.0.1.0.0',
    'category': 'Event',
    'license': 'AGPL-3',
    'author': 'Camptocamp, Odoo Community Association (OCA)',
    'website': 'https://github.com/camptocamp/odoo-event-addons',
    'depends': [
        'event',
        'base'
    ],
    'data': [
        'wizard/confirm_attendees.xml'
    ],
}
