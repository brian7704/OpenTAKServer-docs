OpenTAKServer API
-----------------

.. autoflask:: opentakserver.app:create_app()
    :undoc-static:
    :blueprints: ots_api.token_api_blueprint, ots_api.api_blueprint, ots_api.casevac_api_blueprint, ots_api.data_package_api,
                 ots_api.device_profile_api_blueprint, ots_api.eud_stats_blueprint, ots_api.group_api, ots_api.ldap_blueprint,
                 ots_api.marker_api_blueprint, ots_api.mediamtx_api_blueprint, ots_api.meshtastic_api_blueprint, ots_api.data_sync_api,
                 ots_api.packages_api_blueprint, ots_api.plugin_api_blueprint, ots_api.schedule_api_blueprint, ots_api.user_api_blueprint,
                 ots_api.video_api_blueprint
    :include-empty-docstring: