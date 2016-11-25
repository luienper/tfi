# -*- coding: utf-8 -*-
{
    'name': "TFI",

    'summary': """Inventario""",

    'description': """
        Toma fisica de invetario
    """,

    'author': "Luis Pérez",
    'website': "http://www.manexware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/local_views.xml',
        'views/zona_views.xml',
        'views/item_views.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}