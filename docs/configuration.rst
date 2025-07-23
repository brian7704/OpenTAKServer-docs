Configuration
=============

--------------

Config file
-----------

--------------

When you first start OpenTAKServer, a default configuration file will be
generated for you at ``~/ots/config.yml``. You can override the defaults
there. You must restart OpenTAKServer for the changes to take effect.

Secrets
-------

--------------

The following sensitive options will compromise the security of your
server if they are leaked. If you are asking for support over public
channels such as `Discord <https://discord.gg/6uaVHjtfXN>`__ or
`GitHub <https://github.com/brian7704/OpenTAKServer>`__, remove these
settings before posting. If these settings are mistakenly shared
publicly, change them immediately.

* SECRET_KEY
* SECURITY_PASSWORD_SALT
* OTS_MEDIAMTX_TOKEN
* MAIL_USERNAME
* MAIL_PASSWORD

Config Options
--------------

--------------

.. py:data:: DEBUG

    This setting puts Flask in debug mode and will produce many more
    log messages. Do not use on production servers. Default ``False``

.. py:data:: SECRET_KEY

    The `Flask secret key <https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY>`__.
    It is generated automatically with ``secrets.token_hex()`` the
    first time you run OpenTAKServer.

.. py:data:: SECURITY_PASSWORD_SALT

    Used by `Flask-Security <https://flask-security-too.readthedocs.io/en/stable/configuration/#SECURITY_PASSWORD_SALT>`__
    to salt hashed passwords. If you change this after users have been
    generated, they will be locked out until their passwords have been
    reset. This will lock out the administrator as well. It is
    automatically generated the first time you run OpenTAKServer using
    ``secrets.SystemRandom().getrandbits(128)``

OpenTAKServer Settings
----------------------

--------------

.. py:data:: OTS_DATA_FOLDER

   Folder for all of OpenTAKServer’s data (sqlite db, video
   recordings, uploaded files, etc). Default: ``~/ots``

.. py:data:: OTS_LISTENER_PORT

   OpenTAKServer’s API listens on this port on the loopback
   interface. Nginx will proxy HTTP requests to this port. Default
   ``8081``

.. py:data:: OTS_MARTI_HTTP_PORT (Renamed from OTS_HTTP_PORT as of version 1.1.3)

   Port that nginx listens on for HTTP requests. Nginx will proxy
   these requests to OTS_LISTENER_PORT. Default ``8080``

.. py:data:: OTS_MARTI_HTTPS_PORT (Renamed from OTS_HTTPS_PORT as of version 1.1.3)

   Nginx listens on this port for HTTPS requests and proxies them to
   OTS_LISTENER_PORT. Default ``8443``

.. py:data:: OTS_CERTIFICATE_ENROLLMENT_PORT

   Nginx listens on this port for certificate enrollment requests and
   proxies them to OTS_LISTENER_PORT. Default ``8446``

.. py:data:: OTS_TCP_STREAMING_PORT

   OpenTAKServer listens on this port for TCP connections from ATAK,
   WinTAK, and iTAK. Default ``8088``

.. py:data:: OTS_SSL_STREAMING_PORT

   OpenTAKServer listens on this port for SSL connections from ATAK,
   WinTAK, and iTAK. Default ``8089``

.. py:data:: OTS_BACKUP_COUNT (Added in 1.1.4)

   Log files in ``~/ots/logs/`` will rotate at midnight every night.
   This setting determines the number of days to keep rotated logs
   Log files older than this setting will be automatically deleted.
   Default ``7``

.. py:data:: OTS_RABBITMQ_SERVER_ADDRESS (Added in 1.1.4)

   Address of the RabbitMQ server. Default ``127.0.0.1``

.. py:data:: OTS_RABBITMQ_TTL (Added in 1.3.0)

   Time To Live setting for messages published to RabbitMQ. Default:
   ``86400000`` (one day)

.. py:data:: OTS_RABBITMQ_PREFETCH (Added in 1.4.3)

    Number of CoT messages to prefetch from the RabbitMQ queue. Default: ``2``

.. py:data:: OTS_COT_PARSER_PROCESSES (Added in 1.5.0)

    Number of ``cot_parser`` processes to run. Default: ``1``

