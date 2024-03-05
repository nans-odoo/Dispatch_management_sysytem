from odoo import models, fields , api

class InventoryBatchTransfer(models.Model):
    _inherit = 'stock.picking.batch'

    dock = fields.Many2one('stock.dock', string='Dock')
    vehicle = fields.Many2one('fleet.vehicle',string='Vehicle')
    vehicle_category = fields.Many2one('fleet.vehicle.model.category',string='Vehicle Category')
    weight=fields.Float(compute='_compute_weight')
    volume=fields.Float(compute='_compute_volume')
    
    
    @api.depends("move_line_ids", "vehicle_category")
    def _compute_weight(self):
        for record in self:
            total_weight = sum(move_line.product_id.weight * move_line.quantity for move_line in record.move_line_ids if move_line.product_id and move_line.product_id.weight)
            max_weight = record.vehicle_category.max_weight
            record.weight = (total_weight / max_weight)*100 if max_weight != 0 else 1000

    @api.depends("move_line_ids", "vehicle_category")
    def _compute_volume(self):
        for record in self:
            total_volume = sum(move_line.product_id.volume * move_line.quantity for move_line in record.move_line_ids if move_line.product_id and move_line.product_id.volume)
            max_volume = record.vehicle_category.max_volume
            record.volume = (total_volume / max_volume)*100 if max_volume != 0 else 1000

    


    

    
    
    
    