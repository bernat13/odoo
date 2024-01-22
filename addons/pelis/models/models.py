# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pelis(models.Model):
    _name = 'pelis.pelis'

    titulo = fields.Char()
    name = fields.Char()
    valoracion = fields.Integer()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100