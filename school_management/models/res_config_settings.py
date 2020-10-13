from odoo import fields, models, api

class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    condition = fields.Boolean(string='Condition')
    team_condition = fields.Char(string='Team condition')
    student_id = fields.Many2one('student.record', string='Student')


    @api.onchange('condition')
    def check_condition(self):
        if not self.condition:
            self.team_condition = False


    @api.model
    def get_values(self):
        res = super(ResConfigSetting, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        sale_condtion = ICPSudo.get_param('sale.condition')
        sale_team_condition = ICPSudo.get_param('sale.team_condition')
        student_id = int(ICPSudo.get_param('school_management.student_id'))
        if student_id and \
                not self.env['student.record'].browse(student_id).exists():
            student_id = False
        res.update(condition=sale_condtion,
            team_condition=sale_team_condition,
            student_id=student_id)
        return res

    # @api.multi
    def set_values(self):
        super(ResConfigSetting, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param("sale.condition", self.condition)
        ICPSudo.set_param("sale.team_condition",self.team_condition)
        ICPSudo.set_param("school_management.student_id", self.student_id.id)


