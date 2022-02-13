from odoo import models, fields, api
from odoo.exceptions import UserError


class CrmInherit(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient')

    def unlink(self):
        if self.related_patient_id:
            raise UserError("You can not delete this patient")
        super(CrmInherit, self).unlink()

    @api.constrains('related_patient_id')
    def _check_patient_mail(self):
        if self.email == self.related_patient_id.email:
            raise UserError("You can not add this patient.")
