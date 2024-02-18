# -*- coding: utf-8 -*-
{
    'name': "Arepazo",

    'summary': """
       Para gestionar el menú y la rentabilidad de un restaurante de comida Venezolana Arepazo""",

    'description': """
        Arepazo es fenomenal
    """,

    'author': "Bernat",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
         'web.assets_common': [
            'pelis/static/src/scss/pelis.scss',
            'pelis/static/src/js/pelis.js',
            ],
            
    },
    'application': True,
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}