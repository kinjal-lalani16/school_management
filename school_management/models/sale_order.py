from odoo import fields, models
from functools import partial
from odoo.tools.misc import formatLang


class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_age = fields.Integer(string="Customer age")
