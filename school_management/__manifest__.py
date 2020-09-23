# -*- coding: utf-8 -*-
{
    'name': "school Management",
    'summary': """This module will store the school details""",
    'description': """This module will store the school details""",
    'author': "Aktiv software",
    'website': "http://www.aktivesoftware.com",
    'category': 'Tooles',
    'version': '12.0.1.0.0',
    'depends': ['base','sale_management',
                'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_record_views.xml',
        'views/profesor_record_views.xml',
        'views/subject_record_views.xml',
        'views/sale_order_views.xml',
        'views/product_product_views.xml',
        
        #'views/templates.xml',
    ],
   
}


