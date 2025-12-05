from odoo import models, fields


class RealEstateAgent(models.Model):
    _name = 'real.estate.agent'
    _description = 'Real Estate Agent'

    name = fields.Char(string='Agent Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    property_ids = fields.One2many('estate.property', 'agent_id', string='Properties')
from odoo import models, fields

class RealEstateAgent(models.Model):
    _name = 'real.estate.agent'
    _description = 'Real Estate Agent'

    name = fields.Char(string='Agent Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    property_ids = fields.One2many('estate.property', 'agent_id', string='Properties')
