
from datetime import  datetime

from odoo import api, fields, models

from dateutil.relativedelta import relativedelta

from odoo.exceptions import ValidationError

class ProjectProject(models.Model):
    """docstring for ProjectProject"models.Model def __init__(self, arg):
        super(ProjectProject,models.Model.__init__()
        self.arg = arg"""

    _inherit = 'project.project'

    end_day = fields.Date(string='End date', default=datetime.today())
    number_of_days = fields.Integer(string='Number of Days',
        compute='_calculate_number_of_day', store=True)

    @api.depends('create_date', 'end_day')
    def _calculate_number_of_day(self):
        create = self.create_date
        end = self.end_day
        result = relativedelta(end, create)
        age = int(result.days)
        print('\n-----------age-------------\n', age)
        self.number_of_days = age
