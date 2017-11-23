# -*- coding: utf-8 -*-
from odoo import http

# class Cabinetmedical(http.Controller):
#     @http.route('/cabinetmedical/cabinetmedical/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cabinetmedical/cabinetmedical/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cabinetmedical.listing', {
#             'root': '/cabinetmedical/cabinetmedical',
#             'objects': http.request.env['cabinetmedical.cabinetmedical'].search([]),
#         })

#     @http.route('/cabinetmedical/cabinetmedical/objects/<model("cabinetmedical.cabinetmedical"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cabinetmedical.object', {
#             'object': obj
#         })