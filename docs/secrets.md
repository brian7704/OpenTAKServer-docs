# Secrets
***
Several secret keys are required and stored in `config.yml`. They will be generated automatically the first time you run
OpenTAKServer

### **DO NOT POST OR SHARE THESE SECRETS**

***

If you're asking for support on Discord or GitHub and need to post your `config.yml` file, be sure to redact these settings
before doing so. If your secrets are compromised, change them immediately.

### secret_key

***

This is Flask's [secret key](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY). From Flask's documentation:
  
  > A secret key that will be used for securely signing the session cookie and can be used for any other security related needs by extensions or your application. It should be a long random bytes or str. For example, copy the output of this to your config:

  > python3 -c 'import secrets; print(secrets.token_hex())'

  > Do not reveal the secret key when posting questions or committing code.
### security_password_salt

***

OpenTAKServer uses flask-security for authentication. This option specifies the salt used to hash passwords that
are stored in the database. See flask-security's [documentation](https://flask-security-too.readthedocs.io/en/stable/configuration.html#SECURITY_PASSWORD_SALT) for more details. Generate by using this command:
`python3 -c 'import secrets; print(secrets.SystemRandom().getrandbits(128))'`

### mediamtx_token

***

This token is used as rudimentary protection of OpenTAKServer's MediaMTX API endpoints. Generate with the following
command:
`python3 -c 'import secrets; print(secrets.SystemRandom().getrandbits(128))'`

### mail_username

***

If email is enabled, this is the email account username. If email is disabled, leave it set to the default value or an empty string.

### mail_password

***

If email is enabled, this the email accmount password. If email is disabled, leave it set to the default value or an empty string.