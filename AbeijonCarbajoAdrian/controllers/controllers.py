# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerZodiac(http.Controller):
#     @http.route('/partner_zodiac/partner_zodiac', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_zodiac/partner_zodiac/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_zodiac.listing', {
#             'root': '/partner_zodiac/partner_zodiac',
#             'objects': http.request.env['partner_zodiac.partner_zodiac'].search([]),
#         })

#     @http.route('/partner_zodiac/partner_zodiac/objects/<model("partner_zodiac.partner_zodiac"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_zodiac.object', {
#             'object': obj
#         })

