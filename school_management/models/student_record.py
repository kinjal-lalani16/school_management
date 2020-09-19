# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StudentRecord(models.Model):

    _name = 'student.record'

    student_name = fields.Char(string='Name',required=True)
    last_name = fields.Char(string="Last Name",required=True)
    student_photo = fields.Binary(string="Photo")
    student_age = fields.Integer(string="Age")
    student_dob = fields.Date(string="Date of Birth")
    student_gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    student_blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
       ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],string='Blood Group')