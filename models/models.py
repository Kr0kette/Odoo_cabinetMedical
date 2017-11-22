# -*- coding: utf-8 -*-

from odoo import models, fields, api
# class cabinet__medical(models.Model):
#      _name = 'cabinet__medical.cabinet__medical'
#
#      name = fields.Char()
#      value = fields.Integer()
#      value2 = fields.Float(compute="_value_pc", store=True)
#      description = fields.Text()
#
#      @api.depends('value')
#      def _value_pc(self):
#          self.value2 = float(self.value) / 100

class Cabinet(models.Model):
    _name = 'cabinet.medical'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()