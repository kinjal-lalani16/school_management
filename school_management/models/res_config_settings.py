from odoo import fields, models, api


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    condition = fields.Boolean(string='Condition')
    team_condition = fields.Char(string='Team condition')
    #sale_id = fields.Many2one('sale.order',string='Sale order')
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
        student_id = int(ICPSudo.get_param('school_management.student_id',
                                       default='False'))
        if student_id and \
                not self.env['student.record'].browse(student_id).exists():
            student_id = False
        res.update(
            condition=sale_condtion,
            student_id=student_id
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSetting, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param("sale.condition", self.condition)
        ICPSudo.set_param("school_management.student_id", self.student_id.id)
