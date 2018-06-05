# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields


class CrmLead(models.Model):

    _inherit = 'crm.lead'

    event_id = fields.Many2one(
        'event.event',
        readonly=True,
        ondelete='cascade'
    )
    type = fields.Selection(
        selection_add=[('event_waiting_list', 'Event Waiting list')],
    )

