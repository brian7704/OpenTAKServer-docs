# Let's Encrypt

If you have a domain name for your server you can use a Let's Encrypt certificate to secure the web UI. This also
allows iTAK to register with the server using a QR code.

Before beginning, make sure your domain has a DNS A record that points to the public IP of your server.

## ATAK and Trusted Certificates

Please note that ATAK does not use Android's trusted certificate store. It comes bundled with root CAs for Let's Encrypt
and Digicert only. Other trusted certificate providers will result in a `TAK Server's Identity Could Not Be Verified` error
even though most web browsers and OSes trust them.

## Ubuntu and Raspberry Pi OS

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