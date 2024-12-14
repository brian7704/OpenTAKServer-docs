![GitHub Release Date](https://img.shields.io/github/release-date/brian7704/OpenTAK_ICU)
![GitHub Release](https://img.shields.io/github/v/release/brian7704/OpenTAK_ICU)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fbrian7704%2FOpenTAK_ICU&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/brian7704/OpenTAK_ICU/total)



# OpenTAK ICU

***

OpenTAK ICU is a video streaming app based on [RootEncoder](https://github.com/pedroSG94/RootEncoder) 
that can stream audio and video to RTSP(S), RTMP(S), and SRT servers such as 
[MediaMTX](https://github.com/bluenviron/mediamtx). Its primary focus is to work with the TAK ecosystem.

## Why?

***

While ATAK already has the TAK ICU plugin, it doesn't seem to support a few features. Specifically
it doesn't support streaming audio or using authentication and encryption (RTSPS) at the same time.

## Download

***

Get the APK from this repo's [latest release](https://github.com/brian7704/OpenTAK_ICU/releases/latest)

## Features

***

- Video Codecs
    - H264
    - H265
    - AV1
- Audio Codecs
    - AAC
    - G711
    - OPUS
- Streaming protocols
    - RTSP
    - RTSPS
    - RTMP
    - RTMPS
    - SRT (SRT does not yet support authentication)
    - Multicast UDP
- Authentication
- Servers with self-signed certificates
- Background streaming and recording - Continue streaming and recording audio and video even if the app
is minimized or the screen is off.
- Record video to the device while streaming
- Take photos while recording or streaming
- Change between front and back cameras during stream
- Adaptive bitrate
- UVC Cameras
- Optional text overlay with GPS location and timestamp
- Support for devices with built-in IR cameras
    - Tested on the Ulefone Armor X13, Armor 22, and Armor 26 Ultra
    - Requires root
- Video filters

## Planned features

***

- KLV
- Stream your device's screen instead of camera

## Servers

***

This app has been developed using [MediaMTX](https://github.com/bluenviron/mediamtx) as the 
streaming server but any RTSP/RTMP server should work.

## Viewing OpenTAK ICU streams from MediaMTX in ATAK

***

In the video tool, tap the + symbol to add a new stream and use the following settings:
- Type: rtsp
- Address: Your server's IP address or domain name
- Port: The defaults are 8554 for RTSP and 8322 for RTSPS
- Path: The stream's path that is set in OpenTAK ICU's settings
- Username/Password: Required only if your server enforces authentication
- Reliable P2P Connection: Enables a TCP connection and is required if there is a NAT/firewall
  between your EUD and the server.

## Viewing the stream in a browser

***

When using MediaMTX and streaming with H264, you can watch the live stream in a browser by going to

`http://your_server_ip:8888/stream_path` 

for an HLS stream or

`http://your_server_ip:8889/stream_path`

for a WebRTC stream. Note that most browsers don't yet
support H265. See [CanIUse](https://caniuse.com/hevc) for details. Also note that WebRTC does not
support AAC audio so you will need to use OPUS or G711 if you're viewing the stream via WebRTC.

## Viewing streams in VLC

***

1. Click on Media -> Open Network Stream
2. In the URL field enter `rtsp://your_server_address:8554/your_path`
3. Click Play

## Adaptive Bitrate

***

When adaptive bitrate is enabled, the video bitrate will change based on your network/internet connection.
If the connection can't send packets fast enough, the bitrate will lower. If the connection is good
the bitrate will max out at what the bitrate setting's value is.

## Servers with self-signed certificates

***

If your server is using self signed certificates and you wish to stream encrypted audio and video,
you'll need your server's trust store certificate in PKCS12 (.p12 file extension) format. If your 
RTSP server is using the same certificates as your TAK server, you can use the same trust store 
certificate and certificate password in OpenTAK ICU. After selecting the certificate and providing
the certificate password, press the Test Certificate button. This simply validates that the certificate
is the correct format and that the password is correct.

## Feature Comparison

***

### Streaming Protocols

***

|               | TAK ICU | OpenTAK ICU |
|---------------|---------|-------------|
| RTSP          | Yes     | Yes         |
| RTSPS         | No      | Yes         |
| RTMP          | No      | Yes         |
| RTMPS         | No      | Yes         |
| SRT           | No      | Yes         |
| Multicast UDP | Yes     | Yes         |

### Video Codecs

***

|      | TAK ICU | OpenTAK ICU |
|------|---------|-------------|
| H264 | Yes     | Yes         |
| H265 | No      | Yes         |
| AV1  | No      | Yes         |

### Audio Codecs

***

|      | TAK ICU | OpenTAK ICU |
|------|---------|-------------|
| AAC  | No      | Yes         |
| G711 | No      | Yes         |
| OPUS | No      | Yes         |

### Other Features

***

|                                      | TAK ICU                    | OpenTAK ICU              |
|--------------------------------------|----------------------------|--------------------------|
| Broadcast CoT on local network       | Yes                        | Yes                      |
| Send CoT to TAK server               | No                         | Yes                      |
| Show video on map (KLV)              | Yes                        | No                       |
| View video in ATAK/WinTAK video tool | Yes                        | Yes                      |
| Stream to Wowza                      | Yes                        | No                       |
| Stream in background                 | Yes                        | Yes                      |
| Take a photo while streaming         | Yes                        | Yes                      |
| Switch camera while streaming        | No                         | Yes                      |
| Turn on flashlight while streaming   | No                         | Yes                      |
| Record to device while streaming     | Yes                        | Yes                      |
| Change Video/Audio bitrate           | No                         | Yes                      |
| Adaptive Bitrate                     | No                         | Yes                      |
| 1080p                                | No                         | Yes                      |
| 4K                                   | Yes                        | Yes                      |
| Change FPS                           | No                         | Yes                      |
| Compass Display                      | Yes                        | No                       |
| Server Authentication                | Yes (only when using RTSP) | Yes (RTSP(S) and RTMP(S) |
| UVC Camera Support                   | No                         | Yes                      |
| Video Filters                        | No                         | Yes                      |
| Text Overlay                         | No                         | Yes                      |