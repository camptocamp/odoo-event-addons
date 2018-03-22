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
        attachment=True,
        store=True,
    )
    lead_image_medium = fields.Binary(
        string="Medium Lead Image",
        compute="_compute_images",
        attachment=True,
        store=True,
    )
    lead_image_small = fields.Binary(
        string="Small Lead Image",
        compute="_compute_images",
        attachment=True,
        store=True,
    )
    lead_image_thumb = fields.Binary(
        string="Thumb Lead Image",
        compute="_compute_images",
        attachment=True,
        store=True,
    )

    @api.depends("lead_image")
    def _compute_images(self):
        for item in self:
            if not self.env.context.get('bin_size'):
                item.update(item._get_resized_images())
            else:
                # We don't have the images yet so we can't know their size.
                self.lead_image_big = self.lead_image
                self.lead_image_medium = self.lead_image
                self.lead_image_small = self.lead_image
                self.lead_image_thumb = self.lead_image

    def _get_resized_images(self):
        images = {
            'lead_image_big': self._resize_image_big(),
            'lead_image_medium': self._resize_image_medium(),
            'lead_image_small': self._resize_image_small(),
            'lead_image_thumb': self._resize_image_thumb(),
        }
        return images

    def _resize_image_size_map(self, key=None):
        # TODO: make configurable
        mapping = {
            'big': (1600, None),
            'medium': (1024, None),
            'small': (600, None),
            'thumb': (128, None),
        }
        return mapping.get(key, mapping)

    def _resize_image_big(self):
        return tools.image_resize_image(
            self.lead_image,
            size=self._resize_image_size_map('big'),
            avoid_if_small=True
        )

    def _resize_image_medium(self):
        return tools.image_resize_image(
            self.lead_image,
            size=self._resize_image_size_map('medium'),
            avoid_if_small=True
        )

    def _resize_image_small(self):
        return tools.image_resize_image(
            self.lead_image,
            size=self._resize_image_size_map('small'),
            avoid_if_small=True
        )

    def _resize_image_thumb(self):
        return tools.image_resize_image(
            self.lead_image,
            size=self._resize_image_size_map('thumb'),
            avoid_if_small=True
        )

    def lead_image_url(self, size='big'):
        return ('/web/image/{self._name}/'
                '{self.id}/lead_image_{size}').format(self=self, size=size)
