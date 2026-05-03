/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';
import { loadJS } from '@web/core/assets';

publicWidget.registry.JitsiWidget = publicWidget.Widget.extend({
    selector: '.jitsi-meet-container',

    start() {
        this._super(...arguments);
        this._loadJitsiScript();
    },

    async _loadJitsiScript() {
        try {
            await loadJS('https://air.fincom.tech/external_api.js');
            this._initJitsiMeet();
        } catch (error) {
            console.error('Failed to load air.fincom.tech script:', error);
        }
    },

    _initJitsiMeet() {
        if (typeof JitsiMeetExternalAPI !== 'undefined') {
            const domain = 'air.fincom.tech';
            const options = {
                roomName: this.$el.data('room-name') || 'default-room',
                width: this.$el.data('width') || '100%',
                height: this.$el.data('height') || '100%',
                parentNode: this.el,
                configOverwrite: {
                    startWithAudioMuted: true,
                    startWithVideoMuted: true
                }
            };
            new JitsiMeetExternalAPI(domain, options);
        }
    }
});
