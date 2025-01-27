from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    nivel_de_autorizacion = fields.Selection([
        ('1', 'Nivel 1'),
        ('2', 'Nivel 2'),
        ('3', 'Nivel 3'),
    ], string='Nivel de Autorización OC', default='1')
