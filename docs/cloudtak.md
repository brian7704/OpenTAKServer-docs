# CloudTAK

***

OpenTAKServer is compatible with [CloudTAK](https://github.com/dfpc-coe/CloudTAK), a fully featured, in-browser TAK client.

## Notes

***

CloudTAK has only been tested using an FQDN with a trusted certificate (i.e. Let's Encrypt). It may still work without an FQDN or trusted cert, but SSL is always required.
For best results you should create a subdomain. For example, if your FQDN is `example.com`, your subdomain could be `cloudtak.example.com`.

If you need support, please ask in the OTS discord rather than contacting COTAK (the creators of CloudTAK).

## Installation

***

This guide assume that you're installing CloudTAK on the same server as OpenTAKServer.

### Docker

Run these commands to install Docker on Ubuntu. If you're not using Ubuntu, check the Docker docs on how to install for your distro.

```shell
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update

sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### CloudTAK

***

1. Clone the CloudTAK repo

```bash
git clone https://github.com/dfpc-coe/CloudTAK.git
cd CloudTAK
```

2. Change `API_URL` in docker_compose.yml. It should be prefixed with `https://` and should be changed to the IP or FQDN that you'll use to access it. You should also remove `:5000` at the end. It cannot be localhost unless you're installing CloudTAK to the same computer you'll be accessing it from.
3. Configure the nginx proxy. Copy the config below and paste it to a new file at `/etc/nginx/sites-available/cloudtak`. You also need to change the `server_name` line to your FQDN.

```nginx
server {

   root /var/www/html;

   # Add index.php to the list if you are using PHP
   index index.html index.htm index.nginx-debian.html;

   server_name cloudtak.example.com; # <------- Change this to your FQDN

   location / {

           proxy_pass http://localhost:5000; 
           proxy_ssl_verify off;
           proxy_ssl_session_reuse on;
           proxy_buffering off;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           #proxy_hide_header Authorization;
           #proxy_set_header Referer '';
           #proxy_set_header Origin '';
   }

listen 80;
}
```

4. Create a symbolic link to enable the new nginx config file.

```bash
sudo ln -s /etc/nginx/sites-available/cloudtak /etc/nginx/sites-enabled/cloudtak
```

5. Edit `/etc/nginx/sites-available/ots_certificate_enrollment` and add the following inside the `server {}` stanza.

```nginx
        location /oauth {
                proxy_pass http://127.0.0.1:8081;
                proxy_http_version 1.1;
                proxy_set_header Host $host:8443;
                proxy_set_header X-Forwarded-For $remote_addr;
                proxy_set_header X-Ssl-Cert $ssl_client_escaped_cert;
                proxy_set_header X-Forwarded-Proto $scheme;

        }
```

6. Edit `/etc/nginx/sites-available/ots_https` and add this inside the listen 8443 `server {}`.

```nginx
        location /files {
                proxy_pass http://127.0.0.1:8081;
                proxy_http_version 1.1;
                proxy_set_header Host $host:443;
                proxy_set_header X-Forwarded-For $remote_addr;
                proxy_set_header X-Ssl-Cert $ssl_client_escaped_cert;
                proxy_set_header X-Forwarded-Proto $scheme;

        }
```

7. Install certbot and nginx `sudo apt install nginx certbot python3-certbot-nginx -y`
8. Get a cert from Let's Encrypt `sudo certbot --nginx`
9. Restart nginx `sudo systemctl restart nginx`
10. Open a browser and enter your CloudTAK server's URL, i.e. https://cloudtak.example.com