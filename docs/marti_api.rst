Marti API
---------

The following Marti API endpoints are supported by OTS. The full Marti API spec can be found on `TAK.gov <https://docs.tak.gov/api/takserver>`__

.. autoflask:: opentakserver.app:create_app()
    :undoc-static:
    :blueprints: marti_blueprint.certificate_authority_api_blueprint, marti_blueprint.citrap_api_blueprint, marti_blueprint.contacts_api, marti_blueprint.cot_api, marti_blueprint.data_package_marti_api,
                 marti_blueprint.device_profile_marti_api_blueprint, marti_blueprint.group_api, marti_blueprint.marti_api, marti_blueprint.mission_marti_api, marti_blueprint.video_marti_api
    :include-empty-docstring: