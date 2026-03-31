/** @odoo-module */

//import { Component } from "@odoo/owl";
import { VoicePlayer } from "@mail/discuss/voice_message/common/voice_player";

import { registry } from "@web/core/registry";

//export class VoiceRecorder extends Component {
export class VoiceRecorder extends VoicePlayer {
//     static template = "fct_portal_voice_message.VoiceRecorder";
//     static props = {};
}

registry.category("public_components").add("fct_portal_voice_message.VoiceRecorder", VoiceRecorder);
