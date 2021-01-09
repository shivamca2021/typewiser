# -*- coding: utf-8 -*-
##############################################################################
{
    'name' : 'Typewiser Courses Enhancement',
    'category' : 'Base',
    'description' : """Typewiser Courses Enhancement

""",
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