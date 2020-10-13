# -*- coding: utf-8 -*-

import re
from datetime import date

from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class StudentRecord(models.Model):

    _name = 'student.record'
    _rec_name = 'student_name'

    roll_no = fields.Char(string='Student Roll No', required=True, copy=False,
    readonly=True, states={'draft': [('readonly', False)]}, index=True,
    default=lambda self: ('New'))

    student_name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string="Last Name", required=True)
    student_photo = fields.Binary(string="Photo")
    student_age = fields.Integer(string="Age",store=True)
    student_dob = fields.Date(string="Date of Birth")
    school_type = fields.Selection([('public', 'Public School'),
                                    ('private', 'Private School')])
    auto_rank = fields.Integer(compute="_auto_rank", string="Rank")
    student_gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    student_blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'),
        ('O+', 'O+ve'), ('AB+', 'AB+ve'),('A-', 'A-ve'), ('B-', 'B-ve'),
        ('O-', 'O-ve'), ('AB-', 'AB-ve')], string='Blood Group')
    student_email = fields.Char(string='Student Email')
    profesor_id = fields.Many2one('profesor.record', string="Profesor")
    gender = fields.Selection(related="profesor_id.profesor_gender",readonly=True)
    subject_ids = fields.Many2many(
        'subject.record', 'subject_table', 'sub_id', 'sub_name')
    school_name = fields.Char(string='School')
    sale_id = fields.Many2one('sale.order', string="Sale Order")

    def number_count(self):
        return {
            'name' : 'Profesor',
            'domain' : [('profesor_id', '=' ,self.id)],
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'profesor.record',
            'view_mode': 'tree',
            'view_id': False,

        }

    @api.onchange('student_dob')
    def get_age(self):
        for record in self:
            if record.student_dob:
                date_record = record.student_dob
                current_date = date.today()
                result = relativedelta(current_date, date_record)
                age = int(result.years)
                record.student_age = age

    @api.constrains('student_email')
    def validate_mail(self):
        if self.student_email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.student_email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')

    @api.constrains('student_dob')
    def validate_dob(self):
        if self.student_dob >= (date.today()):
            raise ValidationError("Date you have enter is not valid..!")


    @api.model
    def create(self, vals):
        if vals.get('roll_no', ('New')) == ('New'):
            vals['roll_no'] = self.env['ir.sequence'].next_by_code(
                'student.record') or ('New')
            vals['school_name'] = 'L.J School'

        result = super(StudentRecord, self).create(vals)
        # search method
        student_female = self.env['student.record'].search(
            [('student_gender', '=', 'f')])
        print(student_female)
        student_male = self.env['student.record'].search(
            [('student_gender', '=', 'm'), ('student_age', '=', 15)])
        print("\n\n\n\n\t\t\t\t", student_male)
        profesor_bg = self.env['profesor.record'].search(
            [('profesor_blood_group', '=', 'AB+')])
        print("\n\n\n\n", profesor_bg)
        # browse method
        student_browse = self.env['student.record'].browse(27).exists()
        print("\n\n\n", student_browse)
        # exists method
        if student_browse.exists():
            print("\n \n \nId exists in database")
        else:
            print("\n \n \nid does not exist in database")
        # search_count()
        student_count = self.env['student.record'].search_count([])
        print("number of student is : ", student_count)
        # ref method
        sale_xml = self.env.ref(
            'school_management.profesor_record_form_view').id
        print("\n \n sale id is", sale_xml)

        # unlink

        return result

        def write(self, values):
            super(StudentRecord, self).write(values)
            # print('\n\n\n ',values)

            if 'student_email' in values:
                raise UserError("You cannot change email of a student.")
            unlink_record = self.env['student.record'].browse(27)
            unlink_record.unlink()

    @api.depends('school_type')
    def _auto_rank(self):
        for r in self:
            if r.school_type == "private":
                r.auto_rank = 50
            elif r.school_type == "public":
                r.auto_rank = 100
            else:
                r.auto_rank == 0
