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