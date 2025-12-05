from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    postcode = fields.Char(string='Postcode')
    tag_ids = fields.Many2many('estate.property.tag', 'estate_property_tag_rel', 'property_id', 'tag_id', string='Tags')
    bedrooms = fields.Integer()
    living_area = fields.Integer(string='Living Area (sqm)')
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price')
    date_availability = fields.Date()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ])
    agent_id = fields.Many2one('real.estate.agent', string='Agent')
from odoo import models, fields
from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    postcode = fields.Char(string='Postcode')
    tag_ids = fields.Many2many('estate.property.tag', 'estate_property_tag_rel', 'property_id', 'tag_id', string='Tags')
    bedrooms = fields.Integer()
    living_area = fields.Integer(string='Living Area (sqm)')
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price')
    date_availability = fields.Date()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ])
    agent_id = fields.Many2one('real.estate.agent', string='Agent')
