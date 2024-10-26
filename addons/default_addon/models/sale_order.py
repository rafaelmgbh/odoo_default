from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    phone_number = fields.Char(string="Phone Number")
