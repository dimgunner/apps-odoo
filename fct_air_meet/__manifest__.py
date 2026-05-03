# -*- coding: utf-8 -*-

{
    'name': 'FCT Air Meets',
    'version': '17.0.1.0.0',
    'category': 'Productivity/Discuss',
    'license': 'AGPL-3',
    'summary': """Fincomtech Air Meets""",
    'description': """Fincomtech Air Meets for Discuss""",
    'author': 'Fincomtech',
    "depends": [
        'website',
    ],
    "data": [
        'security/ir.model.access.csv',
        'security/base_security.xml',
        'data/fct_air_meet.xml',
        'views/fct_air_meet_views.xml',
        'views/web_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'fct_air_meet/static/src/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
