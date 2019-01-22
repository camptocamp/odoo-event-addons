# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Event survey',
    'summary': 'Event survey customizations',
    'version': '11.0.1.0.0',
    'author': 'Camptocamp, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'category': 'Others',
    'depends': [
        'survey',
        'event',
    ],
    'website': 'https://github.com/camptocamp/odoo-event-addons',
    'data': [
        'wizard/event_survey_generator_view.xml',
        'views/event_survey.xml',
        'views/event_event.xml',
    ],
    'installable': True,
}
