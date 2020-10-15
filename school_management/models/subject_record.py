from odoo import fields, models


class SubjectRecord(models.Model):

    _name = "subject.record"
    _rec_name = "subject_name"

    subject_name = fields.Char(sting="Name",required=True)
    subject_details = fields.Char(string="Details")
    profesor_ids = fields.One2many('profesor.record','subject_id',
        string='Profesor')
    profesor_count = fields.Integer(compute='get_profesor_count')


    #function for smart button
    def get_profesor(self):
        return {
            'name' : 'Professor',
            'domain' : [('subject_id', '=' ,self.id)],
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'profesor.record',
            'view_mode': 'tree',
            'view_id': False,

        }

    #function to get profesor count for subject
    def get_profesor_count(self):
        count = self.env['profesor.record'].search_count([
            ('subject_id','=',self.id)])
        self.profesor_count = count
