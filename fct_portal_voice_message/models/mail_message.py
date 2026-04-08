# -*- coding: utf-8 -*-

from odoo import models


class MailMessage(models.Model):
    _inherit = 'mail.message'

    def _portal_message_format(self, properties_names, options=None):
        vals_list = super()._portal_message_format(properties_names, options=options)

        attachment_ids = [
            attachment['id']
            for val in vals_list
            for attachment in val.get('attachment_ids', [])
            if attachment.get('id')
        ]

        if attachment_ids:
            attachments = self.env['ir.attachment'].sudo().browse(attachment_ids)
            voice_map = {attachment.id: 1 if attachment.voice_ids else 0 for attachment in attachments}

            for val in vals_list:
                for attachment in val.get('attachment_ids', []):
                    if attachment_id := attachment.get('id'):
                        attachment['voice'] = voice_map.get(attachment_id, 0)

        return vals_list
