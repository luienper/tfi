# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Item(models.Model):
    _name = 'tfi.item'
    _rec_name = 'codigo'

    zona_id = fields.Many2one('tfi.zona',string='Zona')
    codigo = fields.Char()
    usuario = fields.Char()
    cantidad = fields.Integer()
    tipo_carga = fields.Selection(selection=[('A','Automático'),('M','Manual')], string="Tipo de carga")
