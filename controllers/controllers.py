# -*- coding: utf-8 -*-
# from odoo import http


# class Programaherencia(http.Controller):
#     @http.route('/programaherencia/programaherencia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/programaherencia/programaherencia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('programaherencia.listing', {
#             'root': '/programaherencia/programaherencia',
#             'objects': http.request.env['programaherencia.programaherencia'].search([]),
#         })

#     @http.route('/programaherencia/programaherencia/objects/<model("programaherencia.programaherencia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('programaherencia.object', {
#             'object': obj
#         })
