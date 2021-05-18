# Copyright 2018 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Event Report Base",
    "summary": "Common base for event reports",
    "version": "13.0.1.0.0",
    "author": "Camptocamp",
    "license": "LGPL-3",
    "category": "Others",
    "depends": ["event"],
    "website": "https://github.com/camptocamp/odoo-event-addons",
    "data": [
        # View
        "views/company.xml",
        # Template
        "templates/paper_format.xml",
        "templates/report_logo.xml",
        "templates/misc.xml",
    ],
    "installable": True,
}
