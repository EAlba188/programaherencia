
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class addUserWiz(models.TransientModel):
    _name = "addUserWiz"

    def _get_that_sales(self):
        return self.env['sale.order'].browse(self.env.context.get('active_ids'))

    choosenOnes = fields.One2many("sale.order", string="Usuarios", default=_get_that_sales)
    theOne = fields.Many2one("res.user", string="Elegido")

    def setChoosenOnes(self):
        for x in self.choosenOnes:
            x.user_id = self.theOne