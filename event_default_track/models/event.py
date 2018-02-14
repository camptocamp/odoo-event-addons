from odoo import models, api


class Event(models.Model):

    _inherit = "event.event"

    @api.model
    def create(self, vals):
        rec = super().create(vals)
        if not self.env.context.get('skip_default_track_create'):
            rec.create_track()
        return rec

    def _get_track_data(self):
        """Get necessary data to create Track for Event."""
        data = {}
        data['event_id'] = self.id
        data['name'] = self.name
        return data

    def create_track(self):
        """Create default track for current event and return it."""
        self.ensure_one()
        data = self._get_track_data()
        return self.env['event.track'].create(data)
