==============
Server Plugins
==============

As of version 1.5.0, OpenTAKServer includes a plugin system.

Developing Plugins
------------------

If you'd like to develop a plugin, you can start by making a new repo by clicking the `Use this template` button
in the `OTS-Plugin-Template <https://github.com/brian7704/OTS-Plugin-Template>`_ repo.

Like OpenTAKServer, plugins are made using Python's `Flask <https://flask.palletsprojects.com/en/stable/>`_ framework.
Specifically, plugins are `Flask Blueprints <https://flask.palletsprojects.com/en/stable/tutorial/views/>`_.

Plugins classes must be a subclass of `opentakserver.plugins.Plugin.Plugin`