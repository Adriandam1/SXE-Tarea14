# -*- coding: utf-8 -*-

from odoo import models, fields, api


class partner_zodiac(models.Model):
     #funciona "como un import"
     _inherit = 'res.partner'
     f_nac = fields.Date("Fecha de nacimiento")
     #NO SE DEBE ALMACENAR LA EDAD EN LA BD, ES MALA PRÁXIS, PERO LO HACEMOS CON FINES DE APRENDIZAJE
     edad = fields.Integer(string="Edad", readOnly = True, compute="_calcular_signo", store= True)
     signo_zodiacal = fields.Char(string="Signo zodiacal", readOnly = True, compute="_calcular_signo", store= True)
     linkedin_profile = fields.Char(string="Perfil de LinkedIn")
     activo_redes = fields.Selection([('activo', 'Activo'), ('inactivo', 'Inactivo')],
        string="Estado en Redes Sociales",
        compute="_calcular_actividad_redes",
        store=True
    )
     
     @api.depends('f_nac')
     def _calcular_edad(self):
        from datetime import date
        for record in self:
            if record.f_nac:
                today = date.today()
                record.edad = today.year - record.f_nac.year - ((today.month, today.day) < (record.f_nac.month, record.f_nac.day))

     @api.depends('f_nac')
     def _calcular_signo(self):
        signos = [
            ("Capricornio", (12, 22), (1, 19)),
            ("Acuario", (1, 20), (2, 18)),
            ("Piscis", (2, 19), (3, 20)),
            ("Aries", (3, 21), (4, 19)),
            ("Tauro", (4, 20), (5, 20)),
            ("Géminis", (5, 21), (6, 20)),
            ("Cáncer", (6, 21), (7, 22)),
            ("Leo", (7, 23), (8, 22)),
            ("Virgo", (8, 23), (9, 22)),
            ("Libra", (9, 23), (10, 22)),
            ("Escorpio", (10, 23), (11, 21)),
            ("Sagitario", (11, 22), (12, 21)),
        ]
        for record in self:
            if record.f_nac:
                mes, dia = record.f_nac.month, record.f_nac.day
                for signo, inicio, fin in signos:
                    if (inicio[0] == mes and inicio[1] <= dia) or (fin[0] == mes and fin[1] >= dia):
                        record.signo_zodiacal = signo
                        break

     @api.depends('linkedin_profile')
     def _calcular_actividad_redes(self):
        for record in self:
            record.activo_redes = 'activo' if record.linkedin_profile else 'inactivo'

