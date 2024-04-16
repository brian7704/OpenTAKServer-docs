# OpenTAKServer-Installer

***

All the installers are on [GitHub](https://github.com/brian7704/OpenTAKServer-Installer).

## Ubuntu and Raspberry Pi

***

The Ubuntu and Raspberry pi installers should be run as a regular user, not root. Copy and paste the following command into your terminal for the Ubuntu installer.

`curl https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/ubuntu_installer.sh | bash -`

Use the following command for the Raspberry Pi installer. The installer supports Raspberry Pi OS Bookworm or newer versions.

`curl https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/raspberry_pi_installer.sh | bash -`

## Notes

***

For better security, OpenTAKServer should not be run as root. The installer will exit when run as root.

## Features

***

### Certificates

***

The installer will generate a CA and all the keys you need to get the server started. It will also configure the
certificate authority automatically.

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
