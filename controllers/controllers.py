# -*- coding: utf-8 -*-
from odoo import http

class Tfi(http.Controller):
    @http.route('/tfi/', auth='public')
    def index(self, **kw):
        return "True"

    @http.route('/mimodulo/mimodulo/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('mimodulo.listing', {
            'root': '/mimodulo/mimodulo',
            'objects': http.request.env['mimodulo.mimodulo'].search([]),
        })

    @http.route('/mimodulo/mimodulo/objects/<model("mimodulo.mimodulo"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('mimodulo.object', {
            'object': obj
        })