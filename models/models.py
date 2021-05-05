
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tipoInicial(models.Model):
    _name = "tipo.inicial"

    name = fields.Char(string="Nombre")

class heredaTickets(models.Model):
    _inherit = "helpdesk.ticket"

    tipo_inicial = fields.Many2one("tipo.inicial", string="Tipo Inicial")