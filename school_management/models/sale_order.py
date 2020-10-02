from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_age = fields.Integer(string="Customer age")
