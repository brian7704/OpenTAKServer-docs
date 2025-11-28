# UVC Cameras

OpenTAK ICU supports UVC cameras connected via USB such as the [MOHOC 2](https://www.mohoc.com/product/mohoc-2-usb-uvc/).
Any UVC cameras, includes cameras supported by HelmCam, should work. If you try a camera please let us know if it worked or not
on the [Discord server](https://discord.gg/6uaVHjtfXN) or by opening an issue on the [GitHub repo](https://github.com/brian7704/OpenTAK_ICU/issues).

## Usage

When you connect your camera to your phone via USB, a dialog box will pop up asking if you want to all OpenTAK ICU to use
it. When you click yes, OpenTAK ICU will open automatically if it's not already opened.

To switch to the UVC camera instead of the device's internal cameras, either tap the settings button 
(looks like ⚙) → Video Settings → Video Source → UVC camera, or tap the three vertical dots icon 
(looks like ⋮) → Video Source → UVC Camera.

When switching to the UVC Camera source, the camera does not have to be connected. If it is not connected you will see
a black screen where the video should be. The video will start automatically when the camera is connected. Likewise,
the camera can be disconnected and video will restart automatically when it is reconnected.

## Setting Resolution

OpenTAK ICU doesn't automatically detect the UVC camera's resolution. To set the resolution manually, tap on settings  (looks like ⚙)
→ Video Settings → UVC Camera Resolution Width and UVC Camera Resolution Height. If those options are greyed out,
tap the Video Source option and choose UVC camera. Check your camera's documentation for the best resolution. The default
resolution in OpenTAK ICU is 1920x1080.

## Audio

Only video is supported from UVC cameras. If your camera has audio capabilities, they will not be used. Instead, audio
will come from your device's internal microphone.

## Flashlight

Your device's built-in flashlight can be enabled when using a UVC camera.