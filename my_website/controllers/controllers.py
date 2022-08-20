# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import requests


class WelcomeWebsite(http.Controller):

    # @http.route('/add/value/sum', auth='public', website=True)
    # def employee_js_connect(self,**kw):
    #     print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' ,kw)

    @http.route('/student', auth='public', website=True)
    def list(self, **kw):
        return request.render('my_website.website_page_template', {
            'country': request.env['res.country'].search([]),
            'state': request.env['res.country.state'].search([]),
        })

    @http.route('/employee/info', type="http", methods=["POST"], auth='none', csrf=False, website=True)
    def weather_info_two(self, **kw):
        name = kw.get('name')
        job_position = kw.get('job_position')
        email = kw.get('email_input')
        # state = kw.get('state')
        # country = kw.get('country_id')

        vals = {
            'name': name,
            'function': job_position,
            'email': email,
            # 'state_id': state,
            # 'country_id': country,
        }
        request.env['res.partner'].sudo().create(vals)
        return

    @http.route('/my_website/objects', auth='public', website=True)
    def student_profile_create(self, **kw):
        return request.render('my_website.student_profile', {
            'objects': request.env['res.partner'].search([]),
        })