.. py:data:: OTS_MEDIAMTX_API_ADDRESS (Added in 1.1.4)

   Address for MediaMTX’s API server. Make sure to include the scheme
   (ie ``http://``), address, and port. Default
   ``http://localhost:9997``

.. py:data:: OTS_MEDIAMTX_TOKEN

   This token protects the /api/mediamtx/webhook endpoint. It is
   generated using ``python3 -c 'import secrets; print(secrets.token_hex())``

.. py:data:: OTS_SSL_VERIFICATION_MODE

   SSL verification mode for the SSL CoT port. See `Python’s
   documentation <https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode>`__
   for more details. Default ``ssl.CERT_REQUIRED``

.. py:data:: OTS_NODE_ID

   Unique node ID of this server. It can be generated with the
   following command
   ``python3 -c "import random; import string; print(''.join(random.choices(string.ascii_lowercase + string.digits, k=64)))``

.. py:data:: OTS_CA_NAME

   Name for your certificate authority. Default ``OpenTAKServer-CA``

.. py:data:: OTS_CA_FOLDER

   Location of your certificate authority. Default ``~/ots/ca``

.. py:data:: OTS_CA_PASSWORD

   Password for all generated certificate. Default ``atakatak``

.. py:data:: OTS_CA_EXPIRATION_TIME

   Number of days that generated certificates should be valid.
   Default ``3650``

.. py:data:: OTS_CA_COUNTRY

   ISO country code for your certificate authority. Default ``WW``

.. py:data:: OTS_CA_STATE

   State abbreviation for your certificate authority. Default ``XX``

.. py:data:: OTS_CA_CITY

   City name for your certificate authority. Default ``YY``

.. py:data:: OTS_CA_ORGANIZATION

   Organization name for your certificate authority. Default ``ZZ``

.. py:data:: OTS_CA_ORGANIZATIONAL_UNIT

   Organizational Unit (OU) name for your certificate authority.

.. py:data:: OTS_CA_SUBJECT

   Subject for your certificate authority. Default
   ``/C=OTS_CA_COUNTRY/ST=OTS_CA_STATE/L=OTS_CA_CITY/O=OTS_CA_ORGANIZATION/OU=OTS_CA_ORGANIZATIONAL_UNIT``

.. py:data:: OTS_AIRPLANES_LIVE_LAT

   Latitude used to query ADS-B data from
   `Airplanes.live <https://airplanes.live/>`__. Default
   ``40.744213`` (Manhattan)

.. py:data:: OTS_AIRPLANES_LIVE_LON

   Longitude used to query ADS-B data from
   `Airplanes.live <https://airplanes.live/>`__. Default
   ``-73.986939`` (Manhattan)

.. py:data:: OTS_AIRPLANES_LIVE_RADIUS

   Radius in nautical miles to query ADSB from
   `Airplanes.live <https://airplanes.live/>`__. Default ``10`` Max
   ``250``

.. py:data:: OTS_AISHUB_USERNAME (Added in 1.3.0)

   Username of your AISHub.net account. Default: ``None``

.. py:data:: OTS_AISHUB_SOUTH_LAT (Added in 1.3.0)

   Southern latitude. Default: ``None``

.. py:data:: OTS_AISHUB_WEST_LON (Added in 1.3.0)

   Western longitude. Default: ``None``

.. py:data:: OTS_AISHUB_NORTH_LAT (Added in 1.3.0)

   Northern latitude. Default: ``None``

.. py:data:: OTS_AISHUB_EAST_LON (Added in 1.3.0)

   Eastern Longitude. Default: ``None``

.. py:data:: OTS_AISHUB_MMSI_LIST (Added in 1.3.0)

   A comma-separated string of MMSI numbers of specific vessels to
   search, for example ``"367658140,366902120"`` Default: ``""``

.. py:data:: OTS_AISHUB_IMO_LIST

   A comma-separated string of IMO numbers of specific vessels to
   search, for example ``"1234,5678"`` Default: ``""``

.. py:data:: OTS_PROFILE_MAP_SOURCES (Added in 1.3.0)

   Automatically install map tile sources from
   `ATAK-Maps <https://github.com/joshuafuller/ATAK-Maps.git>`__ when
   an EUD first connects to the server. Default: ``true``

.. py:data:: OTS_ENABLE_MUMBLE_AUTHENTICATION

   This option provide authentication for your Mumble server. When
   connecting to the Mumble server you will have to use your
   OpenTAKServer username and password. This also prevents anyone
   without an account on your OpenTAKServer from connecting. Default:
   ``False``

.. py:data:: OTS_ENABLE_EMAIL

   Allow users to self-register accounts with an email address.
   Emails will only be sent to users to confirm their registration,
   reset their passwords, and optionally for two-factor
   authentication. Default ``False``

.. py:data:: OTS_EMAIL_DOMAIN_WHITELIST

   If ``OTS_ENABLE_EMAIL`` is set to ``True``, you can use this
   whitelist to only allow users with email accounts with specific
   domains to register. For example, if you set this option to
   ``['gmail.com', 'yahoo.com']``, only users with gmail.com or
   yahoo.com email addresses can register. Leave the default setting
   to allow any domain to register. Default: ``[]``

.. py:data:: OTS_EMAIL_DOMAIN_BLACKLIST

   Similar to ``OTS_EMAIL_DOMAIN_WHITELIST``, but prevents specific
   email domains from registering accounts. Leave the default setting
   to allow any domain to register. Default: ``[]``

.. py:data:: OTS_EMAIL_TLD_WHITELIST

   Similar to ``OTS_EMAIL_DOMAIN_WHITELIST`` but only allows users
   with specific top level domains to register. For example, you
   could set this to ``['gov', 'mil']`` to only allow users with .gov
   or .mil email addresses to register. Do not put a dot before the
   TLD. Leave the default setting to allow any TLD to register.
   Default: ``[]``

.. py:data:: OTS_EMAIL_TLD_BLACKLIST

   Similar to ``OTS_EMAIL_TLD_WHITELIST``, but prevents certain top
   level domains from registering accounts. Leave the default setting
   to allow any TLD to register. Default: ``[]``

.. py:data:: OTS_DELETE_OLD_DATA_SECONDS (Added in 1.4.0)

   Used by the Delete Old Data scheduled job. Default: ``0``

.. py:data:: OTS_DELETE_OLD_DATA_MINUTES (Added in 1.4.0)

   Used by the Delete Old Data scheduled job. Default: ``0``

.. py:data:: OTS_DELETE_OLD_DATA_HOURS (Added in 1.4.0)

   Used by the Delete Old Data scheduled job. Default: ``0``

.. py:data:: OTS_DELETE_OLD_DATA_DAYS (Added in 1.4.0)

   Used by the Delete Old Data scheduled job. Default: ``0``

.. py:data:: OTS_DELETE_OLD_DATA_WEEKS (Added in 1.4.0)

   Used by the Delete Old Data scheduled job. Default: ``1``

.. py:data:: OTS_ENABLE_PLUGINS (Added in 1.5.0)

    Enable or disable server plugins. Default: ``True``

Flask-Security
--------------

--------------

You can check
`defaultconfig.py <https://github.com/brian7704/OpenTAKServer/blob/master/opentakserver/defaultconfig.py>`__
for the settings that OpenTAKServer uses. To learn about each setting
you can check Flask-Security’s
`documentation <https://flask-security-too.readthedocs.io/en/stable/configuration.html>`__.

Flask-Mailman settings
----------------------

--------------

These settings only take effect if ``OTS_ENABLE_EMAIL`` is ``True``. The
defaults will send email via a Gmail account, just provide your username
and `app
password <https://support.google.com/accounts/answer/185833?hl=en>`__.
See `Email <email.md>`__ for details.

.. py:data:: MAIL_ASCII_ATTACHMENTS

   Default ``False``

.. py:data:: MAIL_DEBUG

   Default ``False``

.. py:data:: MAIL_DEFAULT_SENDER

   Default ``null``

.. py:data:: MAIL_MAX_EMAILS

   Default: ``null``

.. py:data:: MAIL_PORT

   Default ``587``

.. py:data:: MAIL_SERVER

   Default ``smtp.gmail.com``

.. py:data:: MAIL_SUPPRESS_SEND

   Default ``false``

.. py:data:: MAIL_USERNAME

   Default ``null``

.. py:data:: MAIL_PASSWORD

   Default ``null``

.. py:data:: MAIL_USE_SSL

   Default ``false``

.. py:data:: MAIL_USE_TLS

   Default ``true``

MediaMTX
--------

--------------

OpenTAKServer’s default configuration assumes that MediaMTX is running
on the same server and OpenTAKServer connects to it via the loopback
interface. As of version 1.1.4, MediaMTX can now be hosted on a
different server. To do so you will need to change two settings.

The first is ``OTS_MEDIAMTX_API_ADDRESS`` in ``config.yml``. Make sure
to include the scheme (ie ``http://`` or ``https://``), server address,
and port.

The nginx config also needs to be changed. In
``/etc/nginx/sites-enabled/ots_https`` (or
``c:\tools\nginx-1.25.4\conf\ots\ots_https.conf`` on Windows), look for
the ``location`` blocks for webrtc and hls. Each should have a
``proxy_pass`` line that starts with ``https://127.0.0.1``. Change that
address (and port number if necessary) to the address of your MediaMTX
server.

After changing these settings make sure to restart both OpenTAKServer
and nginx.

Max Upload Size
---------------

--------------

OpenTAKServer’s default configuration limits the size of uploaded files,
including data packages, to 100MB. This setting is found in the
``ots_http`` and ``ots_https`` nginx config files. In those files,
change the line ``client_max_body_size 100M;`` to raise the limit.
