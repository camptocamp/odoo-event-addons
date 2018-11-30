# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import http


class EventWaitingListRegister(http.Controller):

    @http.route([
        '/event/<model("event.event"):event>/waiting-list-registration',
    ], type='http', auth='public', website=True, sitemap=False)
    def event_register_waiting_list(self, event, **kwargs):
        if not event.waiting_list:
            raise http.request.not_found()
        waiting_list_reg_template = 'website_event_waiting_list.' \
                                    'event_waiting_list_registration'

        kwargs.update({
            'lead_type': 'event_waiting_list',
            'event': event,
            'event_id': event.id,
        })
        return http.request.render(waiting_list_reg_template, kwargs)

    @http.route([
        '/event/<model("event.event"):event>/waiting-list-confirmation',
    ], type='http', auth='public', website=True, sitemap=False)
    def event_waiting_list_confirmation(self, event, **kwargs):
        if not event.waiting_list:
            raise http.request.not_found()
        waiting_list_confirmation_template = 'website_event_waiting_list.' \
                                             'event_waiting_list_confirmation'
        kwargs.update({
            'event': event,
            'event_id': event.id,
        })
        return http.request.render(waiting_list_confirmation_template, kwargs)
