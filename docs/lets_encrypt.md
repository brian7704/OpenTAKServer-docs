# Let's Encrypt

***

If you have a domain name for your server you can use a Let's Encrypt certificate to secure the web UI. This also
allows iTAK to register with the server using a QR code.

Before beginning, make sure your domain has a DNS A record that points to the public IP of your server.

## ATAK and Trusted Certificates

***

Please note that although a certificate is trusted by web browsers, ATAK might not trust it. It seems that ATAK doesn't
use Android's built-in trusted certificate store. Let's Encrypt certificates work. However, while certificates from ZeroSSL will work in
other TAK clients, they won't work in ATAK. It fails with the following logcat error

```
URLReq: id 0 transfer failed - status 9 (SSL certificate problem: self-signed certificate in certificate chain); transferred 0 of 0
```

Other trusted certificate providers may result in the same issue.

## Ubuntu and Raspberry Pi OS

***

Use the following commands to obtain a certificate.

```shell
sudo apt install certbot
sudo systemctl stop nginx
sudo certbot certonly --standalone --preferred-challenges http -d your_domain_name.com # Replace your_domain_name.com with your actual domain
```

Next change these following two lines in `/etc/nginx/sites-enabled/ots_certificate_enrollment` from this:

```shell
ssl_certificate /home/your_username/ots/ca/certs/opentakserver/opentakserver.pem;
ssl_certificate_key /home/your_username/ots/ca/certs/opentakserver/opentakserver.nopass.key;
```

to this:

```shell
ssl_certificate /etc/letsencrypt/live/your_domain_name.com/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/your_domain_name.com/privkey.pem;
```

Finally, in `/etc/nginx/sites-enabled/ots_https`, change the same two lines in the server block for port 443. Do not change
the certificate settings in the server block for port 8443.

Once the certificate settings are change, start nginx with this command: `systemctl start nginx`.