# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError


class StudentRecord(models.Model):

    _name = 'student.record'
    _rec_name = 'student_name'

    roll_no = fields.Char(string='Student Roll No', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: ('New'))
    student_name = fields.Char(string='Name',required=True)
    last_name = fields.Char(string="Last Name",required=True)
    student_photo = fields.Binary(string="Photo")
    student_age = fields.Integer(string="Age")
    student_dob = fields.Date(string="Date of Birth")
    student_gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    student_blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
       ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],string='Blood Group')
    #profesor_ids = fields.One2many('profesor.record','student_id',string="Profesor")
    student_email = fields.Char(string='Student Email')
    profesor_id = fields.Many2one('profesor.record',string="Profesor")
    subject_ids = fields.Many2many('subject.record','subject_table','sub_id','sub_name')
    school_name = fields.Char(string='School')
    
    @api.model
    def create(self, vals):
        if vals.get('roll_no', ('New')) == ('New'):
            vals['roll_no'] = self.env['ir.sequence'].next_by_code('student.record') or ('New')
            vals['school_name'] = 'L.J School'
        result = super(StudentRecord, self).create(vals)
        return result

    def write(self, values):
        super(StudentRecord, self).write(values)
        print('\n\n\n ',values)
        if 'student_email' in values:
            raise UserError(("You cannot change email of a student."))
        
