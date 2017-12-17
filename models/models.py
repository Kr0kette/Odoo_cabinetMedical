# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api, exceptions


class Etablissement(models.Model):
    _name = 'cabinetmedical.etablissement'

    name = fields.Char(string="Nom de l'établissement", required=True)


class Specialite(models.Model):
    _name = 'cabinetmedical.specialite'

    name = fields.Char(string="Nom de la spécialité", required=True)



class Rendezvous(models.Model):
    _name = 'cabinetmedical.rendezvous'

    start_date = fields.Datetime()

    duration = fields.Float(help="Duration in hours", string="Duration in hours : minutes")

    end_date = fields.Datetime(string="End Date", store=True,
                           compute='_get_end_date', inverse='_set_end_date')

    etablissement_id = fields.Many2one('cabinetmedical.etablissement',
                                       ondelete='cascade', string="Etablissement")
    medecin_id = fields.Many2one('res.users', ondelete='cascade', string="Medecin")
    patient_id = fields.Many2one('res.partner', ondelete='cascade', string="Patient")

    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         self.value2 = float(self.value) / 100


    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            start = fields.Datetime.from_string(r.start_date)
            duration = timedelta(hours=r.duration, seconds=-1)
            r.end_date = start + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            start_date = fields.Datetime.from_string(r.start_date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - start_date).days + 1
