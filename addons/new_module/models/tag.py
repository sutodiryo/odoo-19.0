from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Property Tag'

    name = fields.Char(string='Tag', required=True)
    color = fields.Integer(string='Color Index')
from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Property Tag'

    name = fields.Char(string='Tag', required=True)
    color = fields.Integer(string='Color Index')
