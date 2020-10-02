from odoo import fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError


class profesorRecord(models.Model):

    _name = "profesor.record"
    _rec_name = "profesor_name"

    profesor_name = fields.Char(string="Professor Name", required=True)
    profesor_department = fields.Char(string="Department", required=True)
    profesor_age = fields.Integer(string="Age", compute="_get_age")
    profesor_email = fields.Char(string="E-mail")
    profesor_dob = fields.Date(string="Date of Birth")
    profesor_phone_number = fields.Char(string="Phone Number")
    profesor_gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    profesor_blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'),
                                             ('O+', 'O+ve'), ('AB+', 'AB+ve'), ('A-',
                                                                                'A-ve'), ('B-', 'B-ve'),
                                             ('O-', 'O-ve'), ('AB-', 'AB-ve')], string='Blood Group')
    subject_id = fields.Many2one('subject.record', string="Subject")
    subject_description = fields.Char(related="subject_id.subject_details",
                                      readonly=True)
    student_ids = fields.One2many(
        'student.record', 'profesor_id', string="Student")

    @api.depends('profesor_dob')
    def _get_age(self):
        for record in self:
            if record.profesor_dob:
                date_record = record.profesor_dob
                current_date = date.today()
                result = relativedelta(current_date, date_record)
                record.profesor_age = int(result.years)

    @api.constrains('profesor_phone_number')
    def check_phone_number(self):
        if self.profesor_phone_number:
        	match = re.match("^[a-zA-Z]+$")
        	if match == None:
        		raise ValidationError('Entered number is wrong..!')
