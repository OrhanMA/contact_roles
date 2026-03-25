from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    contact_role_ids = fields.Many2many(
        "partner.contact.role",
        string="Contact Roles",
    )
    buying_central_id = fields.Many2one(
        "partner.buying.central",
        string="Buying Central",
    )

    @api.onchange("type")
    def _onchange_type_force_delivery_company(self):
        if (
            self.env.context.get("contact_roles_force_delivery_company")
            and self.type == "delivery"
            and self.company_type != "company"
        ):
            self.company_type = "company"
            self.is_company = True
