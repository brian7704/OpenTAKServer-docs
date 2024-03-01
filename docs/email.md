# Email

***

OpenTAKServer uses [Flask-Mail](https://pythonhosted.org/Flask-Mail/) is used to handle emails. 
Enabling email support also enables the following features:

- User account self registration
- Password reset - Without email, only administrators can change a user's password if they forget it
- Two-factor authentication via email

## Enabling Email Support

***

The following settings are required to enable email support. You can find them in your `config.yml` file.

- `OTS_ENABLE_EMAIL`: Other settings have no effect is this is set to `false`
- `MAIL_SERVER`
- `MAIL_PORT`
- `MAIL_USERNAME`
- `MAIL_PASSWORD`

These settings are optional and will depend on the email service you use.

- `MAIL_USE_SSL`
- `MAIL_USE_TLS`

## Gmail

***

If you plan to use a Gmail account to send emails, you will need to log into your account and enable an app password. Your
regular password will not work in OpenTAKServer. See [Google's documentation](https://support.google.com/accounts/answer/185833?hl=en) 
for details.

### Gmail settings

***

| Setting        | Value                     |
|----------------|---------------------------|
| **MAIL_SERVER** | `smtp.gmail.com`          |
| **MAIL_PORT**  | `587`                     |
|**MAIL_USE_SSL**| `false`                   |
|**MAIL_USE_TLS**| `true`                    |
|**MAIL_USERNAME**| `your_username@gmail.com` |
|**MAIL_PASSWORD**| `your_app_password`       |