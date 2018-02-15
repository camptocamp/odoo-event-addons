# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class EventRegistration(models.Model):

    _inherit = "event.registration"

    firstname = fields.Char(
        string="Firstname",
        related="partner_id.firstname",
        readonly=True,
        store=True,
        index=True,
    )
    lastname = fields.Char(
        string="Lastname",
        related="partner_id.lastname",
        readonly=True,
        store=True,
        index=True,
    )
    name = fields.Char(
        string="Name",
        related="partner_id.name",
        readonly=True,
        store=True
    )
