from odoo import fields, models, api

class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    condition = fields.Boolean(string='Condition')
    team_condition = fields.Char(string='Team condition')

    @api.onchange('condition')
    def check_condition(self):
        if not self.condition:
            self.team_condition = False


    @api.model
    def get_values(self):
        res = super(ResConfigSetting, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        sale_condtion = ICPSudo.get_param('sale.condition')
        res.update(condition=sale_condtion)
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSetting, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param("sale.condition", self.condition)

