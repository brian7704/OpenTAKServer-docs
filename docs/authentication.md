# Authentication

***

OpenTAKServer uses [Flask-Security](https://flask-security-too.readthedocs.io/en/stable/) to provide authentication.

## Administrator Account

***

When you start OpenTAKServer for the first time, an administrator account is automatically created. The username
is ```administrator``` and the password is ```password```. You should immediately change the password when you first log in.

## Creating Accounts

***

By default, only administrators can create user accounts. However, users can register their own accounts if an administrator
enables [email](email.md) support.

## Two-Factor Authentication

***

Two-factor authentication can be enabled for any accounts using a TOTP from an authenticator app such as Google Authenticator
([Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_US&gl=US)/[iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)) or
Microsoft Authenticator ([Android](https://play.google.com/store/apps/details?id=com.azure.authenticator)/[iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)).
Click on ```Setup 2FA``` in the navigation bar and select the authenticator app option. It will generate a code and a QR code.
Either scan the QR code with your authenticator app or copy and paste the code into the authenticator app. Your authenticator
app will give you a PIN that you enter below the QR code.
![!2FA Setup](images/2fa_setup.png)

## SSL Socket Authentication

***

Connecting to OpenTAKServer's SSL socket requires authentication. In ATAK's server setup, tap ```Use Authentication```
and enter your username and password. When ATAK connects, it will send an ```<auth>``` CoT with the username
and password. If the username and password are incorrect, the account is disabled, or no ```<auth>``` CoT is sent,
OpenTAKServer will close the connection.