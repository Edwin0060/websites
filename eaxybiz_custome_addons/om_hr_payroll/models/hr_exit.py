
import time

from odoo import models, fields, api, _
from odoo.exceptions import Warning

class hr_exit_process(models.Model):
    _name = 'hr.exit.employee'
    _description = "Exit"
    # _rec_name = 'employee_id'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    # _order = 'id desc'

    employee_id = fields.Many2one('hr.employee', required=True, string="Employee")
    request_date = fields.Date('Request Date', readonly='1',
                               default=fields.datetime.now())
    user_id = fields.Many2one('res.users', string='User',
                              default=lambda self: self.env.user,
                           readonly=True)
    confirm_date = fields.Date(string='Confirm Date(Employee)',
                               readonly=True, copy=False)
    dept_approved_date = fields.Date(string='Approved Date(Department Manager)',
                                     readonly=True, copy=False)
    validate_date = fields.Date(string='Approved Date(HR Manager)',
                                readonly=True, copy=False)
    general_validate_date = fields.Date(string='Approved Date(General Manager)',
                                        readonly=True, copy=False)
    confirm_by_id = fields.Many2one('res.users', string='Confirm By', readonly=True, copy=False)
    dept_manager_by_id = fields.Many2one('res.users', string='Approved By Department Manager', readonly=True,
                                         copy=False)
    hr_manager_by_id = fields.Many2one('res.users', string='Approved By HR Manager', readonly=True, copy=False)
    gen_man_by_id = fields.Many2one('res.users', string='Approved By General Manager', readonly=True, copy=False)
    reason_for_leaving = fields.Char(string='Reason For Leaving', required=True, copy=False, readonly=True)
    last_work_date = fields.Date(string='Last Day of Work')
    # survey = fields.Many2one('survey.survey', string="Interview", readonly=True)
    # response_id = fields.Many2one('survey.user_input', "Response", ondelete="set null", oldname="response")
    # partner_id = fields.Many2one('res.partner', "Contact", readonly=True)

    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('approved_dept_manager', 'Approved by Dept Manager'),
        ('approved_hr_manager', 'Approved by HR Manager'),
        ('approved_general_manager', 'Approved by General Manager'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
        ('reject', 'Rejected')], string='State',
        readonly=True, help='', default='draft',
        track_visibility='onchange')
    notes = fields.Text(string='Notes')
    # manager_id = fields.Many2one('hr.employee', 'Department Manager',
    #                              related='employee_id.department_id.manager_id',
    #                              states={'draft': [('readonly', False)]}, readonly=True, store=True,
    #                              help='This area is automatically filled by the user who \
    #                     will confirm the exit', copy=False)
    # company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)
    # department_id = fields.Many2one(related='employee_id.department_id',
    #                                 string='Department', type='many2one', relation='hr.department',
    #                                 readonly=True, store=True)
    # job_id = fields.Many2one(related='employee_id.job_id',
    #                          string='Job Title', type='many2one', relation='hr.department',
    #                          readonly=True, store=True)
    # checklist_ids = fields.One2many('hr.exit.line', 'exit_id', string="Checklist")
    # contract_id = fields.Many2one('hr.contract', string='Contract', readonly=False)
    # contract_ids = fields.Many2many('hr.contract', 'hr_contract_contract_tag')
