# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models, _


class EventSurveyGenerator(models.TransientModel):

    _name = 'event.survey.generator'

    survey_template_id = fields.Many2one(
        comodel_name='survey.survey',
        required=True,
        domain=[('is_template', '=', True)]
    )
    survey_title = fields.Char(
        string="Survey name",
    )
    event_id = fields.Many2one(
        comodel_name='event.event',
        default=lambda self: self._default_event(),
        required=True
    )

    def _default_event(self):
        return self.env['event.event'].browse(self.env.context.get(
            'active_id'))

    def action_generate(self):
        """Create survey from survey template """
        self.ensure_one()
        new_survey = self.survey_template_id.copy()

        # title - html field couldn't be rewrite w/ default, write directly
        new_survey.write({'title': self.survey_title})

        self.event_id.write({'survey_id': new_survey.id})
        msg = '{}<a href="#"  data-oe-model="survey.survey" ' \
              'class="o_channel_redirect" data-oe-id="{}">{}</a>'.format(
                  _('Created from template: '),
                  self.survey_template_id.id,
                  self.survey_template_id.title,)

        new_survey.message_post(body=msg, type='comment')

        return {'type': 'ir.actions.act_window_close'}
