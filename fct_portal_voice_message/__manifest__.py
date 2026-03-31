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
    'assets': {
        'web.assets_frontend': [
            'mail/static/src/utils/common/misc.js',
            'mail/static/src/core/common/record.js',
            'mail/static/src/core/common/store_service.js',
            'mail/static/src/core/common/user_settings_service.js',
            'mail/static/src/discuss/voice_message/common/mp3_encoder.js',
            'mail/static/src/discuss/voice_message/common/voice_message_service.js',
            'mail/static/src/discuss/voice_message/common/voice_player.js',
            'mail/static/src/discuss/voice_message/common/voice_player.xml',
            'mail/static/src/discuss/voice_message/common/voice_player.scss',
            'mail/static/src/discuss/voice_message/common/voice_recorder.js',
            'mail/static/src/discuss/voice_message/common/voice_recorder.xml',
            'fct_portal_voice_message/static/src/portal/**/*',
        ],
    },
    'installable': True,
    'auto_install': True,
    'application': False,
}
