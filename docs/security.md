# Security

For enhanced security, it is recommended that you disable the TCP CoT streaming port and disable nginx from listening
for unencrypted HTTP requests on ports 80 and 8080. All data sent and received over these ports is unencrypted.
Any third party that intercepts the data will be able to see things such as EUD locations, passwords, geochats,
and other data in the clear. To disable the TCP CoT streaming port, simply click the switch in the TCP box
of the UI's dashboard, or set the `OTS_ENABLE_TCP_STREAMING_PORT` option to `false` in `config.yml`

Another concern is the Marti API. When TAK clients query the Marti API on port 8080, they do not use any authentication.
This means that any third party that can access port 8080 on your server can interact with the Marti API and do things
such as upload/download data packages, query video feeds, get a list of EUDs, etc, all without any authentication.
When querying the Marti API over HTTPS on port 8443, TAK clients sends a client certificate which the server will verify.
These certificates can only be obtained by [certificate enrollment](certificate_enrollment.md) which requires a
username and password, or by having an administrator generate a certificate data package and giving it to a user.
To stop nginx from listening on ports 80 and 8080, delete `/etc/nginx/sites-enabled/ots_http` and restart
nginx by running `sudo systemctl restart nginx`.

## Blocking Port Scanning Bots

The [ipsum](https://github.com/stamparm/ipsum) GitHub repo maintains a list of malicious IP addresses that updates daily.
Blocking these IP addresses can be done with the following bash script that is run via a cron job.

```shell
#!/bin/bash
ipset -q flush ipsum
ipset -q create ipsum hash:ip
for ip in $(curl --compressed https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt 2>/dev/null | grep -v "#" | grep -v -E "\s[1-2]$" | cut -f 1); do ipset add ipsum $ip; done
iptables -D INPUT -m set --match-set ipsum src -j DROP 2>/dev/null
iptables -I INPUT -m set --match-set ipsum src -j DROP
```

### Setting up the ipsum Script

1. Copy and paste the above script to a file somewhere on your server, for example `/opt/ipsum.sh`.
2. Make the script executable `sudo chmod +x /opt/ipsum.sh` (substitute `/opt/ipsum.sh` with the actual location you saved the script to)
3. Add a cron job to run every day at midnight
   1. `sudo crontab -e`
      2. Add the following line to the bottom of the crontab file `0 0 * * * /opt/ipsum.sh`
      3. Save the crontab file. If you're using `nano`, press `ctrl+o` to save, press `enter` to confirm, then `ctrl+x` to exit

## IPTables Rules

The following IPTables ruleset opens all ports used by OpenTAKServer and blocks all others. It also includes the ipsum ruleset.
You can add or remove rules from this list as needed. After saving the rules to a file, you can load them with this command
`iptables-restore < /path/to/iptables.rules`

Which rules to enable depends on which components you're using. The list of all services is available in [Architecture](architecture.md). 
At a minimum, you'll need to open 8443, 443, 8089, and 8446 for TAK to work, and 8080, 80, and 8088 if you're using TCP.

```shell
*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [11996:8975838]
-A INPUT -i lo -j ACCEPT
-A INPUT -m set --match-set ipsum src -j DROP
-A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A INPUT -p tcp -m tcp --dport 64738 -j ACCEPT
-A INPUT -p udp -m udp --dport 64738 -j ACCEPT
-A INPUT -p udp -m udp --dport 8890 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8889 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8888 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8883 -j ACCEPT
-A INPUT -p udp -m udp --dport 8554 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8554 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8322 -j ACCEPT
-A INPUT -p udp -m udp --dport 8189 -j ACCEPT
-A INPUT -p udp -m udp --dport 8001 -j ACCEPT
-A INPUT -p udp -m udp --dport 8000 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 1936 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 1935 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 1883 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8089 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8088 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8080 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8446 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 8443 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 443 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
-A INPUT -j DROP
COMMIT
```

Once the rules are loaded, install the `iptables-persistent` package in Ubuntu to re-apply them after every reboot.
