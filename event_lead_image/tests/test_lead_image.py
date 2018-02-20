from odoo.tests.common import SavepointCase
import os
from base64 import b64encode, b64decode


class TestLeadEvent(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        path = os.path.dirname(__file__) + '/assets/testimage.png'
        with open(path, 'rb') as file_:
            cls.testevent = cls.env['event.event'].create({
                'name': 'Testevent',
                'date_begin': '2018-02-13 08:00:00',
                'date_end': '2018-02-13 10:00:00',
                'lead_image': b64encode(file_.read())
            })

    def test_access_normal(self):
        """Check if we get correct base64 strings back."""
        self.assertTrue(b64decode(self.testevent.lead_image_big))
        self.assertTrue(b64decode(self.testevent.lead_image_medium))
        self.assertTrue(b64decode(self.testevent.lead_image_small))

    def test_access_binsize(self):
        """Test that we don't fail if we're in bin_size mode."""

        # bin_size makes the attachment return its size instead of the
        # actual image data.
        event = self.env['event.event'].with_context(
            bin_size=True).browse(self.testevent.id)

        # Since when our the Images are scaled on access and we haven't
        # accessed them yet we don't know their size so it should be equal
        # to the original.
        self.assertAlmostEqual(self.convert_to_float(event.lead_image),
                               114.59)
        self.assertAlmostEqual(self.convert_to_float(event.lead_image_big),
                               114.59)
        self.assertAlmostEqual(self.convert_to_float(event.lead_image_medium),
                               114.59)
        self.assertAlmostEqual(self.convert_to_float(event.lead_image_small),
                               114.59)

    def convert_to_float(self, size_string):
        return float(size_string.split()[0])
