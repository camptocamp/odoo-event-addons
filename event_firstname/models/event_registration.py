import logging
from odoo import models, fields, api


_logger = logging.getLogger(__name__)


class EventRegistration(models.Model):

    _inherit = "event.registration"

    firstname = fields.Char(string="Firstname",
                            related='partner_id.firstname',
                            readonly=True,
                            store=True)
    lastname = fields.Char(string="Lastname",
                           related='partner_id.lastname',
                           readonly=True,
                           store=True)

    name = fields.Char(string="Name",
                           related='partner_id.name',
                           readonly=True,
                           store=True)
