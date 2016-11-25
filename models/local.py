# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Local(models.Model):
    _name = 'tfi.local'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner',string='Cliente')
    zona_ids = fields.One2many('tfi.zona',inverse_name='local_id',string='Zona')
