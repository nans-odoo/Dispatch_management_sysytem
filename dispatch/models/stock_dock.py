from odoo import models, fields

class StockDock(models.Model):
    _name = 'stock.dock'
    _description = 'Docks'

    name = fields.Char(string='Name', required=True)
    
