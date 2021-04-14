# -*- coding: utf-8 -*-

from odoo import models, fields, api

class podExtendido(models.Model):
    _inherit = 'programaventas.producto'

    estado = fields.Selection(string="Estado", selection=[("pagado","Pagado"),("pendiente","Pendiente")])
