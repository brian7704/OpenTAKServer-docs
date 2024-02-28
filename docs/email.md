# Email

***

Email support is disabled by default. Enabling it also enables the following features:

- User account self registration
- Password reset - Without email, only administrators can change a user's password if they forget it
- Two-factor authentication via email

## Enabling Email Support

***

1. Log in as an administrator
2. Click on `Settings` in the navigation bar
3. Find `OTS_ENABLE_EMAIL` and click on the toggle 
4. Scroll down to the email settings at the bottom of the page
5. `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, and `MAIL_PASSWORD` are all required. If your email server or service
uses TLS or SSL, make sure to enable `MAIL_USE_SSL` or `MAIL_USE_TLS`

## Gmail

***

If you plan to use a Gmail account to send emails, you will need to log into your account and enable an app password. Your
regular password will not work in OpenTAKServer. See [Google's documentation](https://support.google.com/accounts/answer/185833?hl=en) 
for details.

### Gmail settings

***

| Setting        | Value            |
|----------------|------------------|
| **MAIL_SERVER** | `smtp.gmail.com` |
| **MAIL_PORT**  | `465`            |
|**MAIL_USE_SSL**|`True`|
|**MAIL_USE_TLS**|`False`|
|**MAIL_USERNAME**|`your_username@gmail.com`|
|**MAIL_PASSWORD**|`your_app_password`|