from odoo import fields, models

class SubjectRecord(models.Model):
	_name = "subject.record"
	subject_name = fields.Char(sting="Name")
	subject_details = fields.Char(string="Details")
