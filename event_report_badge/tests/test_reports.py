# Copyright 2021 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

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
