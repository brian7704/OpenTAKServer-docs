# Mumble

OpenTAKServer supports acting as an authentication provider for a Mumble server. This forces Mumble clients to connect
using their OpenTAKServer username and password. It also prevents anyone without an account on your OpenTAKServer, 
or an account that has been disabled by an administrator, from connecting.

## OpenTAKServer Configuration

Enable Mumble authentication by setting `OTS_ENABLE_MUMBLE_AUTHENTICATION` to `true` in your `config.yml`. It will 
connect to Mumble's Ice server at 127.0.0.1:6502.

## Mumble Configuration

In your Mumble server's config file, make sure you uncomment or add this line `ice="tcp -h 127.0.0.1 -p 6502"`