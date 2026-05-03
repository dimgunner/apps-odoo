# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class AirMeet(http.Controller):

    @http.route('/air-meet/<int:meet_id>/', type='http', auth="public", website=True)
    def air_meet(self, meet_id, **kwargs):
        record = request.env['air.meet'].sudo().browse(meet_id)

        if record and not record.closed:
            return request.render("fct_air_meet.meet", {'data': record})

        return request.render("fct_air_meet.meet_closed")
