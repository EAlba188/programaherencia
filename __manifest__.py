# -*- coding: utf-8 -*-
{
    'name': "programaherencia",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://github.com/EAlba188/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','helpdesk'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'wizard/addUserWizView.xml',
        'views/tipoView.xml',
        'views/views.xml',
        'views/heredaview.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
