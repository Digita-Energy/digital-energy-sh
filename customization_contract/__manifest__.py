# -*- coding: utf-8 -*-
{
    'name': "Contract Customization",

    'version': '15.0.1.0.0',
    'summary': "Invoice format",
    'description': "Customised invoice,quotation,purchase order formats",
    'category': 'Invoicing',
    'author': 'Advanced Solutions',
    'website': 'http://www.advanced.qa',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['hr_contract'],

    # always loaded
    'data': [
        'views/hr_contract.xml',
    ],

}
