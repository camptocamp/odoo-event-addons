# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class LeadEventConfirm(models.TransientModel):

    _name = 'event.event.leadconfirm'

    def _get_current_lead_event(self):
        return self.env['event.event'].search([('lead_event', '=', True)])

    old_lead_id = fields.Many2one(
        comodel_name='event.event',
        string='Current Lead Event',
        readonly=True,
        default=lambda self: self._get_current_lead_event(),
    )
    event_id = fields.Many2one(
        comodel_name='event.event',
        string='New Lead Event',
        readonly=True,
    )

    def set_lead_event(self):
        if self.old_lead_id and self.old_lead_id != self.event_id:
            self.old_lead_id.toggle_lead_event()
        self.event_id.toggle_lead_event()
        return {'type': 'ir.actions.act_window_close'}
