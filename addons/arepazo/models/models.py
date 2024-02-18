# -*- coding: utf-8 -*-

from odoo import models, fields, api

class menu(models.Model):
    _name = 'arepazo.menu'
    name = fields.Char( required=True, index=True, help="Nombre")
    precio = fields.Float()
    description = fields.Text(string="Descripción")
    tipo = fields.Selection([
        ('arepa', 'Arepa'),
        ('cachapa', 'Cachapa'),
        ('racion', 'Racion'),
        ('bebida', 'bebida'),
        ('postre', 'postre')
        ], default='arepa')
    ingredientes = fields.Many2many('arepazo.ingrediente', string='Ingredientes')



# class receta(models.Model):
#     _name = 'arepazo.receta'
#     name= fields.Char( required=True, index=True, help="Nombre")
#     cantidad = fields.Float()
#     menu_id = fields.Many2one('arepazo.menu','receta_ids', string="Menu")
#     ingrediente_id = fields.Many2one('arepazo.ingrediente', string="Ingrediente")
#     descripcion = fields.Text()

class ingrediente(models.Model):
    _name = 'arepazo.ingrediente'
    name = fields.Char( required=True, index=True, help="Nombre")
    precioPorKg = fields.Float()
    description = fields.Text(string="Descripción")
    menus = fields.Many2many('arepazo.menu', string="Recetas")

    
