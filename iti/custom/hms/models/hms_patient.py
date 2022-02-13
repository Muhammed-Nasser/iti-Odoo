from odoo import models, fields, api
from datetime import date
from odoo.exceptions import UserError
import re


class Patient(models.Model):
    _name = 'hms.patient'
    _rec_name = 'f_name'

    f_name = fields.Char(required=True)
    l_name = fields.Char(required=True)
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([('a+', 'A+'),
                                  ('a-', 'A-'),
                                  ('b+', 'B+'),
                                  ('b-', 'B-'),
                                  ('ab+', 'AB+'),
                                  ('ab-', 'AB-'),
                                  ('O+', 'O+'),
                                  ('O-', 'O-')])
    pcr = fields.Boolean()
    image = fields.Image()
    address = fields.Char()
    email = fields.Char()
    age = fields.Integer()
    department_id = fields.Many2one('hms.department')
    records_ids = fields.One2many('hms.record', 'log_id')
    doctors_ids = fields.Many2many('hms.doctors')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ])
    department_capacity = fields.Integer(string="Department capacity", related="department_id.capacity")

    def undetermined(self):
        self.state = 'undetermined'
        self.env['hms.record'].create({
            'created_by': self._uid,
            'date': date.today(),
            'description': f'state changed to {self.state}',
            'log_id': self.id
        })

    def good(self):
        self.state = 'good'
        self.env['hms.record'].create({
            'created_by': self._uid,
            'date': date.today(),
            'description': f'state changed to {self.state}',
            'log_id': self.id

        })

    def fair(self):
        self.state = 'fair'
        self.env['hms.record'].create({
            'created_by': self._uid,
            'date': date.today(),
            'description': f'state changed to {self.state}',
            'log_id': self.id
        })

    def serious(self):
        self.state = 'serious'
        self.env['hms.record'].create({
            'created_by': self._uid,
            'date': date.today(),
            'description': f'state changed to {self.state}',
            'log_id': self.id
        })

    @api.onchange('age')
    def _onchange_age(self):
        if self.age > 30:
            self.pcr = True
            return {
                'warning': {
                    'message': 'PCR has been changed.'
                }
            }

    _sql_constraints = [
        ('mail_unique', 'unique(email)', 'Email already exists!')
    ]

    @api.constrains('email')
    def _check_salary_value(self):
        if not re.match( '(\w+[.|\w])*@(\w+[.])*\w+', self.email):
            raise UserError("Email not valid.")

    #@api.onchange('birth_date')
    #def _onchange_birth_date(self):
    #    if self.birth_date < date.today():
    #        self.age = date.today().year - self.birth_date.year
    #        return {
    #             'warning': {
    #                'message': 'Age has been changed.'
    #             }
    #        }
    #    raise UserError("Birthdate not valid.")