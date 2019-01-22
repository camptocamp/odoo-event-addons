# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class Survey(models.Model):
    _inherit = 'survey.survey'

    is_template = fields.Boolean(
        string="Survey template",
        help="Allows to re-use a survey as a template to create new ones",
        copy=False,
    )
