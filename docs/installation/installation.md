# OpenTAKServer-Installer

***

All the installers are on [GitHub](https://github.com/brian7704/OpenTAKServer-Installer).

## Ubuntu and Raspberry Pi

***

The Ubuntu and Raspberry pi installers should be run as a regular user, not root. 

Copy and paste the following command into your terminal for the Ubuntu installer.

```shell
curl https://i.opentakserver.io/ubuntu_installer -L | bash - | tee ots_ubuntu_installer.log
```

Use the following command for the Raspberry Pi installer. The installer supports Raspberry Pi OS Bookworm or newer versions.

```shell
curl https://i.opentakserver.io/raspberry_pi_installer -L | bash - | tee ots_rpi_installer.log
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

### ZeroTier

***

You can optionally install [ZeroTier](https://www.zerotier.com/) with the installer. If you plan to do so, make sure 
you already have an account and a network ID before running the installer. The installer will ask for your network ID 
so it can join the network automatically.

### MediaMTX

***

This installer will install the latest binaries for [MediaMTX](https://github.com/bluenviron/mediamtx) and make the 
appropriate configuration changes in order to work with OpenTAKServer
