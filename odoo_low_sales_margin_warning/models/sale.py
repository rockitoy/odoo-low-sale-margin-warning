# -*- coding: utf-8 -*-
# Copyright (C) 2019-present  Technaureus Info Solutions(<http://www.technaureus.com/>).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    margin_percentage = fields.Float(compute='_product_margin_percent', string='Margin %', store=True)
    low_sale_margin = fields.Float(compute='_low_sale_margin')
    percent_symbol = fields.Char(default='%', readonly=True)

    @api.multi
    @api.depends('order_line.purchase_price', 'order_line.product_uom_qty', 'order_line.margin')
    def _product_margin_percent(self):
        for order in self:
            total_qty = 0
            total_cost = 0
            for line in order.order_line:
                total_qty += line.product_uom_qty
                total_cost += line.purchase_price

            if total_cost > 0 and order.margin != 0:
                order.margin_percentage = (order.margin / (total_cost * total_qty)) * 100

    @api.multi
    def _low_sale_margin(self):
        IrDefault = self.env['ir.default'].sudo()
        self.low_sale_margin = IrDefault.get('res.config.settings', "low_sale_margin")
