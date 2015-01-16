# -*- coding: utf-8 -*-
{
    'name': "mysite_favicon",

    'summary': """
        Publish favicon in <head>""",

    'description': """
        favicon.ico in mysite_favicon/static/src/img
        module inherit from website.layout
    """,

    'author': "Hansys",
    'website': "http://www.quarky.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/website_templates.xml',
    ],
}