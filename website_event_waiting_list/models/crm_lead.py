# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class CrmLead(models.Model):

    _inherit = 'crm.lead'

    attendees_number = fields.Integer()

    def website_form_input_filter(self, request, values):
        """Define lead's name as 'firstname lastname' for waiting list."""
        res = super().website_form_input_filter(request, values)
        if request.params.get('type') == 'event_waiting_list':
            complete_name = '{} {}'.format(
                request.params.get('firstname').strip(),
                request.params.get('lastname').strip())
            res['contact_name'] = complete_name
            res['name'] = complete_name
        return res
