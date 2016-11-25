# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Zona(models.Model):
    _name = 'tfi.zona'

    status = fields.Char(string='Estatus')
    name = fields.Char(string='Nombre')
    fecha_apertura = fields.Datetime(default=fields.Datetime.now())
    fecha_cierre = fields.Datetime()
    local_id = fields.Many2one('tfi.local',string='Local')
    item_ids = fields.One2many('tfi.item',inverse_name='zona_id', string='Items')
    total_items = fields.Integer(string='Total Items')