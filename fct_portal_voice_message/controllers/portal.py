# -*- coding: utf-8 -*-

import json

from odoo.http import request, route, Response
from odoo.addons.portal.controllers import portal


class CustomerPortal(portal.CustomerPortal):
    @route()
    def attachment_add(self, name, file, res_model, res_id, access_token=None, **kwargs):
        res = super().attachment_add(name, file, res_model, res_id, access_token, **kwargs)

        if kwargs.get("voice"):
            attachment = request.env['ir.attachment'].sudo().browse(res.json.get('id'))
            attachment._set_voice_metadata()

            data = res.json.copy()
            data['voice'] = 1

            return Response(json.dumps(data), mimetype='application/json')

        return res
