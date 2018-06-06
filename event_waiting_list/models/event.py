# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class Event(models.Model):

    _inherit = 'event.event'

    waiting_list = fields.Boolean('Manage waiting list')
    waiting_list_lead_ids = fields.One2many(
        'crm.lead',
        domain=[('type', '=', 'event_waiting_list')],
        inverse_name='event_id',
    )
    waiting_list_count = fields.Integer(compute='_compute_waiting_list_count')

    @api.multi
    def _compute_waiting_list_count(self):
        for event in self:
            event.waiting_list_count = len(event.waiting_list_lead_ids)
