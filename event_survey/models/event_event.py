# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class Event(models.Model):
    _inherit = 'event.event'

    survey_id = fields.Many2one(
        comodel_name='survey.survey',
        string='Survey',
        copy=False,
    )

    @api.multi
    def action_open_survey(self):
        self.ensure_one()
        if self.survey_id:
            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'survey.survey',
                'res_id': self.survey_id.id,
                'view_id': self.env.ref('survey.survey_form').id
            }
