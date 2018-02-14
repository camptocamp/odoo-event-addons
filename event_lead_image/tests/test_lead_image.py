from odoo.tests.common import SavepointCase
import os
from base64 import b64encode, b64decode


class TestLeadEvent(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        path = os.path.dirname(__file__) + '/assets/testimage.png'
        file_ = open(path, 'rb')

        cls.testevent = cls.env['event.event'].create({
            'name': 'Testevent',
            'date_begin': '2018-02-13 08:00:00',
            'date_end': '2018-02-13 10:00:00',
            'lead_image': b64encode(file_.read())
        })

    def test_access_normal(self):
        b64decode(self.testevent.lead_image_big)
        b64decode(self.testevent.lead_image_medium)
        b64decode(self.testevent.lead_image_small)

    def test_access_binsize(self):
        event = self.env['event.event'].with_context(
            bin_size=True).browse(self.testevent.id)
        self.assertEqual(event.lead_image, '114.59 Kb')
        self.assertEqual(event.lead_image_big, '114.59 Kb')
        self.assertEqual(event.lead_image_medium, '114.59 Kb')
        self.assertEqual(event.lead_image_small, '114.59 Kb')
