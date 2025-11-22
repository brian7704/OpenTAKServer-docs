# Data Packages

## Uploading Data Packages Zip files

Data package zip files can be uploaded via OpenTAKServer's web UI. When they are uploaded, EUDs can download them
via the data package tool.

## Sending Data Packages from EUDs

OpenTAKServer will automatically store a copy of and data package sent out by EUDs.

## Automatic Data Package Creation

`png`, `jpg`, `jpeg`, and `xml` files can also be uploaded on the Data Packages page in the web UI. When they're uploaded,
OpenTAKServer will automatically create data package zip files for them. If an image has
GPS coordinates set in its EXIF data, it will automatically show on the EUD's map when it is downloaded.

## Install on Enrollment and Connection

On the data package page in the web UI there are switches for data package installation on certificate enrollment
and on server connection. If the enrollment switch is enabled, the data package will be automatically installed on the
EUD upon a successful certificate enrollment. Likewise, if the connection switch is enabled, the data package will be automatically
installed the next time the EUD connects. One or both of these options can be enabled for each data package

## ATAK Settings for Installation on Connection

If an EUD is initially connected to OpenTAKServer via certificate enrollment or a data package, the
`Apply TAK Server Profile Updates` option in ATAK will be automatically enabled. Otherwise, you will need to manually
enable it. It can be found under Settings->Network Preferences->Network Connection Preferences.

When ATAK connects to a server and this option is enabled, it makes a call to `/Marti/api/device/profile/connection`
with an optional `syncSecago` parameter. `syncSecago` is a integer representing the number of seconds since that EUD
last connected to the server. If it's present, OpenTAKServer will only send the EUD new or changed data packages
between the current time and the last time the EUD connected.