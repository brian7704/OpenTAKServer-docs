# Video Filters

***

OpenTAK ICU supports a number of video filters provided by the [RootEncoder](https://github.com/pedroSG94/RootEncoder) library.
These filters can be enabled and disabled while streaming from either the devices front or back cameras, or from a UVC camera.

# Text Overlay Filter

***

The text overlay filter will add the stream path, GPS location, and current timestamp to the bottom left
corner of the video. There is an option under Settings → Video Settings → Text Overlay Time Zone to switch
between UTC and your local time zone.

# Chroma Key Filter

***

The chroma key filter will replace a green background with either the default background image or an image of your choice.
To set the image, tap on Settings → Video Settings → Chroma Key Background and choose any image on your device. This
filter requires a bright green background. You can test it by enabling the filter in OpenTAK ICU and pointing your camera
at the green rectangle below. You should see the default background or the image you selected.

![!Chroma Key Test](../images/chroma_key.png)