# -*- coding: utf-8 -*-

{
    'name': 'FCT Partner External Maps',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'license': 'AGPL-3',
    'summary': """Fincomtech Partner External Maps""",
    'description': """Fincomtech Partner External Maps Extension""",
    'author': 'Fincomtech',
    'depends': [
        'partner_external_map',
    ],
    'data': [
        'data/map_website_data.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'auto_install': True,
    'application': False,
}
