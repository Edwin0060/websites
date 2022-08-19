# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
from datetime import timedelta, date, datetime
from odoo.tools import float_compare, float_round, float_repr

from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT


def time_to_float(t):
    return float_round(t.hour + t.minute / 60 + t.second / 3600, precision_digits=2)


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    parent_id = fields.Many2one(related='employee_id.parent_id', string='Reporting Head')
    employee_work_hour_time = fields.Float(string="Diff Hour's")
    total_work_hour_time = fields.Float(string="Office Hour's")
    checkin_time = fields.Float(string="Check in Time")
    checkout_time = fields.Float(string="Check Out Time")
    employee_checkin_time = fields.Float(string="Office Check In")
    employee_checkout_time = fields.Float(string="Office Check Out")
    diff_check_in_time = fields.Float(string="Check In Diff")
    diff_check_out_time = fields.Float(string="Check out Diff")

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if 'team_attendance' in self.env.context and self.env.context['team_attendance']:
            res_user = self.env['res.users'].sudo().search([('id', '=', self.env.uid)])
            emp_id = self.env['hr.employee'].search([('user_id', '=', res_user.id)])
            if self.env.user.has_group('appscomp_hr.group_employee_team_leader'):
                args += [('parent_id', '=', emp_id.id)]
        return super(HrAttendance, self).search(args, offset, limit, order, count=count)
