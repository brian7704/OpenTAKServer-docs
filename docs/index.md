# OpenTAKServer

***

OpenTAKServer (OTS) is yet another open source TAK Server for ATAK, iTAK, and WinTAK. OTS's goal is to be easy to install and use, and to run on both servers and SBCs (ie Raspberry Pi).

This project is just beginning and not yet suitable for production.

## Current Features

***

- ATAK 4.8 - 5.0 support
- WinTAK support
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

## Planned Features

***

- Federation
- DataSync
- iTAK support
- Pull data from networked SDRs (ie dump1090, rtl_ais, rtl_tcp, etc)

