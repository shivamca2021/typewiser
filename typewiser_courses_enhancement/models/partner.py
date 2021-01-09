##############################################################################
from odoo import fields, models ,api, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class Partner(models.Model):
    _inherit = 'res.partner'
    
    is_instructor = fields.Boolean('Instructor')
    is_attendee = fields.Boolean('Attendee')
    course_ids = fields.Many2many('slide.channel', string='Courses')