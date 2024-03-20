# OpenTAKServer-Installer

---

All the installers are on [GitHub](https://github.com/brian7704/OpenTAKServer-Installer). Download the latest
release or clone the repo
```
git clone https://github.com/brian7704/OpenTAKServer-Installer.git
```

## Notes

***

For better security, OpenTAKServer should not be run as root. The installer will exit when run as root.

## Features

***

### Certificates

***

The installer will generate a CA and all the keys you need to get the server started. It will also configure the
certificate authority automatically.

### Let's Encrypt

***

If you have a domain name for your server you can use a Let's Encrypt certificate to secure the web UI.

Follow [Certbot's](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal) instructions on how to obtain a certificate. 
In order for this to work, the domain name should be pointed at your server's public IP address and 
ports 80 and 443 should be open on your server. See
[Let's Encrypt](https://letsencrypt.org/getting-started/) for more details.

After running certbot, open `/etc/nginx/site-enabled/ots_proxy` in a text editor. In the fist `server` section you may
see an if statement that certbot added which will look like this:

```
    if ($host = yourdomain.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot
```

Either change it or add the following if it doesn't exist:

```
    if ($server_port = 80) {
        return 301 https://$host$request_uri;
    } # managed by Certbot
```

This will cause web browsers to redirect to the HTTPS version of the site when they try to access it via HTTP on port 80.
However, it will not redirect HTTP requests from ATAK and WinTAK on port 8080. Redirecting those requests would cause
errors in ATAK and WinTAK.

### ZeroTier

***

You can optionally install [ZeroTier](https://www.zerotier.com/) with the installer. If you plan to do so, make sure 
you already have an account and a network ID before running the installer. The installer will ask for your network ID 
so it can join the network automatically.

### MediaMTX

***

This installer will install the latest binaries for [MediaMTX](https://github.com/bluenviron/mediamtx) and make the 
appropriate configuration changes in order to work with OpenTAKServer

### Email support

***

OpenTAKServer can be optionally configured to require users to register using an email account. Users will be emailed to
confirm their registration, reset their passwords, and optionally for two-factor authentication codes. If this option is
enabled, you will need your mail server's address, port, username, and password. When using Gmail you will need to
log into your Gmail account and enable an app password. Your normal password will not work. Other providers probably
require you to take similar steps. You can find the required settings for Gmail [here](https://docs.opentakserver.io/#email/#gmail).
