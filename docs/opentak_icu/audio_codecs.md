# Audio Codecs

***

## OPUS

***

The OPUS codec is supported when streaming in RTSP(S), SRT, and Multicast UDP protocols. If you will be viewing the 
stream in a web browser via WebRTC, use this codec for the best quality.

## AAC

***

AAC is supported in all streaming protocols. If you will be viewing the stream in a web browser make sure to view it via
HLS. HLS supports AAC audio while WebRTC does not.

## G711

***

The G711 codec is locked to a sample rate of 8000hz and mono audio. Both RTSP(S) and RTMP(S) support G711 while SRT does not.

## Compatibility Matrix

***

||OPUS| AAC |G711|
|--|--|-----|--|
| RTSP(S) |Yes| Yes |Yes|
| RTMP(S) |No| Yes |Yes|
| SRT     |Yes| Yes |No|
|Multicast UDP|Yes|Yes|No|