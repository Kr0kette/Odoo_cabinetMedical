# -*- coding: utf-8 -*-
from odoo import http

# class CabinetMedical(http.Controller):
#     @http.route('/cabinet__medical/cabinet__medical/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cabinet__medical/cabinet__medical/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cabinet__medical.listing', {
#             'root': '/cabinet__medical/cabinet__medical',
#             'objects': http.request.env['cabinet__medical.cabinet__medical'].search([]),
#         })

#     @http.route('/cabinet__medical/cabinet__medical/objects/<model("cabinet__medical.cabinet__medical"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cabinet__medical.object', {
#             'object': obj
#         })