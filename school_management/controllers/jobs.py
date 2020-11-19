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

    MANDETORY_FIELD = ["name", "phone", "email"]

    @http.route('/desig/', auth='public', type='http', website=True)
    def job_designation(self, **kwargs):
        designation_details = request.env['job.designation'].sudo().search([])

        return request.render('school_management.job_designation', {
            'des_details': designation_details})

    @http.route(['/designation/<model("job.designation"):jobs>'], type='http',
                auth='public', website=True)
    def get_click(self, jobs, **kwargs):
        values = {
            'error': {},
            'error_message': [],
            'condition':True
        }
        values.update({'job': jobs.id})
        return request.render(
            'school_management.create_form', values)


    @http.route('/create_job_application', auth='user', type='http',
                website=True)
    def create_application(self, **kwargs):
        values = {
            'error': {},
            'error_message': [],
            'condition': True
        }
        if kwargs and request.httprequest.method == 'POST':
            error, error_message = self.details_form_validate(kwargs)

            values.update({'error': error, 'error_message': error_message})
            values.update(kwargs)
            values.update({'condition' : values.get('error').get('name',False)})
            if not error:
                request.env['job.application'].sudo().create(kwargs)
                # response = request.render("portal.portal_my_details", values)
                return request.render('school_management.thank_you', {})
            else:
                return request.render('school_management.create_form', values)
            # else:
            #     return request.redirect('/jobs')



        # des_id = request.env['job.designation'].sudo().browse(kwargs[
        #     'designation_id'])
        # des_id.sudo().write({'application_ids': [(0, 0, (kwargs))]})


    def details_form_validate(self, data):
        print("\n\n\n----------Hello---------\n\n\n")
        error = dict()
        error_message = []

        # Validation
        for field_name in self.MANDETORY_FIELD:
            print("\n\n\n--------Field_name-------\n\n\n", field_name)
            if not data.get(field_name):
                print("\n\n----missing-----\n\n")
                error[field_name] = 'missing'
        if [err for err in error.values() if err == 'missing']:
            print("\n\n----Required fields are empty------\n\n")
            error_message.append(('Some required fields are empty.'))

        return error, error_message
