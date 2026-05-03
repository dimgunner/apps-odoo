/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';
import { loadJS } from '@web/core/assets';

publicWidget.registry.AirWidget = publicWidget.Widget.extend({
    selector: '.air-meet-container',

    start() {
        this._super(...arguments);
        this.domain = this.$el.data('domain'),
        this._loadAirScript();
    },

    async _loadAirScript() {
        try {
            await loadJS(`https://${this.domain}/external_api.js`);
            this._initAirMeet();
        } catch (error) {
            console.error(`Failed to load ${this.domain} script:`, error);
        }
    },

    _initAirMeet() {
        if (typeof JitsiMeetExternalAPI !== 'undefined') {
            const url = window.location.href;
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

            this.api = new JitsiMeetExternalAPI(this.domain, options);
            this.api.on('readyToClose', () => {
                this.api.dispose();
                window.location.href = url;
            });
        }
    },

    destroy() {
        if (this.api) {
            this.api.dispose();
        }
        this._super(...arguments);
    }
});
