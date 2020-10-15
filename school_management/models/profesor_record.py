from odoo import fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
import re

class profesorRecord(models.Model):

    _name = "profesor.record"
    _rec_name = "profesor_name"

    profesor_name = fields.Char(string="Professor Name", required=True)
    profesor_department = fields.Char(string="Department", required=True)
    profesor_dob = fields.Date(string="Date of Birth",required=True)
    profesor_phone_number = fields.Char(string="Phone Number")
    profesor_age = fields.Integer(string="Age",compute='get_dob',store=True)
    profesor_email = fields.Char(string="E-mail")
    profesor_gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    profesor_blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'),
            ('O+', 'O+ve'), ('AB+', 'AB+ve'), ('A-','A-ve'), ('B-', 'B-ve'),
            ('O-', 'O-ve'), ('AB-', 'AB-ve')], string='Blood Group')
    subject_id = fields.Many2one('subject.record', string="Subject")
    subject_description = fields.Char(related="subject_id.subject_details",
                                      readonly=True)
    student_ids = fields.One2many(
        'student.record', 'profesor_id', string="Student")

    #onchange function to get age through entered dob
    @api.depends('profesor_dob')
    def get_dob(self):
        for record in self:
            if record.profesor_dob:
                date_record = record.profesor_dob
                current_date = date.today()
                result = relativedelta(current_date, date_record)
                age = int(result.years)
                self.profesor_age = age

    #constraint to input valid mobile number
    @api.constrains('profesor_phone_number')
    def check_number(self):
        if self.profesor_phone_number:
            match = re.match(r'[789]\d{9}$',self.profesor_phone_number)
            if match == None:
                raise ValidationError('Not a valid mobile number')

    #constrain for not allowing user to enter current date or future date
    @api.constrains('profesor_dob')
    def validate_dob(self):
        if self.profesor_dob >= (date.today()):
            raise ValidationError("Date you have enter is not valid..!")


    @api.constrains('profesor_email')
    def validate_mail(self):
        if self.profesor_email:
            match = re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
                self.profesor_email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')


