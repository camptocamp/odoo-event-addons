# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Event Waiting list',
    'description': 'Register to Events through waiting list',
    'version': '11.0.1.0.0',
    'author': 'Camptocamp',
    'license': 'AGPL-3',
    'category': 'Others',
    'depends': [
        'crm',
        'event',
    ],
    'website': 'http://www.camptocamp.com',
    'data': [
        'security/ir.model.access.csv',
        'security/rules.xml',
        'views/crm_lead.xml',
        'views/event.xml',
    ],
    'installable': True,
}
