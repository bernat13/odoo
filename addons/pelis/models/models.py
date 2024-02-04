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
    tipo = fields.Selection([
        ('ficcion', 'Ficcion'),
        ('documental', 'Documental')
    ], default='accion')
    genero = fields.Many2one('pelis.genero', string="Genero")
    actores = fields.Many2many('pelis.actores', string="Actores")
    

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

class genero(models.Model):
    _name = 'pelis.genero'

    name = fields.Char()
    description = fields.Text()
    pelis_ids = fields.One2many('pelis.pelis', 'genero', string="Pelis")


class actores(models.Model):
    _name = 'pelis.actores'

    name = fields.Char()
    pais=  fields.Char()
    biografia = fields.Text()
    pelis_ids = fields.Many2many('pelis.pelis', string="Pelis")