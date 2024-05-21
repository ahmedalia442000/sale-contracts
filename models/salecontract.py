from datetime import datetime, date
from odoo import api, fields, models
import calendar

class SaleContract(models.Model):
    _name = "sale.contract"
    _description = " Sale Contract"
    _rec_name = 'customer'
    _inherit = ['mail.thread','mail.activity.mixin']

    customer = fields.Char(string="Customer")
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, string="Company")
    currency_id = fields.Many2one('res.currency', string='Currency', related='company_id.currency_id')
    first_payment_date = fields.Date(string="First Payment Date", default=fields.Date.context_today)
    quotation_date = fields.Datetime(string="Quotation Date")
    responding = fields.Char(string="Responding to Maintenance Request")
    date = fields.Date(string="Date", default=fields.Date.context_today)
    sal_order = fields.Char(string="Sale Order")
    date_day = fields.Char(string="Day")
    first_batch = fields.Float(string="First Batch")
    second_batch = fields.Float(string="Second Batch")
    united_amount = fields.Float(string="United Amount")
    amount_tax = fields.Float(string="Amount Tax")
    total_amount = fields.Float(string="Total Amount")

    num_of_payment = fields.Integer(string="Number Of Payment")
    warranty_period = fields.Text(string="warranty period")
    consumables = fields.Integer(string="Consumables")
    contract_lines_ids = fields.One2many('contract.lines', 'line_contract_id', string="Contract Lines")

    @api.model
    def create(self, vals):
        # Call super() to create the record
        ss = super(SaleContract, self).create(vals)

        # Perform custom logic
        num = 0
        for line in ss.contract_lines_ids:
            num += 1
            line.num = num

        # Return the created record after processing
        return ss

    def write(self, vals):
        dd = super(SaleContract, self).write(vals)
        num = 0
        for line in self.contract_lines_ids:
            num += 1
            line.num = num
        return dd

    @api.onchange('date')
    def _get_day_of_date(self):
        for r in self:
            selected = fields.Datetime.from_string(r.date)
            r.date_day = calendar.day_name[selected.weekday()]







