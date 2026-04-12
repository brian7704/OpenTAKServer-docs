# OpenID Connect (OIDC)

OpenTAKServer supports OpenID Connect for browser-based single sign-on. It can be
used with any identity provider that exposes standard OIDC discovery metadata or
explicit authorization, token, and userinfo endpoints.

The relevant OpenTAKServer endpoints are:

- Login: `GET /api/oidc/login`
- Callback: `GET /api/oidc/callback`

OIDC is disabled by default. OpenTAKServer will not use OIDC unless you explicitly
set `OTS_ENABLE_OIDC: true` in your configuration.

If OIDC remains disabled, `GET /api/oidc/login` will return `503` with the message
`OIDC is not enabled`.

## Basic Configuration

Add the following settings to your `config.yml`.

```yaml
OTS_ENABLE_OIDC: true
OTS_OIDC_NAME: oidc
OTS_OIDC_CLIENT_ID: your-client-id
OTS_OIDC_CLIENT_SECRET: your-client-secret
OTS_OIDC_METADATA_URL: https://idp.example.com/.well-known/openid-configuration
OTS_OIDC_SCOPE: openid profile email groups
OTS_OIDC_REDIRECT_URI: /api/oidc/callback
OTS_OIDC_ISSUER: https://idp.example.com
OTS_OIDC_USERNAME_CLAIMS: preferred_username, email, sub
OTS_OIDC_EMAIL_CLAIM: email
OTS_OIDC_ROLE_CLAIM: groups
OTS_OIDC_SUBJECT_CLAIM: sub
OTS_OIDC_ISSUER_CLAIM: iss
OTS_OIDC_ADMIN_ROLES: administrator
OTS_OIDC_DEFAULT_ROLES: user
OTS_OIDC_INCLUDE_AUTH_TOKEN_IN_CALLBACK_JSON: false
```

If your identity provider does not expose discovery metadata, configure these
values instead of `OTS_OIDC_METADATA_URL`:

```yaml
OTS_OIDC_AUTHORIZATION_ENDPOINT: https://idp.example.com/oauth2/authorize
OTS_OIDC_TOKEN_ENDPOINT: https://idp.example.com/oauth2/token
OTS_OIDC_USERINFO_ENDPOINT: https://idp.example.com/oauth2/userinfo
```

## Redirect URI

Your identity provider must allow the OpenTAKServer callback URL, for example:

- `https://ots.example.com/api/oidc/callback`

If OpenTAKServer is behind nginx, Traefik, or another reverse proxy, make sure it
forwards `X-Forwarded-Host`, `X-Forwarded-Proto`, and preferably `X-Forwarded-Port`
so OpenTAKServer generates the correct external callback URL.

## Public Clients and PKCE

If you leave `OTS_OIDC_CLIENT_SECRET` empty, OpenTAKServer will treat the OIDC
client as a public client and automatically enable PKCE with `S256`.

If you want to use PKCE with a confidential client too, set:

```yaml
OTS_OIDC_USE_PKCE: true
OTS_OIDC_PKCE_METHOD: S256
```

## Username and Role Mapping

OpenTAKServer creates or updates local users from OIDC claims.

- `OTS_OIDC_USERNAME_CLAIMS` controls which claims are checked for the local username.
- `OTS_OIDC_EMAIL_CLAIM` controls which claim is used for the local email address.
- `OTS_OIDC_ROLE_CLAIM` controls which claim is used for local role assignment.
- If no roles are found, `OTS_OIDC_DEFAULT_ROLES` is used.
- Roles listed in `OTS_OIDC_ADMIN_ROLES` also grant the local `administrator` role.

For best results, use a username claim such as `preferred_username` that already
matches OpenTAKServer's username rules. If a configured username claim contains
invalid characters such as `@`, `+`, `|`, or `-`, OpenTAKServer will normalize
those characters into `.` before creating the local account.

## Account Binding

OpenTAKServer binds OIDC users to a stable identity using:

- issuer
- subject

It does not auto-link users by local email.

It also does not auto-link users by matching a local username.

## Callback Responses

The callback can either redirect the browser back to a local path or return JSON
when `return_json=true` is used during login.

OpenTAKServer marks OIDC callback responses as non-cacheable with
`Cache-Control: no-store`.

By default, the callback JSON does not include an auth token. If an older
integration requires it, you can enable:

```yaml
OTS_OIDC_INCLUDE_AUTH_TOKEN_IN_CALLBACK_JSON: true
```

## Quick Validation

Check that the provider discovery document is reachable:

```shell
curl -s https://idp.example.com/.well-known/openid-configuration | head -n 1
```

Start the login flow in a browser:

```text
https://ots.example.com/api/oidc/login?return_json=true&next=/dashboard
```

After a successful login, the callback should either:

- return JSON when `return_json=true`, or
- redirect to the stored local path

## Related Documentation

- [Authentication](authentication.md)
- [Security](security.md)
- [Certificate Enrollment](certificate_enrollment.md)
