from odoo import models, fields


class Record(models.Model):
    _name = 'hms.record'
    _rec_name = 'description'

    created_by = fields.Many2one('res.users')
    date = fields.Date()
    description = fields.Char()
    log_id = fields.Many2one('hms.patient')

