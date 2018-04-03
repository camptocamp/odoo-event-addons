# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class EventRegistration(models.Model):

    _inherit = "event.registration"

    firstname = fields.Char(
        string="Firstname",
        index=True,
    )
    lastname = fields.Char(
        string="Lastname",
        index=True,
    )
    name = fields.Char(
        string="Name",
        compute="_compute_name",
        readonly=True,
        store=True
    )

    @api.depends('lastname', 'firstname')
    def _compute_name(self):
        for item in self:
            name = [item[fname].strip()
                    for fname in ('firstname', 'lastname')
                    if item[fname] and item[fname].strip()]
            item.name = ' '.join(name)
