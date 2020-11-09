from odoo import models

from datetime import date, datetime
#from dateutil.relativedelta import relativedelta

class AccountMove(models.Model):

    _inherit = 'account.move'

    def action_send(self):
        template_id = self.env.ref('school_management.email_record_template').id
        self.env['mail.template'].browse(template_id).send_mail(
            self.id, force_send=True)

    def invoice_reminder(self):
        invoice = self.env['account.move'].search([
            ('type', '=', 'out_invoice'),
            ('state', '=', 'posted'),
            ('amount_residual', '>', 0)])

        for records in invoice:
            if records.invoice_date_due:
                current_date = date.today()
                diff = (records.invoice_date_due - current_date).days
                if diff == 2:
                    records.action_send()
                    print('-------------Email sent-----------')
