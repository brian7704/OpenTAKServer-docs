# Let's Encrypt

***

If you have a domain name for your server you can use a Let's Encrypt certificate to secure the web UI. This also
allows iTAK to register with the server using a QR code.

Before beginning, make sure your domain has a DNS A record that points to the public IP of your server. 

## Ubuntu and Raspberry Pi OS

***

Use the following commands to obtain a certificate.

```
sudo apt install certbot
sudo systemctl stop nginx
sudo certbot certonly --standalone --preferred-challenges http -d your_domain_name.com # Replace your_domain_name.com with your actual domain
```

Next change these following two lines in `/etc/nginx/site-enabled/ots_certificate_enrollment` from this:

```
ssl_certificate /home/your_username/ots/ca/certs/opentakserver/opentakserver.pem;
ssl_certificate_key /home/your_username/ots/ca/certs/opentakserver/opentakserver.nopass.key;
```

to this:

```
ssl_certificate /etc/letsencrypt/live/your_domain_name.com/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/your_domain_name.com/privkey.pem;
```

Finally, in `/etc/nginx/site-enabled/ots_https`, change the same two lines in the server block for port 443. Do not change
the certificate settings in the server block for port 8443.

Once the certificate settings are change, start nginx with this command: `systemctl start nginx`.

## Windows

***

These instructions are untested. If you try them out you can leave feedback in the [Discord server](https://discord.gg/6uaVHjtfXN)
or open an issue on [GitHub](https://github.com/brian7704/OpenTAKServer-docs/issues) and we'll modify them accordingly.

1. Install [acme.sh](https://github.com/acmesh-official/acme.sh/wiki#4-how-to-run-on-windows-with-cygwin-or-git-bash)
2. Click on the Start button and search for `Services`
3. In the list of services, stop nginx
4. Open Cygwin and run `acme.sh --issue -d your_domain_name.com -w c:\tools\`
5. Open `C:\tools\nginx-1.25.4\conf\ots\ots_https.conf` in a text editor
6. In the server block for port 443, change `ssl_certificate_key` to `c:\tools\privkey.pem` and `ssl_certificate` to `c:\tools\fullchain.pem`
7. Open `C:\tools\nginx-1.25.4\conf\ots\ots_certificate_enrollment.conf` in a text editor
8. Change `ssl_certificate_key` to `c:\tools\privkey.pem` and `ssl_certificate` to `c:\tools\fullchain.pem`
9. Go back to `Services` and start nginx