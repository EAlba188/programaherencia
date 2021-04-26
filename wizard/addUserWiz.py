
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class addUserWiz(models.TransientModel):
    _name = "wizard.cambiousuario"

    theOne = fields.Many2one("res.users", string="Elegido")

    def setChoosenOnes(self):
        for x in self.env['sale.order'].browse(self.env.context.get('active_ids')):
            x.user_id = self.theOne