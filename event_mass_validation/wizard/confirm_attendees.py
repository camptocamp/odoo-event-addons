# -*- coding: utf-8 -*-
# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api


class ConfirmEventRegistrations(models.TransientModel):

    _name = "event.registration.massvalidation"

    @api.multi
    def validate_registrations(self):
        """Validate selected registrations."""
        context = dict(self.env.context or {})
        active_ids = context.get('active_ids', []) or []

        registrations = self.env['event.registration'].browse(active_ids)

        registrations.confirm_registration()

        return {'type': 'ir.actions.act_window_close'}
