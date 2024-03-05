{
    'name': "stock_transport",
    'version': '1.0',
    'category': "Dispatch/Fleet",
    'author': "Nandani Sanghani",
    'depends':['fleet','stock_picking_batch'],
    'data': [
         'security/ir.model.access.csv',
         'views/fleet_category.xml',
         'views/inventory_batch.xml',
        
        ],
    # "demo": 
    #     "data/estate_demo.xml"
    # ],
    'application': True
}   