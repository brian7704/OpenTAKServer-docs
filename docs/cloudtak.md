# CloudTAK

OpenTAKServer is compatible with [CloudTAK](https://github.com/dfpc-coe/CloudTAK), a fully featured, in-browser TAK client. If you need support, please ask in the OTS discord rather than contacting COTAK (the creators of CloudTAK).

## Domain Name and Certificates

CloudTAK requires a domain name and subdomain names in addition to a Let's Encrypt certificate on the server.

* `ots.example.com` - Points to OpenTAKServer.
* `cloudtak.example.com` - Points to the CloudTAK web UI.
* `tiles.cloudtak.example.com` - This is a sub-subdomain for CloudTAK's map tile server.
* `video.example.com` - CloudTAK's MediaMTX server. This is optional as video streaming from OTS to CloudTAK is not working at this time. However this subdomain will be required once streaming is working.

## Known Issues

* Video streaming currently doesn't work
* Uploading files and data packages doesn't work

## Installation

This guide assume that you're installing CloudTAK on the same server as OpenTAKServer. The CloudTAK installer script only works on Ubuntu.

1. Clone the CloudTAK repo

```bash
git clone https://github.com/dfpc-coe/CloudTAK.git
cd CloudTAK
```

2. Run the CloudTAK installer script `./cloudtak.sh install`. This script will install CloudTAK as well as docker and all prerequisites.
3. Run `./cloudtak.sh start` to start the docker containers.
4. Configure the nginx proxy. Copy the config below and paste it to a new file at `/etc/nginx/sites-available/cloudtak`. You also need to change the `server_name` line to your FQDN.

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
   }

listen 80;
}

server {

   root /var/www/html;

   # Add index.php to the list if you are using PHP
   index index.html index.htm index.nginx-debian.html;

   server_name tiles.cloudtak.example.com; # <------- Change this to your FQDN

   location / {
           

           proxy_pass http://localhost:5002; 
           proxy_ssl_verify off;
           proxy_ssl_session_reuse on;
           proxy_buffering off;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Referer $scheme://$host/;

   }

listen 80;


}
```

5Create a symbolic link to enable the new nginx config file.

```bash
sudo ln -s /etc/nginx/sites-available/cloudtak /etc/nginx/sites-enabled/cloudtak
```

6. Edit `/etc/nginx/sites-available/ots_certificate_enrollment` and add the following inside the `server {}` stanza if it doesn't already exist.

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

7. Edit `/etc/nginx/sites-available/ots_https` and add this inside the listen 8443 `server {}` if it doesn't already exist.

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

8. Install certbot and nginx `sudo apt install nginx certbot python3-certbot-nginx -y`
9. Get a cert from Let's Encrypt `sudo certbot --nginx`
10. Restart nginx `sudo systemctl restart nginx`
11. Open a browser and enter your CloudTAK server's URL, i.e. https://cloudtak.example.com