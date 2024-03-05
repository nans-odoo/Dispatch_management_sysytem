{
    'name': "stock_transport",
    'version': '1.0',
    'category': "Dispatch/Fleet",
    'author': "Nandani",
    'depends':['base','fleet','stock_picking_batch'],
    'data': [
         'security/ir.model.access.csv',
         'views/fleet_category.xml',
         'views/inventory_batch.xml',
        
        ],
    'application': True
}   