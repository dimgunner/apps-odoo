# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AirMeet(models.Model):
    _name = 'air.meet'
    _description = 'Air Meetings'
    _order = 'id desc'
    _inherit = 'mail.thread'

    def _get_default_participants(self):
        return [(6, 0, [self.env.user.id])]

    name = fields.Char('Name', required=True)
    participants = fields.Many2many('res.users', string='Participants', required=True,
                                    default=_get_default_participants)
    url = fields.Char(string='URL to Meeting', compute='_compute_url')
    closed = fields.Boolean(string='Closed')
    domain = fields.Char(string='Domain', compute='_compute_domain')

    @api.depends('name')
    def _compute_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for rec in self:
            rec.url = base_url + "/air-meet/" + str(rec.id)

    def _compute_domain(self):
        domain = self.env['ir.config_parameter'].sudo().get_param('fct_air_meet.url')
        for rec in self:
            rec.domain = domain

    def action_close_meeting(self):
        self.write({'closed': True})

    def action_reopen_meeting(self):
        self.write({'closed': False})

    def open(self):
        return {
            'name': _('Air Meet'),
            'res_model': 'ir.actions.act_url',
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': self.url
        }

    def send_mail(self):
        for rec in self.participants - self.env.user:
            body_html = _(
                '<div><p>You have been invited to a meeting</p>'
                '<p>Please join us by clicking on the following link: </p>'
                '<p>'
                '<a href="%s">JOIN MEETING</a>'
                '</p>'
                '<p>Thank you</p></div>'
            )
            main_content = {
                'subject': _("Air Meet Invitation"),
                'author_id': self.env.user.partner_id.id,
                'body_html': body_html % self.url,
                'email_to': rec.email,
            }
            self.env['mail.mail'].create(main_content).send()

        self.env['mail.mail'].process_email_queue()
