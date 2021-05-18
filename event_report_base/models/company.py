# Copyright 2018 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    report_logo_big = fields.Binary("Report logo", attachment=True)
