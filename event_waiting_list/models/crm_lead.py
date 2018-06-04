# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class CrmLead(models.Model):

    _inherit = 'crm.lead'

    event_id = fields.Many2one(
        'event.event',
        readonly=True,
        ondelete='cascade'
    )
    type = fields.Selection(
        selection_add=[('event_waiting_list', 'Event Waiting list')],
    )

    def website_form_input_filter(self, request, values):
        """Define lead's name as 'firstname lastname' for waiting list."""
        res = super().website_form_input_filter(request, values)
        if (
                not res.get('name') and
                request.params.get('type') == 'event_waiting_list'
        ):
            complete_name = '{} {}'.format(
                request.params.get('firstname'),
                request.params.get('lastname'))
            res['name'] = complete_name
        return res
