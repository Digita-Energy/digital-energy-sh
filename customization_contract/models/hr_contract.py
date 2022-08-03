from odoo import models, fields, api
import calendar
import datetime


class HRContract(models.Model):
    _inherit = 'hr.contract'

    accomodation_allowance = fields.Float(string="Accomodation Allowance")
    food_allowance = fields.Float(string="Food Allowance")
    project_allowance = fields.Float(string="Project Allowance")

