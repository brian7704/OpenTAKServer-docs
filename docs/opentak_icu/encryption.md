# Encryption

***

OpenTAK ICU supports encryption when streaming with either RTSPS or RTMPS. This ensures that a 3rd party cannot intercept
and view the stream while it's in transit to the server.

## CA Signed Certificates

***

If your server uses certificates signed by a trusted CA such as Let's Encrypt, simply choose the RTSPS or RTMPS protocl.
No further action is required.

## Self-Signed Certificates

***

If your server uses self-signed certificates you will need to import them into OpenTAK ICU. The certificates should be
in PKCS12 format, the same format that ATAK uses. To import them, use the following steps:

1. Copy your trust store and user certificates to your device
2. Tap the Settings icon
3. Tap Stream Settings
4. Tap the "Server uses Self-Signed Certificate" switch
5. Tap Trust Store Certificate and locate it
6. Tap Trust Store Certificate Password and enter it. If you're using the same certificates as your TAK server, the password is probably 'atakatak'
7. Tap "Test Certificate". This step is required and validates that the certificate is a valid PKCS12 certificate and that the password is correct