from odoo import models, fields


class Doctors(models.Model):
    _name = 'hms.doctors'
    _rec_name = 'f_name'

    f_name = fields.Char(required=True)
    l_name = fields.Char(required=True)
    image = fields.Image()


