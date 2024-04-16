# Manual Installation

---

## Note

OpenTAKServer should be installed and run as a regular user, not root.

## Dependencies

The following packages are required by OpenTAKServer. Their names may vary by OS or distro.

- python3
- python3-pip
- rabbitmq-server - RabbitMQ is used for routing CoTs between EUDs
- openssl - Required to generate certificates
- nginx - Reverse proxy for the Web UI and video streams
- ffmpeg - Used to get metadata from video recordings

If you're using Ubuntu (and probably other Debian based distros) you can install these dependencies with the following command

```
sudo NEEDRESTART_MODE=a apt install curl python3 python3-pip rabbitmq-server git openssl nginx ffmpeg -y
```

## Optional Dependencies

### Mumble server

If you would like OpenTAKServer to provide authentication for your Mumble server and you're using Ubuntu, 
use the following commands. You can find more details on [Mumble's wiki](https://wiki.mumble.info/wiki/Installing_Mumble).

```
sudo add-apt-repository ppa:mumble/release
sudo apt update
sudo apt install mumble-server
```

### ZeroTier

For Debian and Red Hat based Linux distros, use the following command to install ZeroTier. For other platforms and
further details, see [ZeroTier's site](https://www.zerotier.com/download/).

```
curl -s 'https://raw.githubusercontent.com/zerotier/ZeroTierOne/master/doc/contact%40zerotier.com.gpg' | gpg --import && \  
if z=$(curl -s 'https://install.zerotier.com/' | gpg); then echo "$z" | sudo bash; fi
```

## Python packages

```
sudo pip3 install poetry pyotp
```

## OpenTAKServer

Once all of the dependencies have been installed you are ready to install OpenTAKServer. Download the latest release from GitHub
or clone the repo.

```
git clone https://github.com/brian7704/OpenTAKServer.git
```

```
cd OpenTAKServer
poetry config virtualenvs.in-project true
poetry config virtualenvs.options.system-site-packages true
poetry update
poetry install
```

## Configuration

Configuration settings are located at `~/ots/config.yml`. The out-of-the-box config
should work in most situations. See the [config settings](../configuration.md) page for details on what each setting does.

## Systemd Service

If you would like to start OpenTAKServer when the server boots, add a systemd service

```
sudo tee /etc/systemd/system/opentakserver.service >/dev/null << EOF
[Unit]
Wants=network.target
[Service]
User=$(whoami)
WorkingDirectory=/opt/OpenTAKServer
ExecStart=/usr/local/bin/poetry run python /opt/OpenTAKServer/opentakserver/app.py
[Install]
WantedBy=multi-user.target
EOF
```

Then enable and start the service

```
sudo systemctl daemon-reload
sudo systemctl enable opentakserver
sudo systemctl start opentakserver
```
