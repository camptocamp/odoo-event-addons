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
        for item in self:
            if item.waiting_list:
                item.waiting_list_registration_url = \
                    item.website_url + '/waiting_list_registration'