# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Lead Event',
    'summary': 'Allows the definition of a lead event.',
    'version': '11.0.1.0.2',
    'author': 'Camptocamp, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'category': 'Others',
    'website': 'https://github.com/camptocamp/odoo-event-addons',
    'depends': [
        'event',
        'website_event_track',
    ],
    'data': [
        'wizard/lead_event.xml',
        'views/event_views.xml',
    ],
    'installable': True,
}
