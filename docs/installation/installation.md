# OpenTAKServer-Installer

---

All the installers are on [GitHub](https://github.com/brian7704/OpenTAKServer-Installer). Download the latest
release or clone the repo
```
git clone https://github.com/brian7704/OpenTAKServer-Installer.git
```

## Notes

For better security, OpenTAKServer should not be run as root. The installer will exit when run as root.

## Features

### Certificates

This installer will generate a CA and all the keys you need to get the server started. It will also do all the
configuration automatically.

### Let's Encrypt

The installer will prompt you for your server address. If you're using a domain name, the installer will ask if you
would like to get a certificate from Let's Encrypt. This certificate will be used for OpenTAKServer's web GUI,
MediaMTX video encryption, etc. Pretty much everything except the CoT SSL streaming port (8089).

Please note that in order for this to work, the domain name should be pointed at your server's public IP address and 
ports 80 and 443 should be forwarded to your server. See
[Let's Encrypt](https://letsencrypt.org/getting-started/) and 
[Certbot](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal) for more details.

### ZeroTier

You can optionally install [ZeroTier](https://www.zerotier.com/) with this installer. If you plan to do so, make sure 
you already have an account and a network ID before running the installer. The installer will ask for your network ID 
so it can join the network automatically.

### MediaMTX

This installer will install static binaries for [MediaMTX](https://github.com/bluenviron/mediamtx) and make the 
appropriate configuration changes in order to work with OpenTAKServer

### Email support

OpenTAKServer can be optionally configured to require users to register using an email account. Users will be emailed to
confirm their registration, reset their passwords, and optionally for two-factor authentication codes. If this option is
enabled, you will need your mail server's address, port, username, and password. When using Gmail you will need to
log into your Gmail account and enable an app password. Your normal password will not work. Other providers probably
require you to take similar steps.
