# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class CrmLead(models.Model):

    _inherit = 'crm.lead'

    event_id = fields.Many2one(
        'event.event',
        ondelete='cascade',
        domain=[('waiting_list', '=', True)],
    )
    type = fields.Selection(
        selection_add=[('event_waiting_list', 'Event Waiting list')],
    )

    @api.constrains('type', 'event_id')
    def _check_type_event(self):
        for lead in self:
            if lead.type != 'event_waiting_list':
                continue
            if not lead.event_id:
                raise ValidationError(_(
                    'Event is required if the lead is of waiting_list type.'))
            if not lead.event_id.waiting_list:
                raise UserError(_(
                    'The event must have waiting list activated to be used '
                    'here.'))
