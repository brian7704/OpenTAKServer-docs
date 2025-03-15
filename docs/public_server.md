# Public Server

***

There is a publicly available OpenTAKServer available for evaluation purposes at <https://public.opentakserver.io>.
See [Certificate Enrollment](certificate_enrollment.md) for instruction to connect to the public server with ATAK.

## Account Registration

***

Account registration is required for all functionality except connecting with ATAK via TCP. You can get an account in 
two ways. Either sign up using an email address (it can be a temporary email) or contact us on our 
[Discord server](https://discord.gg/6uaVHjtfXN) and an admin can create one without the need for an email address.

## ATAK Settings for TCP

***

In ATAK, add a new server. The only settings you need are the address, `public.opentakserver.io`, the port which is `8088`,
and the protocol which is `TCP`. Note that any data transmitted between your EUD and this server will not be encrypted
when using TCP.
