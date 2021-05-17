# Copyright 2018 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from collections import defaultdict

from odoo import models


class Event(models.Model):
    _inherit = "event.event"

    def get_tracks_by_days(self, tracks=None):
        self.ensure_one()
        tracks_by_days = defaultdict(list)
        if not tracks:
            tracks = self.env["event.track"].search(
                [("event_id", "=", self.id)], order="date asc"
            )
        else:
            tracks.sorted(key=lambda x: x.date or "")
        for track in tracks:
            key = track.date[:10] if track.date else ""
            tracks_by_days[key].append(track)
        # Workaround: `sorted` is not available in qweb render context
        # hence if you need to render this via qweb you might need this.
        tracks_by_days["__sorted_keys"] = sorted(tracks_by_days.keys())
        return tracks_by_days
