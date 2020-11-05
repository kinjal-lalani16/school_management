from odoo import http
from odoo.http import request

class Job(http.Controller):

    @http.route('/jobs/', auth='public', type='http', website=True)
    def job_application_details(self, **kwargs):
        job_application_details = request.env['job.application'].sudo().search(
            [])
        return request.render('school_management.job_details', {
            'details': job_application_details})

class desigantion(http.Controller):

    @http.route('/desig/', auth='public', type='http', website=True)
    def job_designation(self, **kwargs):
        designation_details = request.env['job.designation'].sudo().search([])

        return request.render('school_management.job_designation', {
            'des_details': designation_details})

    @http.route(['/designation/<model("job.designation"):jobs>'], type='http', auth='public', website=True)
    def get_click(self, jobs, **kwargs):
        print('\n\n----------jobs-----------', jobs)
        return request.render('school_management.create_form', {})

    @http.route('/create_job_application', auth='public', type='http', website=True)
    def create_application(self, **kwargs):
        request.env['job.application'].sudo().create(kwargs)
        print('\n\n\n---------Args----------\n\n\n', kwargs)
        return request.render('school_management.thank_you', {})
