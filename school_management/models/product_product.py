from odoo import fields,models


class ProductProduct(models.Model):

	_inherit = "product.product" 

	product_short_name=fields.Char(string="Product Short Name")
	product_description = fields.Char(string="Product Description")