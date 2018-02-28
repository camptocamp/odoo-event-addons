# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import _
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Event(models.Model):

    _inherit = "event.event"

    lead_event = fields.Boolean(
        string='Lead Event',
        index=True,
    )

    @api.constrains('lead_event')
    def check_only_one_leadevent(self):
        if self.search_count([('lead_event', '=', True)]) > 1:
            raise ValidationError(_("There can be only one lead event."))

    def toggle_lead_event(self):
        self.ensure_one()
        self.lead_event = not self.lead_event
