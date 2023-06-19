# -*- coding:utf-8 -*-
from odoo import api, fields, models

class AsignacionMaterial(models.Model):
    _name = 'asignacion.material'
    _description = 'Módulo para el control del material y epis de los trabajadores'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _order = 'name desc'

    icon = 'asignacion_material,static/description/icon.png'

    name = fields.Char(string='Secuencia', required=True, copy=False, readonly=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('asignacion.material.sequence'))
    date = fields.Datetime(string='Fecha de entrega', default=fields.Datetime.now)
    responsable_entrega_id = fields.Many2one('hr.employee', string='Responsable de Entrega')
    empleado_id = fields.Many2one('hr.employee', string='Operario')
    asignacion_line_ids = fields.One2many('asignacion.material.line', 'asignacion_material_id', string='Asignaciones de Material')
    firma = fields.Binary(string='Firma')
    




class Material(models.Model):
    _name = 'material'
    _description = 'Material'

    name = fields.Char(string='Material', required=True)
    asignacion_line_ids = fields.One2many('asignacion.material.line', 'material_id', string='Asignaciones')
    asignacion_count = fields.Integer(string='Asignaciones', compute='_compute_asignacion_count')

    @api.depends('asignacion_line_ids')
    def _compute_asignacion_count(self):
        for record in self:
            record.asignacion_count = len(record.asignacion_line_ids)



class AsignacionMaterialLine(models.Model):
    _name = 'asignacion.material.line'
    _description = 'Línea de asignación de material'
    
    asignacion_material_id = fields.Many2one('asignacion.material', string='Asignación de Material')
    material_id = fields.Many2one('material', string='Material')
    cantidad = fields.Float(string='Cantidad')
    fecha = fields.Datetime(string='Fecha de asignación', related='asignacion_material_id.date')
    operario_id = fields.Many2one('hr.employee', string='Operario', related='asignacion_material_id.empleado_id')
    asignacion_id = fields.Char(string='Identificador de asignación', related='asignacion_material_id.name')



