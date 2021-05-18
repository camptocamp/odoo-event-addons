# Copyright 2018 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Event Report Badge Barcode EE",
    "summary": "Integrate `event_barcode` from Odoo enterprise",
    "version": "13.0.1.0.0",
    "author": "Camptocamp",
    "license": "LGPL-3",
    "category": "Others",
    "depends": [
        "event_report_badge",
        # Enteprise
        "event_barcode",
    ],
    "website": "https://github.com/camptocamp/odoo-event-addons",
    "data": [
        # Template
        "templates/event_badge.xml",
    ],
    "installable": True,
}
