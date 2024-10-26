# -*- coding: utf-8 -*-
{
    'name': "Default Addon",

    'summary': """  Módulo para desenvolvimento para customização do módulo sale  """,

    'description': """
        Customização do módulo Sale
    """,

    'author': "Rafael Santos de Araujo",


    # any module necessary for this one to work correctly
    'depends': ['base',
                'account',
                'sale',
                'sales_team'
                ],

    # always loaded
    'data': [
        'views/sale_order_views.xml',
    ],
    'license': 'LGPL-3',
}
