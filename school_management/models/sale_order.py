from odoo import models,fields


class SaleOrder(models.Model):
	_inherit = "sale.order"

	customer_age = fields.Integer(string="Customer age")