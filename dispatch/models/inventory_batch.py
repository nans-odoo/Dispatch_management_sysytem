from odoo import models, fields , api

class InventoryBatchTransfer(models.Model):
    _inherit = 'stock.picking.batch'

    dock = fields.Many2one('stock.dock', string='Dock')
    vehicle = fields.Many2one('fleet.vehicle',string='Vehicle')
    vehicle_category = fields.Many2one('fleet.vehicle.model.category',string='Vehicle Category')
    weight=fields.Float(compute='_compute_weight')
    volume=fields.Float(compute='_compute_volume')
    
    
    @api.depends('vehicle_category.max_weight','weight')
    def _compute_weight(self):
        for record in self:
            if record.vehicle_category:
                record.weight=record.weight / record.vehicle_category.max_weight
            else:
                record.weight=0.0
    
    @api.depends('vehicle_category.max_volume','volume')
    def _compute_volume(self):
        for record in self:
            if record.vehicle_category:
                record.volume=record.volume / record.vehicle_category.max_volume
            else:
                record.volume=0.0
    
    