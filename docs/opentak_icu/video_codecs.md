# Video Codecs
---

## Hardware Encoding
---
OpenTAK ICU uses your device's hardware video encoders. If your device doesn't have an encoder for a particular codec
you will have to choose a different one.

## H264
---
H264 is widely supported both in Android devices and web browsers. Use this codec for the best compatibility.

## H265
---
H265 offers better compression than H264 which means a better quality video with less bandwidth required. 
However, many web browsers still don't support it. Therefore, it's recommended to use H264 if you plan to view the stream
in a browser. But if you will view the stream another way, such as [VLC](https://www.videolan.org/), H265 is preferred.

## AV1
---
AV1 is supported by all streaming protocols. However, most devices do not have a hardware AV1 encoder. At the time of this
writing (February 2024), the Google Pixel 8 and Pixel 8 Pro seem to be the only devices with AV1 hardware encoders. But as
of Android 14 Google is enforcing AV1 support. This means that if you are on Android 14 or greater you can use AV1 in 
OpenTAK ICU, but if your device doesn't have a hardware encoder Android will use a software encoder which will probably
drain the battery faster. AV1 is not supported when streaming via SRT.

## Compatibility Matrix
|        | H264 | H265 |AV1|
|--------|------|------|--|
| RTSP(S) | Yes  | Yes  |Yes|
|RTMP(S)|Yes| No   |Yes|
|SRT|Yes| Yes  |No|