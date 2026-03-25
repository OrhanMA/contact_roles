from odoo import fields, models


class PartnerContactRole(models.Model):
    _name = "partner.contact.role"
    _description = "Partner Contact Role"

    name = fields.Char(required=True)
    description = fields.Text()
