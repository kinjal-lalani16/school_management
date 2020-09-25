from odoo import fields,models

class DateWizard(models.TransientModel):
	
	_name = 'date.wizard'

	start_date = fields.Date(string="Start date")
	end_date = fields.Date(string="End date")