/** @odoo-module */

import { Component } from "@odoo/owl";
import { post } from "@web/core/network/http_service";
import { registry } from "@web/core/registry";
import { RPCError } from "@web/core/network/rpc_service";
import { VoiceRecorder } from "@mail/discuss/voice_message/common/voice_recorder";

class VoiceRecorderPortal extends VoiceRecorder {
    /**
     * @override
     */
    static template = "fct_portal_voice_message.VoiceRecorderPortal";

    /**
     * @override
     */
    static props = [
        ...VoiceRecorder.props,
        "res_id?",
        "res_model?",
        "token?",
    ];

    /**
     * @override
     */
    setup() {
        super.setup();
        this.$sendButton = $('.o_portal_chatter_composer_btn');
    }

    /**
     * @override
     */
    stopRecording() {
        this.getMp3()
            .then((buffer) => {
                const file = this._makeFile(buffer, "audio/mp3");
                this.uploadVoiceMessages([file]);
            })
            .catch(() => {});
        this.cleanUp();
    }

    /**
     * Widget PortalComposer
     * portal/static/src/js/portal_composer.js
     */
    _prepareAttachmentData(file) {
        /**
         * _prepareAttachmentData: function (file)
         */
        return {
            'name': file.name,
            'file': file,
            'res_id': this.props.res_id,
            'res_model': this.props.res_model,
            'access_token': this.props.token,
            'voice': true,
        };
    }

    uploadVoiceMessages(files) {
        /**
         * _onFileInputChange: function ()
         */
        var self = this;

        this.$sendButton.prop('disabled', true);

        return Promise.all(files.map((file) => {
            return new Promise(function (resolve, reject) {
                var data = self._prepareAttachmentData(file);
                if (odoo.csrf_token) {
                    data.csrf_token = odoo.csrf_token;
                }
                post('/portal/attachment/add', data).then(function (attachment) {
                    attachment.state = 'pending';
                    Component.env.bus.trigger('add_voice_attachment', attachment);
                    resolve();
                }).catch(function (error) {
                    if (error instanceof RPCError) {
                        self.notification.add(
                            _t("Could not save file <strong>%s</strong>", escape(file.name)),
                            { type: 'warning', sticky: true }
                        );
                        resolve();
                    }
                });
            });
        })).then(function () {
            self.$sendButton.prop('disabled', false);
        });
    }
}

export class VoiceRecorderOWL extends Component {
     static template = "fct_portal_voice_message.VoiceRecorderOWL";
     static components = {
        VoiceRecorderPortal,
     };
     static props = {
        res_id: { type: Number, optional: true },
        res_model: { type: String, optional: true },
        token: { type: String, optional: true },
     };
}

registry.category("public_components").add("fct_portal_voice_message.VoiceRecorderOWL", VoiceRecorderOWL);
