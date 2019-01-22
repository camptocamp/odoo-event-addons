# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import SavepointCase


class TestEventSurveyTemplate(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.event = cls.env.ref('event.event_0')
        cls.survey = cls.env.ref('survey.feedback_form')
        cls.wiz_model = cls.env['event.survey.generator']

    def test_creating_survey(self):

        self.survey.write({'is_template': True})

        context = {'active_id': self.event.id,
                   'active_model': 'event.event'}

        wizard = self.wiz_model.with_context(context).create({
            'survey_template_id': self.survey.id,
            'survey_title': 'Survey name',
        })
        self.assertFalse(self.event.survey_id)
        wizard.action_generate()

        self.assertTrue(wizard)
        self.assertTrue(self.event.survey_id)
        self.assertEqual(self.event.survey_id.title, 'Survey name')
        self.assertFalse(self.event.survey_id.is_template)

        # all question are properly copied
        self.assertEqual(
            len(self.survey.page_ids.ids),
            len(self.event.survey_id.page_ids.ids))
        self.assertNotEquals(
            self.survey.page_ids.ids,
            self.event.survey_id.page_ids.ids)
        self.assertListEqual(
            self.survey.page_ids.mapped('question_ids.question'),
            self.event.survey_id.page_ids.mapped('question_ids.question'))
