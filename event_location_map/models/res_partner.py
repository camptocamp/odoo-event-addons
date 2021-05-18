# Copyright 2018 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models

# TODO: migrate and use this instead of normal binary field
# from odoo.addons.base_binary_validation.fields import BinaryValidated


class ResPartner(models.Model):

    _inherit = "res.partner"

    location_map_image = fields.Binary(
        string="Event location map",
        help="Image ratio must be around 3.3. For instance: ~720x220",
        attachment=True,
        # BinaryValidated required
        # allowed_mimetypes=('image/jpeg', 'image/png'),
    )
