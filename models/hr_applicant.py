from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'hr.applicant'

    foto = fields.Image("Foto del Aplicante")
    
    cedula = fields.Char(string='Cédula / Pasaporte',required=True)

    birth_date = fields.Date(string="Fecha de Nacimiento")
    
    gender = fields.Selection([
        ('masculino', 'Másculino'),
        ('femenino', 'Femenino'),
    ], string='Sexo', default='masculino')
    
    civil_state = fields.Selection([
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
    ], string='Estado Civil', default='soltero')
    
    facebook_profile = fields.Char(string='Perfil de Facebook')
    
    instagram_profile = fields.Char(string='Perfil de Instagram')

    birthplace = fields.Char(string="Lugar de Nacimiento")

    nationality = fields.Char(string="Nacionalidad")

    address = fields.Char(string="Dirección")

    Ciudad = fields.Char(string="Ciudad")

    blood_type = fields.Char(string='Tipo de Sangre')

    ''' Idioma 1 '''

    language_name = fields.Selection([
        ('ingles', 'Inglés'),
        ('frances', 'Francés'),
    ], string='Idioma')

    language_read = fields.Selection([
        ('regular', 'Regular'),
        ('bien', 'Bien'),
    ], string='Lee', default='regular')

    language_write = fields.Selection([
        ('regular', 'Regular'),
        ('bien', 'Bien'),
    ], string='Escribe', default='regular')

    language_speak = fields.Selection([
        ('regular', 'Regular'),
        ('bien', 'Bien'),
    ], string='Habla', default='regular')

    ''' Idioma 2 '''

    language_name_2 = fields.Selection([
        ('ingles', 'Inglés'),
        ('frances', 'Francés'),
    ], string='Idioma')

    language_read_2 = fields.Selection([
        ('regular', 'Regular'),
        ('bien', 'Bien'),
    ], string='Lee', default='regular')

    language_write_2 = fields.Selection([
        ('regular', 'Regular'),
        ('bien', 'Bien'),
    ], string='Escribe', default='regular')

    language_speak_2 = fields.Selection([
        ('regular', 'Regular'),
        ('bien', 'Bien'),
    ], string='Habla', default='regular')

    ''' Educacion Primaria '''

    from_year = fields.Char(string="Desde")
    to_year = fields.Char(string="Hasta")
    gained_title = fields.Char(string="Titulo Obtenido")
    institution = fields.Char(string="Institución")

    ''' Educacion Adicional 1'''

    title_name_1 = fields.Char(string="Nivel Obtenido")
    from_year_1 = fields.Char(string="Desde")
    to_year_1 = fields.Char(string="Hasta")
    gained_title_1 = fields.Char(string="Titulo Obtenido")
    institution_1 = fields.Char(string="Institución")

    ''' Educacion Adicional 2'''

    title_name_2 = fields.Char(string="Nivel Obtenido")
    from_year_2 = fields.Char(string="Desde")
    to_year_2 = fields.Char(string="Hasta")
    gained_title_2 = fields.Char(string="Titulo Obtenido")
    institution_2 = fields.Char(string="Institución")

    ''' Educacion Adicional 3'''

    title_name_3 = fields.Char(string="Nivel Obtenido")
    from_year_3 = fields.Char(string="Desde")
    to_year_3 = fields.Char(string="Hasta")
    gained_title_3 = fields.Char(string="Titulo Obtenido")
    institution_3 = fields.Char(string="Institución")

    ''' Arbol Familiar '''

    family_name = fields.Char(string="Nombre Completo")
    family_relation = fields.Char(string="Parentesco")
    family_sex = fields.Selection([
        ('masculino', 'Másculino'),
        ('femenino', 'Femenino'),
    ], string='Sexo', default='masculino')
    family_age = fields.Integer(string="Edad")
    family_address = fields.Char(string="Dirección")

    ''' Arbol Familiar 2 '''

    family_name_2 = fields.Char(string="Nombre Completo")
    family_relation_2 = fields.Char(string="Parentesco")
    family_sex_2 = fields.Selection([
        ('masculino', 'Másculino'),
        ('femenino', 'Femenino'),
    ], string='Sexo', default='masculino')
    family_age_2 = fields.Integer(string="Edad")
    family_address_2 = fields.Char(string="Dirección")


    ''' Arbol Familiar 3 '''

    family_name_3 = fields.Char(string="Nombre Completo")
    family_relation_3 = fields.Char(string="Parentesco")
    family_sex_3 = fields.Selection([
        ('masculino', 'Másculino'),
        ('femenino', 'Femenino'),
    ], string='Sexo', default='masculino')
    family_age_3 = fields.Integer(string="Edad")
    family_address_3 = fields.Char(string="Dirección")




    