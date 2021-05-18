# Copyright 2021 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import SavepointCase


class EventCommonCase(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.company = cls.env.ref("base.main_company")
        cls.partner = cls.env.ref("base.partner_demo")
        cls.event = cls.env["event.event"].create(
            {
                "name": "Testevent",
                "date_begin": "2021-05-17 10:00:00",
                "date_end": "2021-05-20 16:00:00",
            }
        )

    def _render_report(self, xid, values):
        """Render report and return its HTML."""
        report = self.env.ref(xid)
        return report.render_template(report.report_name, values).decode("utf-8")

    @staticmethod
    def _create_attendee(class_or_instance, **kw):
        vals = {
            "partner_id": class_or_instance.partner.id,
            "event_id": class_or_instance.event.id,
        }
        vals.update(kw)
        return class_or_instance.env["event.registration"].create(vals)
