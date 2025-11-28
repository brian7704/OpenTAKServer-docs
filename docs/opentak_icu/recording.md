# Recording

OpenTAK ICU supports recording video files to the local device while streaming. Note that for audio, only the AAC codec
is supported. If OPUS or G711 codecs are used, the video will record without audio.

There is also support for recording without streaming. Simply disable the `Stream video` in `Streaming Settings` and enable
`Record video to this device` in `Video Settings`. Also make sure that the audio codec is set to AAC.