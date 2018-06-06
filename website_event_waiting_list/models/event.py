# -*- coding: utf-8 -*-
# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class Event(models.Model):

    _inherit = 'event.event'

    waiting_list_registration_url = fields.Char(
        compute='_compute_waiting_list_registration_url',
    )

    @api.depends('waiting_list')
    def _compute_waiting_list_registration_url(self):
        for event in self:
            if event.waiting_list:
                event.waiting_list_registration_url = \
                    event.website_url + '/waiting-list-registration'
