# -*- coding: utf-8 -*-

{
    'name': 'FCT Portal Voice Messages',
    'version': '17.0.1.0.0',
    'category': 'Productivity/Discuss',
    'license': 'AGPL-3',
    'summary': """Fincomtech Portal Voice Messages""",
    'description': """Fincomtech Voice Messages for Portal""",
    'author': 'Fincomtech',
    'depends': [
        'mail',
        'portal',
    ],
    # 'data': {
    #     'views/templates.xml',
    # },
    'assets': {
        'web.assets_frontend': [
            'mail/static/src/core/common/attachment_service.js',
            # 'mail/static/src/core/common/persona_model.js',
            'mail/static/src/core/common/record.js',
            'mail/static/src/core/common/store_service.js',
            'mail/static/src/utils/common/misc.js',
            'mail/static/src/core/common/attachment_list.js',
            'mail/static/src/core/common/attachment_model.js',
            'mail/static/src/discuss/core/common/attachment_model_patch.js',
            'mail/static/src/discuss/voice_message/common/voice_message_service.js',
            'mail/static/src/discuss/voice_message/common/attachment_service_patch.js',

            'mail/static/src/discuss/voice_message/common/voice_player.xml',
            'mail/static/src/discuss/voice_message/common/voice_player.js',
            'mail/static/src/discuss/voice_message/common/voice_player.scss',

            'fct_portal_voice_message/static/src/portal/**/*',
        ],
    },
    'installable': True,
    'auto_install': True,
    'application': False,
}
