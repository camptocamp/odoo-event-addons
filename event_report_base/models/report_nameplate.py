# Copyright 2018 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models


def gen_chunks(iterable, chunksize=10):
    """Chunk generator.

    Take an iterable and yield `chunksize` sized slices.
    """
    chunk = []
    for i, line in enumerate(iterable):
        if i % chunksize == 0 and i > 0:
            yield chunk
            del chunk[:]
        chunk.append(line)
    yield chunk


class ReportNameplate(models.AbstractModel):
    _name = "report.event_report_base.event_nameplate"

    def get_report_values(self, docids, data=None):
        data = dict(data or {})
        records = self.env["event.registration"].browse(docids)
        # group attendees: 2 per each page
        data.update({"pages": gen_chunks(records, chunksize=2)})
        return data
