# -*- coding: utf-8 -*-

{
    'name': 'FCT Chatter Voice Messages',
    'version': '17.0.1.0.0',
    'category': 'Discuss',
    'license': 'AGPL-3',
    'summary': """Fincomtech Chatter Voice Messages""",
    'description': """Fincomtech Voice Messages for Chatter""",
    'author': 'Fincomtech',
    'depends': [
        'mail',
    ],
    'assets': {
        'web.assets_backend': [
            'fct_chatter_voice_message/static/src/xml/composer.xml',
        ]
    },
    'installable': True,
    'auto_install': True,
    'application': False,
}
