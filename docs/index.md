# OpenTAKServer

***

![PyPI - Downloads](https://img.shields.io/pypi/dm/opentakserver)
![PyPI - Version](https://img.shields.io/pypi/v/opentakserver)
![Discord](https://img.shields.io/discord/1183578214459777164?logo=discord&label=Discord&link=https%3A%2F%2Fdiscord.gg%2F6uaVHjtfXN)
![GitHub Release Date](https://img.shields.io/github/release-date/brian7704/OpenTAKServer)

OpenTAKServer (OTS) is yet another open source TAK Server for ATAK, iTAK, and WinTAK. OTS's goal is to be easy to install and use, and to run on both servers and SBCs (ie Raspberry Pi).

This is a new project under active development. Feel free to report any bugs or feature requests to our [GitHub repo](https://github.com/brian7704/OpenTAKServer).  You can also join us on our [Discord server](https://discord.gg/6uaVHjtfXN)

## Current Features

***

- Support for ATAK 4.8 and up (Older versions may work, needs to be tested)
- WinTAK support
- iTAK support
- TCP and SSL CoT streaming
- Authentication
    - Optional support for user registration with an email account
    - Two-factor authentication via TOTP authenticator or email
- Client certificate enrollment
- CoT routing between EUDs
- [MediaMTX](https://github.com/bluenviron/mediamtx) integration for video streaming
    - Streams secured via SSL and authentication
    - Stream video from TAK ICU and [OpenTAK ICU](https://github.com/brian7704/OpenTAK_ICU)
    - Stream video from drones
    - Connect to IP cameras
    - Watch video streams in ATAK's video tool, web browser, or video player such as VLC
    - Record streams
- Upload data packages to share with other EUDs
- Live stream ADS-B data from the free Airplanes.live API to EUDs
- WebUI
- Mumble Authentication 
    - Use your OpenTAKServer account to log into your Mumble server

## Supported Platforms

***

There are installer scripts for Ubuntu, Raspberry Pi, and Windows in the OpenTAKServer-Installer repo. Other Linux 
distros will probably work via manual installation. If you'd like an installer for a particular distro, feel free to
open an issue in the [OpenTAKServer-Installer repo](https://github.com/brian7704/OpenTAKServer-Installer/issues). There 
are plans for MacOS and Android installers in the future.

## Planned Features
***
- Federation
- DataSync
- Pull data from networked SDRs (ie dump1090, rtl_ais, rtl_tcp, etc)

## Supporting The Project

***

If you'd like to support this project you can contribute [here](https://buymeacoffee.com/opentakserver). Contributions
are voluntary and never required. OpenTAKServer will always remain free and open source.