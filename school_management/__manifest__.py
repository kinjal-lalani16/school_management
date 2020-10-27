
{
    'name': "school Management",
    'summary': """This module will store the school details""",
    'description': """This module will store the school details""",
    'author': "Aktiv software",
    'website': "http://www.aktivesoftware.com",
    'category': 'Tooles',
    'version': '13.0.1.0.0',
    'depends': ['base',
                'sale_management',
                'sale'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/student_record_views.xml',
        'views/profesor_record_views.xml',
        'views/subject_record_views.xml',
        'views/product_product_views.xml',
        'views/sale_order_views.xml',
        'views/test_view.xml',
        'views/res_config_views.xml',

        # data files
        'data/ir_sequence_data.xml',
        'data/subject_corn.xml',

        # wizard files
        'wizard/date_wizard_view.xml',
        'wizard/msg_wizard_views.xml',

        # report files
        'report/student_report.xml',
        'report/student_report_view.xml',
        'report/profesor_view.xml',
        'report/sale_order_report_view.xml',
    ],

}
