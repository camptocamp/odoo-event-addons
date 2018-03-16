# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api, _


class EventRegistrationMassConfirm(models.TransientModel):

    _name = "event.registration.massconfirm"

    @api.multi
    def confirm_registrations(self):
        """Validate selected registrations."""
        context = dict(self.env.context or {})
        active_ids = context.get('active_ids', []) or []

        registrations = self.env['event.registration'].browse(active_ids)

        if len(registrations) > 0:
            registrations.confirm_registration()

        return {'domain': "[('id', 'in', %s)]" % registrations.ids,
                'name': _("Mass confirmed registrations"),
                'auto_search': True,
                'res_model': 'event.registration',
                'views': [
                    (self.env.ref('event.view_event_registration_tree').id, 'tree')],
                'search_view_id': False,
                'type': 'ir.actions.act_window'
                }
