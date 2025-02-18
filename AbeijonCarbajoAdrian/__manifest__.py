# -*- coding: utf-8 -*-
{
    'name': "partner_zodiac",

    'summary': "Modulo para ver el signo zodiacal",

    'description': """
Este módulo extiende el modelo res_partner añadiendo los siguientes 3 campos a los contactos:
- Fecha de nacimiento.
- Edad (calculado automaticamente)
- Signo zodiacal (calculado automaticamente)
    """,

    'author': "Daniel Castelao",
    'website': "https://www.danielcastelao.orgm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

