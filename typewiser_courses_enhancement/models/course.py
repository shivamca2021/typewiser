##############################################################################
from odoo import fields, models ,api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class Courses(models.Model):
    _inherit = 'slide.channel'

    instructor_id = fields.Many2one('res.partner', string='Instructor', domain="[('is_instructor', '=', True)]")
    course_room_id = fields.Many2one('course.rooms', string='Course Room')


class ChannelPartner(models.Model):
    _inherit = 'slide.channel.partner'

    @api.model
    def create(self, vals):
        channel_id = vals.get('channel_id', '')
        if channel_id:
            course_id = self.env['slide.channel'].browse(channel_id)
            if course_id.course_room_id and course_id.course_room_id.max_capacity:
                channel_attende_id = self.env['slide.channel.partner'].search([('channel_id', '=', channel_id)])
                if len(channel_attende_id) > int(course_id.course_room_id.max_capacity):
                    raise UserError(_('Only %s maximum Attendee are allowed')% (int(course_id.course_room_id.max_capacity)))
        
            if course_id and course_id.instructor_id and vals and vals.get('partner_id'):
                if vals.get('partner_id') == course_id.instructor_id.id:
                    raise UserError(_('%s person can not be an instructor and attendee of the same course')% (course_id.instructor_id.name))
                    
        return super(ChannelPartner, self).create(vals)