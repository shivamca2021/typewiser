# -*- coding: utf-8 -*-
##############################################################################
{
    'name' : 'Typewiser Courses Enhancement',
    'version' : '13.0',
    'summary': 'Typewiser Courses Enhancement',
    'category': 'base',
    'author': 'Shiva Singh',
    'depends' : ['website_slides', 'base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/course_room_view.xml',
        'views/course_view.xml',
        'views/res_partner_view.xml',
        'views/slide_template_course.xml',
    ],
    'qweb' : [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}
