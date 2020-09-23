from odoo import models, fields


class ProfesorRecord(models.Model):
	_name = "profesor.record"

	profesor_name = fields.Char(string="Professor Name",required=True)
	profesor_department = fields.Char(string="Department",required=True)
	profesor_subject = fields.Char(string="Subject",required=True)
	profesor_age = fields.Integer(string="Age")
	profesor_email = fields.Char(string="E-mail")
	profesor_dob = fields.Date(string="Date of Birth")
	profesor_phone_number = fields.Char(string="Phone Number")
	profesor_gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
	profesor_blood_group = fields.Selection([('A+', 'A+ve'),('B+', 'B+ve'),('O+', 'O+ve'),('AB+', 'AB+ve'),
 			('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],string='Blood Group')
    
	