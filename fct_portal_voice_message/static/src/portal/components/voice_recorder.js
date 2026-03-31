/** @odoo-module */

import { VoiceRecorder } from "@mail/discuss/voice_message/common/voice_recorder";
import { registry } from "@web/core/registry";

registry.category("public_components").add("fct_portal_voice_message.VoiceRecorder", VoiceRecorder);
