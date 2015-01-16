# -*- coding: utf-8 -*-
from openerp import http

# class MysiteFavicon(http.Controller):
#     @http.route('/mysite_favicon/mysite_favicon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mysite_favicon/mysite_favicon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mysite_favicon.listing', {
#             'root': '/mysite_favicon/mysite_favicon',
#             'objects': http.request.env['mysite_favicon.mysite_favicon'].search([]),
#         })

#     @http.route('/mysite_favicon/mysite_favicon/objects/<model("mysite_favicon.mysite_favicon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mysite_favicon.object', {
#             'object': obj
#         })