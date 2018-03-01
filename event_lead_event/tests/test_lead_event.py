# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from contextlib import contextmanager

from odoo.exceptions import ValidationError
from odoo.tests.common import SavepointCase


class TestLeadEvent(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.event1 = cls.env['event.event'].create({
            'name': 'Testevent',
            'date_begin': '2018-03-01 10:00:00',
            'date_end': '2018-03-01 11:00:00',
            'lead_event': True,
        })

        cls.event2 = cls.env['event.event'].create({
            'name': 'Testevent',
            'date_begin': '2018-03-01 10:00:00',
            'date_end': '2018-03-01 11:00:00',
        })

    def test_constraint_two_lead_events(self):
        with self.assertRaises(ValidationError):
            self.event2.lead_event = True

    def test_constraint_swap(self):
        msg = 'Lead event constaint unexpectedly prohibited lead event change.'
        with self.assertNotRaises(ValidationError, msg):
            self.event1.lead_event = False
            self.event2.lead_event = True

    def test_lead_event_swap(self):
        event_wizard = self.env['event.event.leadconfirm'].with_context(
            {'active_id': self.event2.id,
             'default_event_id': self.event2.id}).create({})

        event_wizard.set_lead_event()
        self.assertFalse(self.event1.lead_event)
        self.assertTrue(self.event2.lead_event)

    def test_lead_event_set(self):
        self.event1.lead_event = False
        event_wizard = self.env['event.event.leadconfirm'].with_context(
            {'active_id': self.event2.id,
             'default_event_id': self.event2.id}).create({})

        event_wizard.set_lead_event()
        self.assertFalse(self.event1.lead_event)
        self.assertTrue(self.event2.lead_event)

    def test_lead_event_unset(self):
        event_wizard = self.env['event.event.leadconfirm'].with_context(
            {'active_id': self.event1.id,
             'default_event_id': self.event1.id}).create({})
        event_wizard.set_lead_event()
        self.assertFalse(self.event1.lead_event)
        self.assertFalse(self.event2.lead_event)

    def test_constraint_multiple_events(self):
        events = self.env['event.event'].search([('name', '=', 'Testevent')])
        with self.assertRaises(ValidationError):
            events.write({'lead_event': True})

    @contextmanager
    def assertNotRaises(self, exc_type, message=""):
        try:
            yield None
        except exc_type:
            raise self.failureException('{} raised. {}'.format(
                exc_type.__name__, message))
