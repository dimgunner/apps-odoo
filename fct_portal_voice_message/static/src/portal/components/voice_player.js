/** @odoo-module */

import { VoicePlayer } from "@mail/discuss/voice_message/common/voice_player";
import { registry } from "@web/core/registry";

registry.category("public_components").add("fct_portal_voice_message.VoicePlayer", VoicePlayer);
