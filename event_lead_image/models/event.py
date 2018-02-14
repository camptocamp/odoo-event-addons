from odoo import models, fields, tools, api


class Event(models.Model):

    _inherit = "event.event"

    lead_image = fields.Binary(
        "Lead Image",
        attachment=True,
    )
    lead_image_big = fields.Binary(
        "Big Lead Image",
        compute="_compute_images",
    )
    lead_image_medium = fields.Binary(
        string="Medium Lead Image",
        compute="_compute_images",
    )
    lead_image_small = fields.Binary(
        string="Small Lead Image",
        compute="_compute_images",
    )

    @api.depends("lead_image")
    def _compute_images(self):
        for item in self:
            if not self._context.get('bin_size'):
                item.update(item._get_resized_images())
            else:
                self.lead_image_big = self.lead_image
                self.lead_image_medium = self.lead_image
                self.lead_image_small = self.lead_image

    def _get_resized_images(self):
        images = tools.image_get_resized_images(
            self.lead_image,
            big_name="lead_image_big",
            medium_name="lead_image_medium",
            small_name="lead_image_small",
            return_big=True)
        return images
