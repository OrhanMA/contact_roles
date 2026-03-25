from odoo import fields, models


class PartnerBuyingCentral(models.Model):
    _name = "partner.buying.central"
    _description = "Buying Central"

    name = fields.Char(required=True)
    description = fields.Text()
