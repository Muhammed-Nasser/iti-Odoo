from odoo import models, fields


class Departments(models.Model):
    _name = 'hms.department'

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patients_ids = fields.One2many(comodel_name='hms.patient', inverse_name='department_id')

