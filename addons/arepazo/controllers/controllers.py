# -*- coding: utf-8 -*-
from odoo import http

class Arepazo(http.Controller):
    @http.route('/arepazo/arepazo/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/arepazo/arepazo/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('arepazo.listing', {
            'root': '/arepazo/arepazo',
            'objects': http.request.env['arepazo.arepazo'].search([]),
        })

    @http.route('/arepazo/arepazo/objects/<model("arepazo.arepazo"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('arepazo.object', {
            'object': obj
        })