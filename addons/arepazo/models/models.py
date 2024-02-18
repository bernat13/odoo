# -*- coding: utf-8 -*-

from odoo import models, fields, api

class menu(models.Model):
    _name = 'arepazo.menu'
    name = fields.Char( required=True, index=True, help="Nombre")
    precioVenta = fields.Float()
    description = fields.Text(string="Descripción")
    tipo = fields.Selection([
        ('arepa', 'Arepa'),
        ('cachapa', 'Cachapa'),
        ('racion', 'Racion'),
        ('bebida', 'bebida'),
        ('postre', 'postre')
        ], default='arepa')
    receta = fields.Many2many('arepazo.ingrediente',
        'menu_ingrediente_rel', 'menu_id', 'ingrediente_id',cantidad=fields.Float()
                              , string='Ingredientes')
    ingredientePrincipal = fields.Many2one('arepazo.ingrediente', string="Ingrediente Principal")
    preciocoste = fields.Float(compute="_value_pc", store=True)
    rentabilidad= fields.Float(compute="_value_rentabilidad", store=True)
    cantidadIngredientes = fields.Integer(compute="_value_cantidadIngredientes", store=True)
    

    @api.depends('receta')
    def _value_pc(self):
        # suma el precio de todos los ingredientes de la receta
        self.preciocoste = sum(self.receta.mapped('precio'))
    
    @api.depends('precioVenta','preciocoste')
    def _value_rentabilidad(self):
        # calcula la rentabilidad
        if self.preciocoste != 0:
            if self.precioVenta != 0:
                self.rentabilidad = 100*(self.precioVenta-self.preciocoste)/self.precioVenta
            else:
                self.rentabilidad = 0
        else:
            self.rentabilidad = 100   

    @api.depends('receta')
    def _value_cantidadIngredientes(self):
        # cuenta la cantidad de ingredientes de la receta
        self.cantidadIngredientes = len(self.receta)


class mesa(models.Model):
    _name = 'arepazo.mesa'
    name= fields.Char( required=True, index=True, help="Nombre")
    camarero = fields.Many2one('res.partner', string="Servido por")
    # menu_id = fields.Many2one('arepazo.menu',string="Menu")
    # ingrediente_id = fields.Many2one('arepazo.ingrediente', string="Ingrediente")
    descripcion = fields.Text()

class ingrediente(models.Model):
    _name = 'arepazo.ingrediente'
    name = fields.Char( required=True, index=True, help="Nombre")
    precio = fields.Float()
    description = fields.Text(string="Descripción")
    menus = fields.Many2many('arepazo.menu',
        'menu_ingrediente_rel', 'ingrediente_id', 'menu_id',cantidad=fields.Float()
                              , string='Menus')
    SoyPrincipalEn = fields.One2many('arepazo.menu','ingredientePrincipal', string="Soy Principal En")
    
