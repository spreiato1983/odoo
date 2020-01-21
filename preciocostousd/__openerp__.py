# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Precio Costo USD',
    'version': '1.0',
    'author': ['Santiago Preiato'],
    'category': 'Tools',
    'summary': 'Precio Costo USD',
    'website': 'https://www.sgpgestion.com.ar',
    'description': """
Precio Costo USD.
======================
Con este módulo mostraremos Precio Costo Dolares
    """,
    'depends': ['base'],
    'data': [
        'preciocostousd_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}
