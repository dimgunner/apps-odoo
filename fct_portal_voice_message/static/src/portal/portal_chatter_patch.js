/** @odoo-module **/

import { Component } from "@odoo/owl";
import PortalChatter from '@portal/js/portal_chatter';

import publicWidget from "@web/legacy/js/public/public_widget";

PortalChatter.include({
    /**
     * @override
     */
    _renderMessages: function () {
        this._super(...arguments);
        Component.env.services.public_component.mountComponents();
    },

    _attach_stringify: function (attach) {
        attach.urlRoute = `/web/content/${attach.id}`;
        attach.urlQueryParams = {
            "access_token": attach.access_token,
            "filename": attach.name,
            "unique": attach.checksum,
        };
        return JSON.stringify(attach);
    },
});

publicWidget.registry.portalChatter.include({
    /**
     * @override
     */
    async start() {
        const result = await this._super.apply(this, arguments);
        Component.env.services.public_component.mountComponents();
        return result;
    },
});
