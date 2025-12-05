{
    'name': 'Estate',
    'version': '1.0',
    'summary': 'Real Estate Advertisement module',
    'description': 'Manage real estate properties and agents.',
    'author': 'Your Name',
    'category': 'Real Estate',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/real_estate_property_views.xml',
        'views/real_estate_agent_views.xml',
        'views/menu.xml',
    ],
    # No custom asset overrides (removed font size override)
    'installable': True,
    'application': True,
    'auto_install': False,
}