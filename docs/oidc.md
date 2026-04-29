# OpenID Connect (OIDC)

OpenTAKServer supports OpenID Connect for browser-based single sign-on. It has
been validated end to end with **Authelia**, and it can be used with other
identity providers that expose standard OIDC discovery metadata or explicit
authorization, token, and userinfo endpoints.

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
OTS_OIDC_USERNAME_CLAIMS: preferred_username, upn, email, sub
OTS_OIDC_EMAIL_CLAIM: email
OTS_OIDC_ROLE_CLAIM: groups
OTS_OIDC_SUBJECT_CLAIM: sub
OTS_OIDC_ISSUER_CLAIM: iss
OTS_OIDC_ADMIN_ROLES: administrator
OTS_OIDC_DEFAULT_ROLES: user
OTS_OIDC_TOKEN_ENDPOINT_AUTH_METHOD: ""
OTS_OIDC_INCLUDE_AUTH_TOKEN_IN_CALLBACK_JSON: false
```

If your identity provider does not expose discovery metadata, configure these
values instead of `OTS_OIDC_METADATA_URL`:

```yaml
OTS_OIDC_AUTHORIZATION_ENDPOINT: https://idp.example.com/oauth2/authorize
OTS_OIDC_TOKEN_ENDPOINT: https://idp.example.com/oauth2/token
OTS_OIDC_USERINFO_ENDPOINT: https://idp.example.com/oauth2/userinfo
```

## Web UI and Login Flow

When OIDC is enabled, OpenTAKServer advertises `oidc` in
`SECURITY_USER_IDENTITY_ATTRIBUTES`. The web UI uses that to detect that the
server expects browser OIDC login and starts the flow with `GET /api/oidc/login`
instead of posting credentials to `/api/login`.

In our original deployment, a reverse proxy in front of OpenTAKServer was
responsible for sending the user into the correct OIDC flow. OpenTAKServer now
supports that flow directly, so the web UI no longer depends on proxy-side
routing to enter OIDC.

If both LDAP and OIDC are enabled at the same time, the current web UI behavior
is to prefer OIDC when `oidc` is present.

## Redirect URI

Your identity provider must allow the OpenTAKServer callback URL, for example:

- `https://ots.example.com/api/oidc/callback`

If OpenTAKServer is behind nginx, Traefik, or another reverse proxy, make sure it
forwards `X-Forwarded-Host`, `X-Forwarded-Proto`, and preferably `X-Forwarded-Port`
so OpenTAKServer generates the correct external callback URL.

## Public Clients, Token Endpoint Auth, and PKCE

If you leave `OTS_OIDC_CLIENT_SECRET` empty, OpenTAKServer will treat the OIDC
client as a public client, automatically use `token_endpoint_auth_method=none`,
and enable PKCE with `S256`.

If you want to use PKCE with a confidential client too, set:

```yaml
OTS_OIDC_USE_PKCE: true
OTS_OIDC_PKCE_METHOD: S256
```

If your provider requires a specific token endpoint authentication method, set:

```yaml
OTS_OIDC_TOKEN_ENDPOINT_AUTH_METHOD: client_secret_post
```

If `OTS_OIDC_TOKEN_ENDPOINT_AUTH_METHOD` is left empty for a confidential client,
OpenTAKServer uses the default client behavior instead of forcing `client_secret_post`.

## Username, Email, and Role Mapping

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

Some providers, including Authelia, keep values such as `preferred_username`,
`email`, and `groups` in the userinfo endpoint instead of the ID token.
OpenTAKServer will fetch and merge userinfo claims when available, so those
claims can still be used for username and role mapping.

For example:

```yaml
OTS_OIDC_ROLE_CLAIM: groups
OTS_OIDC_ADMIN_ROLES: ots-admin
OTS_OIDC_DEFAULT_ROLES: user
```

With that configuration:

- a user with `groups=["ots-admin"]` receives the local `administrator` role
- a user with no role claim falls back to the local `user` role

If the provider does send explicit roles or groups for non-admin users, those
roles are synchronized on login. If you want non-admin users to fall back to the
local `user` role, omit the role claim for them or include `user` explicitly if
that is the role you want assigned.

## Account Binding

OpenTAKServer binds OIDC users to a stable identity using:

- issuer
- subject

It does not auto-link users by local email.

It also does not auto-link users by matching a local username.

## Session Cookies and Callback Responses

Browser OIDC callbacks do not work with `SESSION_COOKIE_SAMESITE=strict`. When
OIDC is enabled, OpenTAKServer will relax a strict SameSite setting to `Lax` so
that the browser can complete the callback flow.

The callback can either redirect the browser back to a local path or return JSON
when `return_json=true` is used during login.

OpenTAKServer marks OIDC callback responses as non-cacheable with
`Cache-Control: no-store`.

By default, the callback JSON does not include an auth token. If an older
integration requires it, you can enable:

```yaml
OTS_OIDC_INCLUDE_AUTH_TOKEN_IN_CALLBACK_JSON: true
```

OpenTAKServer also avoids storing provider-issued OIDC tokens in the browser
session cookie.

## Quick Validation

Check that the provider discovery document is reachable:

```shell
curl -s https://idp.example.com/.well-known/openid-configuration | head -n 1
```

Start the login flow in a browser:

```text
https://ots.example.com/api/oidc/login?return_json=true&next=/dashboard
```

For normal browser use through the web UI, users can simply open `/login` and
the UI will route them into `/api/oidc/login` automatically when OIDC is enabled.

After a successful login, the callback should either:

- return JSON when `return_json=true`, or
- redirect to the stored local path

## Related Documentation

- [Authentication](authentication.md)
- [Security](security.md)
- [Certificate Enrollment](certificate_enrollment.md)
