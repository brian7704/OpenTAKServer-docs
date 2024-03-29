# Configuration

***

## Config file

***

When you first start OpenTAKServer, a default configuration file will be generated for you at `~/ots/config.yml`. You can
override the defaults there. You must restart OpenTAKServer for the changes to take effect.

## Config Options

***

- SECRET_KEY
    - The [Flask secret key](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY). This is generated 
    automatically by the installer. It is generated using the following command 
    `python3 -c 'import secrets; print(secrets.token_hex())`

- SECURITY_PASSWORD_SALT
    - Used by [Flask-Security](https://flask-security-too.readthedocs.io/en/stable/configuration/#SECURITY_PASSWORD_SALT) 
    to salt hashed passwords. If you change this after users have been generated, they will
    be locked out until their passwords have been reset. This will lock out the administrator as well. It is generated
    using `secrets.SystemRandom().getrandbits(128)`

## OpenTAKServer Settings

***

- OTS_DATA_FOLDER
    - Folder for all of OpenTAKServer's data (sqlite db, video recordings, uploaded files, etc). Default: `~/ots`

- OTS_LISTENER_PORT
    - OpenTAKServer's API listens on this port on the loopback interface. Nginx will proxy HTTP requests to this port.
        Default `8081`

- OTS_HTTP_PORT
    - Port that nginx listens on for HTTP requests. Nginx will proxy these requests to OTS_LISTENER_PORT. Default `8080`

- OTS_HTTPS_PORT
    - Nginx listens on this port for HTTPS requests and proxies them to OTS_LISTENER_PORT. Default `8443`

- OTS_CERTIFICATE_ENROLLMENT_PORT
    - Nginx listens on this port for certificate enrollment requests and proxies them to OTS_LISTENER_PORT. Default `8446`

- OTS_TCP_STREAMING_PORT
    - OpenTAKServer listens on this port for TCP connections from ATAK, WinTAK, and iTAK. Default `8088`

- OTS_SSL_STREAMING_PORT
    - OpenTAKServer listens on this port for SSL connections from ATAK, WinTAK, and iTAK. Default `8089`

- OTS_MEDIAMTX_TOKEN
    - This token protects the /api/mediamtx/webhook endpoint. It is generated using `python3 -c 'import secrets; print(secrets.token_hex())`

- OTS_SSL_VERIFICATION_MODE
    - SSL verification mode for the SSL CoT port. See [Python's documentation](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode) 
    for more details. Default `ssl.CERT_REQUIRED`
  
- OTS_NODE_ID
    - Unique node ID of this server. It can be generated with the following command `python3 -c "import random; import string; print(''.join(random.choices(string.ascii_lowercase + string.digits, k=64)))`

- OTS_CA_NAME
    - Name for your certificate authority. Default `OpenTAKServer-CA`

- OTS_CA_FOLDER
    - Location of your certificate authority. Default `~/ots/ca`

- OTS_CA_PASSWORD
    - Password for all generated certificate. Default `atakatak`

- OTS_CA_EXPIRATION_TIME
    - Number of days that generated certificates should be valid. Default `3650`

- OTS_CA_COUNTRY
    - ISO country code for your certificate authority. Default `WW`

- OTS_CA_STATE
    - State abbreviation for your certificate authority. Default `XX`

- OTS_CA_CITY
    - City name for your certificate authority. Default `YY`

- OTS_CA_ORGANIZATION
    - Organization name for your certificate authority. Default `ZZ`

- OTS_CA_ORGANIZATIONAL_UNIT
    - Organizational Unit (OU) name for your certificate authority.

- OTS_CA_SUBJECT
    - Subject for your certificate authority. Default 
    `/C=OTS_CA_COUNTRY/ST=OTS_CA_STATE/L=OTS_CA_CITY/O=OTS_CA_ORGANIZATION/OU=OTS_CA_ORGANIZATIONAL_UNIT`

- OTS_AIRPLANES_LIVE_LAT
    - Latitude used to query ADS-B data from [Airplanes.live](https://airplanes.live/). Default `40.744213` (Manhattan)

- OTS_AIRPLANES_LIVE_LON
    - Longitude used to query ADS-B data from [Airplanes.live](https://airplanes.live/). Default `-73.986939` (Manhattan)

- OTS_AIRPLANES_LIVE_RADIUS
    - Radius in nautical miles to query ADSB from [Airplanes.live](https://airplanes.live/). Default `10` Max `250`

- OTS_AIRPLANES_LIVE_MINUTES
    - Query interval (minutes) for [Airplanes.live](https://airplanes.live/) Default `5`

- OTS_AIRPLANES_LIVE_SECONDS
    - Query interval (seconds) for [Airplanes.live](https://airplanes.live/) Default `0`

- OTS_ENABLE_EMAIL
    - Allow users to self-register accounts with an email address. Emails will only be sent to users to confirm their registration,
    reset their passwords, and optionally for two-factor authentication. Default `False`

## Flask-Mail settings

***

These settings only take effect if `OTS_ENABLE_EMAIL` is `True`. The defaults will send email via a Gmail account, just
provide your username and [app password](https://support.google.com/accounts/answer/185833?hl=en). 
See [Flask-Mail's documentation](https://pythonhosted.org/Flask-Mail/) for details.

- MAIL_ASCII_ATTACHMENTS
    - Default `False`
- MAIL_DEBUG
    - Default `False`
- MAIL_DEFAULT_SENDER
    - Default `null`
- MAIL_MAX_EMAILS
    - Default: `null`
- MAIL_PORT
    - Default `465`
- MAIL_SERVER
    - Default `smtp.gmail.com`
- MAIL_SUPPRESS_SEND
    - Default `false`
- MAIL_USERNAME
    - Default `null`
- MAIL_PASSWORD
    - Default `null`
- MAIL_USE_SSL
    - Default `false`
- MAIL_USE_TLS
    - Default `true`
