# Authentication

***

OpenTAKServer uses [Flask-Security](https://flask-security-too.readthedocs.io/en/stable/) to provide authentication.

## Administrator Account

***

When you start OpenTAKServer for the first time, an administrator account is automatically created. The username
is `administrator` and the password is `password`. You should immediately change the password when you first log in.

## Creating Accounts

***

By default, only administrators can create user accounts. However, users can register their own accounts if an administrator
enables [email](email.md) support.

## Note on Passwords

***

OpenTAKServer prevents `@` and `:` characters in passwords. In certain situations that use basic authentication, 
such as viewing RTSP streams, having these characters can cause an invalid URL. A typical URL when using basic authentication
looks like `rtsp://username:password@server_address:8554/path`. In these situations, the ':' character separates the
username and password, and the `@` character separates the username/password from the server address. Having a password
with these characters will cause browsers and video players to incorrectly parse the URL.

## Token Authentication

***

OpenTAKServer supports token authentication which can be helpful when interacting with OpenTAKServer via the
[API](API.md). Use the following steps to authenticate with a token:

Add these settings to `~/ots/config.yml` if they're not already present. This will remove the CSRF requirements
for token auth but still require CSRF for basic and session auth.

```yaml
SECURITY_CSRF_PROTECT_MECHANISMS:
- session
- basic
```

If you changed `config.yml` you must restart OpenTAKServer `sudo systemctl restart opentakserver`   

Next, make an HTTP POST request to `/api/login` with the `include_auth_token` query parameter and your credentials as JSON.
Here is an example in Python. If your server uses signed certs such as from Let's Encrypt you can remove `verify=False`.

```python
import requests
response = requests.post("https://<your_server_address>/api/login", params={'include_auth_token': ''}, json={'username': 'your_username', 'password': 'your_password'}, verify=False)
```
   
A successful login JSON response will be as follows

```json
{
  "meta": {
    "code": 200
},
  "response": {
    "csrf_token": "xxxxx",
    "user": {
      "authentication_token": "yyyy"
    }
  }
}
```

The `authentication_token` must be sent on every subsequent request. It can be in a query parameter called `auth_token`
or in an HTTP header called `Authentication-Token`

### Session Authentication

***

Making API calls while using session authentication requires a CSRF token. Here is a python example 
using session authentication. If your server uses signed certs such as from Let's Encrypt you can remove `verify=False`.

```python
import requests
s = requests.session()
address = "https://<your_server_address>"
r = s.get(f"{address}/api/login", json={}, verify=False)
csrf_token = r.json()['response']['csrf_token']
s.headers['X-XSRF-TOKEN'] = csrf_token
s.headers['Referer'] = address

r = s.post(f"https://{address}/api/login", json={'username': 'administrator', 'password': 'password'}, verify=False)
```

### Whitelisting and Blacklisting Email Domains

***

If email support is enabled, any valid email address can be used to create an account. However, there are whitelists
for email domains and top level domains. Likewise, there are also blacklists. For example, if you add `example.com` to 
the `OTS_EMAIL_DOMAIN_WHITELIST` option, only users with `@example.com` email addresses can register accounts.
You can also add top level domains (TLDs) to the `OTS_EMAIL_TLD_WHITELIST` option. For example, adding `gov` and `mil`
will allow only users with .gov or .mil email accounts to register accounts.

`OTS_EMAIL_DOMAIN_BLACKLIST` and `OTS_EMAIL_TLD_BLACKLIST` are similar except that any email address not in those
lists will be able to register for an account.

## Two-Factor Authentication

***

### TOTP

***

Two-factor authentication can be enabled for any accounts using a TOTP from an authenticator app such as Google Authenticator
([Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_US&gl=US)/[iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)) or
Microsoft Authenticator ([Android](https://play.google.com/store/apps/details?id=com.azure.authenticator)/[iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)).
Click on `Setup 2FA` in the navigation bar and select the authenticator app option. It will generate a code and a QR code.
Either scan the QR code with your authenticator app or copy and paste the code into the authenticator app. Your authenticator
app will give you a PIN that you enter below the QR code.

### Email

***

You can choose to use an email address as your 2FA if your administrator has [enabled](email.md) email support. A code
will be sent to your email address which you will need to enter when you log in.

### Screenshot

***

![!2FA Setup](images/2fa_setup.png)

## SSL Socket Authentication

***

Connecting to OpenTAKServer's SSL socket requires authentication. In ATAK's server setup, tap `Use Authentication`
and enter your username and password. When ATAK connects, it will send an `<auth>` CoT with the username
and password. If the username and password are incorrect, the account is disabled, or no `<auth>` CoT is sent,
OpenTAKServer will close the connection. Two-Factor authentication is not required for the SSL socket.