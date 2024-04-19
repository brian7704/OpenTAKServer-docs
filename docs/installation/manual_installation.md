# Manual Installation

***

## Note

***

OpenTAKServer should be installed and run as a regular user, not root.

## Dependencies

***

The following packages are required by OpenTAKServer. Their names may vary by OS or distro.

- python3
- python3-pip
- python3-venv
- rabbitmq-server - RabbitMQ is used for routing CoTs between EUDs
- openssl - Required to generate certificates
- openjdk-19-jre-headless - OpenTAKServer uses `keytool` from this package during certificate generation
- nginx - Reverse proxy for the Web UI and video streams
- ffmpeg - Used to get metadata from video recordings

If you're using Ubuntu (and probably other Debian based distros) you can install these dependencies with the following command

```
sudo apt update && sudo NEEDRESTART_MODE=a apt upgrade -y
sudo NEEDRESTART_MODE=a apt install curl python3 python3-pip python3-venv rabbitmq-server openssl nginx ffmpeg openjdk-19-jre-headless -y
```

## Optional Dependencies

***

### Mumble server

***

If you would like OpenTAKServer to provide authentication for your Mumble server and you're using Ubuntu, 
use the following commands. You can find more details on [Mumble's wiki](https://wiki.mumble.info/wiki/Installing_Mumble).

```
sudo add-apt-repository ppa:mumble/release
sudo apt update
sudo apt install mumble-server python3-zeroc-ice -y
sudo sed -i '/ice="tcp -h 127.0.0.1 -p 6502"/s/^#//g' /etc/mumble-server.ini
sudo sed -i 's/icesecretwrite/;icesecretwrite/g' /etc/mumble-server.ini
sudo service mumble-server restart
```

Check `/var/log/mumble-server/mumble-server.log` for your SuperUser password

### ZeroTier

***

For Debian and Red Hat based Linux distros, use the following command to install ZeroTier. For other platforms and
further details, see [ZeroTier's site](https://www.zerotier.com/download/).

```
curl -s 'https://raw.githubusercontent.com/zerotier/ZeroTierOne/master/doc/contact%40zerotier.com.gpg' | gpg --import && \  
if z=$(curl -s 'https://install.zerotier.com/' | gpg); then echo "$z" | sudo bash; fi
```

### MediaMTX

***

Download version 1.6.0 from [MediaMTX's GitHub repo](https://github.com/bluenviron/mediamtx/releases/tag/v1.6.0).
Versions greater than 1.6.0 aren't supported yet due to some breaking changes that were introduced. When downloading,
make sure to select the correct version for your OS and processor. Create the mediamtx folder using `mkdir -p ~/ots/mediamtx/recordings`,
then extract the archive to `~/ots/mediamtx`.

Run the following commands to get the pre-configured `mediamtx.yml` from the OpenTAKServer-Installer repo and create a
systemd service.

```shell
wget https://github.com/brian7704/OpenTAKServer-Installer/raw/master/mediamtx.yml -qO ~/ots/mediamtx/mediamtx.yml
sudo sed -i "s~OTS_FOLDER~${HOME}/ots~g" ~/ots/mediamtx/mediamtx.yml
sudo tee /etc/systemd/system/mediamtx.service >/dev/null << EOF
[Unit]
Wants=network.target
[Service]
User=$(whoami)
ExecStart=$HOME/ots/mediamtx/mediamtx $HOME/ots/mediamtx/mediamtx.yml
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable mediamtx
sudo systemctl start mediamtx
```

## OpenTAKServer

***

Create a new Python virtual environment and install OpenTAKServer from pip with the following commands. The 
`--system-site-packages` option is required if you want to enable Mumble authentication. Mumble authentication 
requires python's zeroc-ice package which most distros have a binary package for. Installing zeroc-ice via pip will
compile from source and require lots of dev packages to be installed.

```shell
python3 -m venv --system-site-packages ~/.opentakserver_venv
~/.opentakserver_venv/bin/pip install opentakserver
```

## Systemd Service

Use the following commands to install a systemd service which allows OpenTAKServer to start at boot. After starting
OpenTAKServer the first time, it will automatically generate the certificate authority and all the keys you need
to get started.

```shell
sudo tee /etc/systemd/system/opentakserver.service >/dev/null << EOF
[Unit]
Wants=network.target
[Service]
User=$(whoami)
ExecStart=$HOME/.opentakserver_venv/bin/python -m opentakserver.app
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable opentakserver
sudo systemctl start opentakserver
```


## Configuration

***

Configuration settings are located at `~/ots/config.yml`. The out-of-the-box config
should work in most situations. See the [config settings](../configuration.md) page for details on what each setting does. After changing
config.yml you will need to restart OpenTAKServer for the changes to take effect.

## NGINX

***

Download [ots_http](https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/nginx_configs/ots_http),
[ots_https](https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/nginx_configs/ots_https),
and [ots_certificate_enrollment](https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/nginx_configs/ots_certificate_enrollment)
and place them in `/etc/nginx/sites-enabled/`. Use the `sed` command to set the location of your server certificates.

```shell
sudo sed -i "s~SERVER_CERT_FILE~$HOME/ots/ca/certs/opentakserver/opentakserver.pem~g" /etc/nginx/sites-enabled/*
sudo sed -i "s~SERVER_KEY_FILE~$HOME/ots/ca/certs/opentakserver/opentakserver.nopass.key~g" /etc/nginx/sites-enabled/*
sudo sed -i "s~CA_CERT_FILE~$HOME/ots/ca/ca.pem~g" /etc/nginx/sites-available/*
sudo systemctl restart nginx
```

## Finalizing

***

Restart OpenTAKServer and MediaMTX to finalize the installation. This will cause OpenTAKServer to update mediamtx.yml
with the OTS_MEDIAMTX_TOKEN setting.

```shell
sudo systemctl restart opentakserver
sudo systemctl restart mediamtx
```