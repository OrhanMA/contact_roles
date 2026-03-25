{
    "name": "Contact Roles",
    "version": "19.0.1.0.0",
    "license": "LGPL-3",
    "author": "Orhan Madi Assani",
    "category": "Contacts",
    "depends": ["contacts", "sale"],
    "summary": "Manage contact roles and buying centrals on partners",
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
    ],
    "installable": True,
    "application": False,
}
