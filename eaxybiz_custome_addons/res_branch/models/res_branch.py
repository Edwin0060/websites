from odoo import models, fields, api



class ResBranch(models.Model):
    '''Multiple Company Modification'''

    _name = "res.branch"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Multiple Company Modification"



    name = fields.Char(string="Name")
    company_id = fields.Many2one('res.company',string="Company")
    street1 = fields.Char(string="Street1", tracking=True)
    street2 = fields.Char(string="Street2", tracking=True)
    city = fields.Char(string="City", tracking=True)
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]", tracking=True)
    zip = fields.Char(change_default=True, tracking=True)
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', tracking=True)
    image = fields.Binary(string="Image", tracking=True)

class ResUser(models.Model):
    _inherit = "res.users"

    branch_id = fields.Many2one('res.branch', string='Default Branch',
                                help='The default Branch for this user.')
    allowed_branch_ids = fields.Many2many('res.branch', 'res_branch_users_rel', 'user_id', 'bid',
                                  string='Allowed Branch')

