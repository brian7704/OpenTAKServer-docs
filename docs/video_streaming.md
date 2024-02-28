# Video Streaming

***

OpenTAKServer uses [MediaMTX](https://github.com/bluenviron/mediamtx) for video streaming and recording. It accepts
streams from apps such as OpenTAK ICU and TAK ICU, as well as devices like drones and IP Cameras.

## Streaming Protocols

***

You can stream to MediaMTX using a variety of protocols:

- RTSP(S)
- RTMP(S)
- SRT
- HLS
- WebRTC
- UDP Multicast

## Recording Streams

***

To record a stream, simply click on the stream's record switch. You can do this during a stream or while not streaming.
Recording automatically starts when a stream goes live and stops one the stream stops. Recorded videos will be in
`~/ots/mediamtx/recordings/<path_name>` by default. You can watch and download recording by clicking `Video Recordings`
in the navigation bar.

## Screenshot

***

![!Video Streams](images/video_streams.png)