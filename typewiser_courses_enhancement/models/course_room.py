##############################################################################
from odoo import fields, models ,api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class CourseRooms(models.Model):
    _name = 'course.rooms'
    _inherit = ['mail.thread']
    _rec_name = 'room_code'
    _description = 'Course Rooms'

    room_code = fields.Char(string='Room Code')    
    room_name = fields.Char(string='Room Name')    
    course_ids = fields.Many2many('slide.channel', string='Course')  
    slide_ids = fields.Many2many('slide.slide', string='Lessons')  
    max_capacity = fields.Integer(string='Max Capacity')  
      
