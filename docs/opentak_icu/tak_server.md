# TAK Server

OpenTAK ICU can connect to a TAK server and send Cursor-on-Target messages in XML. This will show a sensor icon on the maps 
of all EUDs connected to the server. The icon will also show the field of view of the camera. Additionally, OpenTAK ICU
will send an HTTP POST request to your server's /Marti/vcm API endpoint. This allows EUDs to download the video stream details
in the video tool.

## TCP

If you're using TCP the only settings that are required are the server address and the port. The port defaults to 8088.

## SSL

If your server requires SSL, tap the `Connect to ATAK Server via SSL` switch. You'll then need to specify your trust store
and client certificates, along with their passwords. These are the same certificates and passwords you use to connect
ATAK to your TAK server. Once specifying both certs, make sure to tap the `Test Certificate` option to validate that
the certificates are in the right format and the password is correct.

## Authentication

If your TAK server requires authentication, tap the `Enable ATAK Authentication` switch and input your username and password.

## TAK Servers Tested

OpenTAK ICU has been tested and works with the official [tak.gov](https://tak.gov/) TAK server, 
[OpenTAKServer](https://github.com/brian7704/OpenTAKServer) and [FreeTAKServer](https://github.com/FreeTAKTeam/FreeTakServer).