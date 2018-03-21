from odoo.tests.common import SavepointCase
from odoo.exceptions import UserError


class TestMassConfirm(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.testevent = cls.env['event.event'].create({
            'name': 'Testevent',
            'date_begin': '2018-02-13 08:00:00',
            'date_end': '2018-02-13 10:00:00',
            'auto_confirm': False
        })
        cls.admin = cls.env.ref('base.user_root')
        cls.demo_user = cls.env.ref('base.user_demo')
        cls.snddemo_user = cls.env.ref('base.demo_user0')

        cls.reg1 = cls.env['event.registration'].create({
            'event_id': cls.testevent.id,
            'partner_id': cls.admin.partner_id.id,
        })
        cls.reg2 = cls.env['event.registration'].create({
            'event_id': cls.testevent.id,
            'partner_id': cls.demo_user.partner_id.id,
        })
        cls.reg3 = cls.env['event.registration'].create({
            'event_id': cls.testevent.id,
            'partner_id': cls.snddemo_user.partner_id.id,
        })

    def test_wizard_success(self):
        wizard = self.env['event.registration.massconfirm'].with_context(
            {'active_ids': [self.reg1.id, self.reg2.id]}).create({})
        wizard.confirm_registrations()

        self.assertEqual(self.reg1.state, 'open')
        self.assertEqual(self.reg2.state, 'open')
        self.assertEqual(self.reg3.state, 'draft')

    def test_wizard_no_ids(self):
        wizard = self.env['event.registration.massconfirm'].with_context(
            {'active_ids': []}).create({})
        with self.assertRaises(UserError):
            wizard.confirm_registrations()

    def test_wizard_success_domain(self):
        wizard = self.env['event.registration.massconfirm'].with_context(
            {'active_ids': [self.reg1.id, self.reg2.id]}).create({})
        value = wizard.confirm_registrations()
        self.assertEqual(
            value['domain'],
            "[('id', 'in', [%i, %i])]" % (self.reg1.id, self.reg2.id)
        )
