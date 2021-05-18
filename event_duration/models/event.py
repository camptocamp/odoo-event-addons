# Copyright 2018 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class Event(models.Model):
    _inherit = "event.event"

    one_day = fields.Boolean(
        compute="_compute_one_day",
        help="Tech field to state if the event happens on 1 day only.",
    )

    @api.depends("date_begin", "date_end")
    def _compute_one_day(self):
        for event in self:
            if not event.date_begin or not event.date_end:
                continue
            event.one_day = event.date_begin.date() == event.date_end.date()
