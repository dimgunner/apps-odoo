# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


def post_init_hook(env):
    logger.info("Updating user settings for maps...")

    yandex_maps_id = env.ref('fct_partner_external_map.yandex_maps').id
    map_website_model = env["map.website"]
    user_model = env["res.users"]

    map_website_model.browse([
        env.ref('partner_external_map.bing_maps').id,
        env.ref('partner_external_map.here').id,
        env.ref('partner_external_map.mapquest').id,
    ]).write({
        "active": False,
    })

    user_model.search([]).write({
        "context_map_website_id": yandex_maps_id,
        "context_route_map_website_id": yandex_maps_id,
    })


def uninstall_hook(env):
    logger.info("Updating user settings for maps...")

    yandex_maps_id = env.ref('fct_partner_external_map.yandex_maps').id
    map_website_model = env["map.website"]
    user_model = env["res.users"]

    map_website_model.browse([
        env.ref('partner_external_map.bing_maps').id,
        env.ref('partner_external_map.here').id,
        env.ref('partner_external_map.mapquest').id,
    ]).write({
        "active": True,
    })

    map_website_model.browse([
        yandex_maps_id,
    ]).write({
        "active": False,
    })

    user_model.search([("context_map_website_id", "=", yandex_maps_id)]).write({
        "context_map_website_id": user_model._default_map_website().id,
    })

    user_model.search([("context_route_map_website_id", "=", yandex_maps_id)]).write({
        "context_route_map_website_id": user_model._default_route_map_website().id,
    })
