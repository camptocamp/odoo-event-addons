# Copyright 2021 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from lxml import html

from .common import EventCommonCase


class EventReportsTest(EventCommonCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner2 = cls.env.ref("base.res_partner_1")
        cls.partner3 = cls.env.ref("base.res_partner_4")
        cls.attendee1 = cls._create_attendee(cls, name="Att One")
        cls.attendee2 = cls._create_attendee(
            cls, name="Att Two", partner_id=cls.partner2.id,
        )
        cls.attendee3 = cls._create_attendee(
            cls, name="Att Three", partner_id=cls.partner3.id,
        )
        cls.all_attendees = cls.attendee1 + cls.attendee2 + cls.attendee3

    def _test_nameplates(self, attendees, nameplates):
        for attendee, nameplate in zip(attendees, nameplates):
            # for each attendee we get 2 sides for nameplate
            flipped, vertical = nameplate.getchildren()
            h1, h2 = flipped.getchildren()
            self.assertEqual(h1.text_content().strip(), attendee.name)
            self.assertEqual(h2.text_content().strip(), attendee.partner_id.name)
            h1, h2 = vertical.getchildren()
            self.assertEqual(h1.text_content().strip(), attendee.name)
            self.assertEqual(h2.text_content().strip(), attendee.partner_id.name)

    def test_nameplate(self):
        xid = "event_report_base.report_event_nameplate"
        model = "report.event_report_base.event_nameplate"
        report_helper = self.env[model]
        data = report_helper.get_report_values(self.all_attendees.ids)
        report_html = self._render_report(xid, data)
        node = html.fragments_fromstring(report_html)[0]
        pages = node.xpath("//div[contains(@class, 'nameplates')]")
        self.assertEqual(len(pages), 2)
        # Page one should contain 2 nameplates
        nameplates = pages[0].getchildren()
        self.assertEqual(len(nameplates), 2)
        self._test_nameplates(self.all_attendees[:-1], nameplates)
        # Page two should contain 1 nameplate
        nameplates = pages[1].getchildren()
        self.assertEqual(len(nameplates), 1)
        self._test_nameplates(self.all_attendees[-1], nameplates)
