from odoo.tests.common import SavepointCase


class TestDefaultTrackEvent(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.default_event = cls.env['event.event'].with_context(
            skip_default_track_create=True).create({
                'name': 'Default Event',
                'date_begin': '2018-02-13 08:00:00',
                'date_end': '2018-02-13 10:00:00'
            })

    def test_data_get(self):
        data = self.default_event._get_track_data()
        self.assertEqual(len(data.keys()), 2)
        self.assertEqual(data['name'], 'Default Event')
        self.assertEqual(data['event_id'], self.default_event.id)

    def test_create_track(self):
        track = self.default_event.create_track()
        self.assertEqual(track.name, 'Default Event')
        self.assertEqual(track.event_id, self.default_event)

    def test_patched_create(self):
        event = self.env['event.event'].create({
            'name': 'Testevent',
            'date_begin': '2018-02-13 08:00:00',
            'date_end': '2018-02-13 10:00:00'
        })
        self.assertEqual(event.name, 'Testevent')
        self.assertEqual(len(event.track_ids), 1)

        track = event.track_ids[0]
        self.assertEqual(track.name, 'Testevent')
