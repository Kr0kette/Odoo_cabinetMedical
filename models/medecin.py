# -*- coding: utf-8 -*-
from odoo import fields, models


class Medecin(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # medecins
    medecin = fields.Boolean("Medecin", default=False)
