# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class LeadEventConfirm(models.TransientModel):
    """Provide the fields for our wizard.

    It is used to change the Lead Event flag on the current Event.
    """

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
    same_event = fields.Boolean(
        compute='_compute_same_event'
    )

    @api.depends('event_id', 'old_lead_id')
    def _compute_same_event(self):
        """Calculate if both events are the same.

        We need this, since we remove the flag completely
        if they are and want to reflect this in the ui.
        """
        for item in self:
            item.same_event = item.old_lead_id == item.event_id

    def set_lead_event(self):
        """Perform the swap of swap of the Lead event."""
        if self.old_lead_id and self.old_lead_id != self.event_id:
            self.old_lead_id.toggle_lead_event()
        self.event_id.toggle_lead_event()
        return {'type': 'ir.actions.act_window_close'}
