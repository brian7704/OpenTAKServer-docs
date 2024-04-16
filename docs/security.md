# Security

***

For enhanced security, it is recommended that you disable the TCP CoT streaming port and disable nginx from listening
for unencrypted HTTP requests on ports 80 and 8080. All data sent and received over these ports is unencrypted.
Any third party that intercepts the data will be able to see things such as EUD locations, passwords, geochats,
and other data in the clear. To disable the TCP CoT streaming port, simply click the switch in the TCP box
of the UI's dashboard, or set the `OTS_ENABLE_TCP_STREAMING_PORT` option to `false` in `config.yml`

Another concern is the Marti API. When ATAK and WinTAK query the Marti API on port 8080, they do not use any authentication.
This means that any third party that can access port 8080 on your server can interact with the Marti API and do things
such as upload/download data packages, query video feeds, get a list of EUDs, etc, all without any authentication.
When querying the Marti API over HTTPS on port 8443, ATAK sends a client certificate which the server will verify.
These certificates can only be obtained by [certificate enrollment](certificate_enrollment.md) which requires a
username and password, or by having an administrator generate a certificate data package and giving it to a user.
To stop nginx from listening on ports 80 and 8080, delete `/etc/nginx/sites-enabled/ots_http` and restart
nginx by running `sudo systemctl restart nginx`.