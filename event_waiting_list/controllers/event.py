# -*- coding: utf-8 -*-
# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import http


class EventWaitingListRegister(http.Controller):

    @http.route([
        '/event/<model("event.event"):event>/waiting_list_registration',
    ], type='http', auth='public', website=True)
    def event_register_waiting_list(self, event, **kwargs):
        waiting_list_reg_template = 'event_waiting_list.' \
                                    'event_waiting_list_registration'
        values = {
            'type': 'event_waiting_list',
            'event_id': event.id,
        }
        kwargs.update({'values': values})
        return http.request.render(waiting_list_reg_template, kwargs)
