# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Website Event Waiting list',
    'summary': 'Register to Events through waiting list using website',
    'version': '11.0.1.1.0',
    'author': 'Camptocamp, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'category': 'Others',
    'depends': [
        'event_waiting_list',
        'website_event',
        'website_form',
        # website_crm is added here to ensure overrides are called
        # correctly. We don't really want it, but it's autoinstall=True,
        # and website_partner is a dependency of website_event.
        'website_crm',
    ],
    'website': 'http://www.camptocamp.com',
    'data': [
        'data/website_form.xml',
        'views/crm_lead_views.xml',
        'templates/waiting_list_registration.xml',
    ],
    'installable': True,
    'auto-install': True,
}
