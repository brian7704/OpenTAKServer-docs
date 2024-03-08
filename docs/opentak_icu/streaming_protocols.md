# Streaming Protocols

***

## RTSP(S)

***

RTSP is OpenTAK ICU's default protocol and supports both TCP and UDP. If you're using TCP you can optionally enable
RTSPS encryption. RTSP over UDP does not support encryption. 

## RTMP(S)

***

RTMP supports H264, H265, and AV1 video codecs as well as AAC and G711 audio codecs.

## SRT

***

SRT supports H264 and H265 video codecs, as well as ACC and OPUS audio codecs. It does not support authentication yet.

## Multicast UDP

***

Multicast UDP can be used to stream over your local network virtual network services such as ZeroTier and TailScale.
No server is required when using Multicast. When your device has a location fix, OpenTAK ICU will send Multicast
CoT messages which will put a sensor icon with its field of view on other EUD's in the same network.

### Valid Multicast IPs

***

The Multiicast IP range is 224.1.0.0 - 239.255.255.255, however some IPs and IP ranges are reserved and cannot be used.
Most IPs in the 232.0.0.0 - 239.255.255.255 range are safe to use. See this [Wikipedia article](https://en.wikipedia.org/wiki/Multicast_address)
for more details. 