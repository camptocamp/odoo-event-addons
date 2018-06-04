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
        'website_form',
        # website_crm is added here to ensure overrides are called
        # correctly. We don't really want it, but it's autoinstall=True,
        # and website_partner is a dependency of website_event.
        'website_crm',
    ],
    'website': 'http://www.camptocamp.com',
    'data': [
        'data/website_form.xml',
        'templates/waiting_list_registration.xml',
        'views/crm_lead.xml',
        'views/event.xml',
    ],
    'installable': True,
}
