/** @odoo-module **/

import { Component } from "@odoo/owl";
import portalComposer from "@portal/js/portal_composer";

var PortalComposer = portalComposer.PortalComposer;

PortalComposer.include({
    /**
     * @override
     */
    start: function () {
        Component.env.bus.addEventListener('add_voice_attachment', (ev) => this._addVoiceAttachment(ev.detail));
        return this._super.apply(this, arguments);
    },

    _addVoiceAttachment: function (attachment) {
        this.attachments.push(attachment);
        this._updateAttachments();
    },
});
