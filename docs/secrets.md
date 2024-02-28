# Secrets
***
OpenTAKServer requires several secret keys that are stored in secret_keys.py which the installer script will generate
automatically. You will need to generate them yourself using Python's built-in secrets library if you are doing a manual installation.

**DO NOT POST OR SHARE THESE SECRETS**

Start by copying secret_keys.example.py to secret_keys.py.

- secret_key
    - This is Flask's [secret key](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY). From Flask's documentation:
  
  > A secret key that will be used for securely signing the session cookie and can be used for any other security related needs by extensions or your application. It should be a long random bytes or str. For example, copy the output of this to your config:

  > python3 -c 'import secrets; print(secrets.token_hex())'

  > Do not reveal the secret key when posting questions or committing code.

- node_id
    - Analogous to takserver's node_id. It can be generated using
    ```python3 -c "import random, string; print(''.join(random.choices(string.ascii_lowercase + string.digits, k=64)))"```

- security_password_salt
    - OpenTAKServer uses flask-security for authentication. This option specifies the salt used to hash passwords that
      are stored in the database. See flask-security's [documentation](https://flask-security-too.readthedocs.io/en/stable/configuration.html#SECURITY_PASSWORD_SALT) for more details. Generate by using this command:
      ```python3 -c 'import secrets; print(secrets.SystemRandom().getrandbits(128))'```

- mediamtx_token
    - This token is used as rudimentary protection of OpenTAKServer's MediaMTX API endpoints. Generate with the following
      command:
      ```python3 -c 'import secrets; print(secrets.SystemRandom().getrandbits(128))'```

- mail_username:
      - If email is enabled, this option should be set to the email address that messages will be sent from. If email is disabled,
        leave it set to the default value or an empty string.

- mail_password:
      - If email is enabled, this option should be set to the email password. If email is disabled,
        leave it set to the default value or an empty string.