# -*- coding: utf-8 -*-
from odoo import fields, models


class Medecin(models.Model):
    _inherit = 'res.users'

    is_medecin = fields.Boolean('Est un médecin', default=False)

    etablissement_id = fields.Many2many('cabinetmedical.etablissement',
                                       ondelete='cascade', string="Etablissement" ,)

    specialite_id=fields.Many2one('cabinetmedical.specialite',
                                       ondelete='cascade', string="Specialité")