
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class addUserWiz(models.TransientModel):
    _name = "wizard.cambiousuario"

    theOne = fields.Many2one("res.users", string="Comercial")

    theClient = fields.Many2one("res.partner", string="Cliente")

    def setChoosenOnes(self):
        for x in self.env['sale.order'].browse(self.env.context.get('active_ids')):
            x.user_id = self.theOne
            x.partner_id = self.theClient

class tipoInicial(models.Model):
    _name = "tipo.inicial"

    name = fields.Char(string="Nombre")

class heredaTickets(models.Model):
    _inherit = "helpdesk.ticket"

    tipo_inicial = fields.Many2one("tipo.inicial", string="Tipo Inicial")