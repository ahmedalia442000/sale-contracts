from datetime import datetime, date
from odoo import api, fields, models


class ContractLines(models.Model):
    _name = "contract.lines"


    line_contract_id = fields.Many2one('sale.contract', string="Contract")
    products_id = fields.Many2one('product.product', string="Product")
    quantaty = fields.Float(string="Quantity")
    price_unit = fields.Float(string="Price Unit", related='products_id.list_price')
    discount = fields.Float(string="Discount")
    price_total = fields.Float(string="Price Total")
    tax_amount = fields.Float(string="Tax Amount")
    price_Sub_total = fields.Float(string="Price Sub Total")
    taxes = fields.Float(string="Taxes")
    num = fields.Integer(string="Num", readonly=True)
