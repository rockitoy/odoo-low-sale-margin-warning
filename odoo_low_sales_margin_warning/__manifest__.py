# -*- coding: utf-8 -*-
# Copyright (C) 2019-present  Technaureus Info Solutions(<http://www.technaureus.com/>).

{
    'name': 'Odoo Low Sales Margin Warning ',
    'version': '12.0.0.0',
    'category': 'Sales',
    'summary': 'Margin Warning',
    'sequence': 1,
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'website': 'http://www.technaureus.com/',
    'description': """
    """,
    'depends': ['sale_margin'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/sale_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
