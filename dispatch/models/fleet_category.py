from odoo import fields, models,api

class FleetCategory(models.Model):

    
    _inherit = "fleet.vehicle.model.category"
    max_weight = fields.Float(string="Max Weight")
    max_volume = fields.Float(string="Max Volume")

    @api.depends('name', 'max_weight', 'max_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name
            if record.max_weight or record.max_volume:
                record.display_name += f" ({record.max_weight}kg, {record.max_volume}㎥)"

    




    


    

