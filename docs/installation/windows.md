# Windows Installer Script

***

The installer script is the recommended way to install OpenTAKServer on Windows. So far it's only been tested on Windows 10 Pro,
but it will probably work on Windows 11 and Windows Server. If you try it on any of these platforms, please leave feedback
about how it worked on [GitHub issues](https://github.com/brian7704/OpenTAKServer-Installer/issues) or on the
[Discord server](https://discord.gg/6uaVHjtfXN).

Note that the Mumble authentication feature is not supported yet in Windows.

## Prerequisites

***

The installer will create new services for MediaMTX and OpenTAKServer that will run under the computer account you
are logged in as. The services require that account to have a password. If your account doesn't have a password you can 
enable one by clicking on `Start` -> `Settings` -> `Accounts` -> `Sign-In options` -> `Password`.

The installer also has to be run in Powershell as an administrator. To do that, click on `Start` and search for `Powershell`.
There should be an option called `Run as administrator` that you can click on.

## Installer Instructions

***

1. Run Powershell as an administrator
2. `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('bit.ly/4c7ZVmq'))`
3. You may be prompted about the script being untrusted. If so, enter `R` at the prompt and press `Enter` to run it anyway.
4. At this point the script will run with minimal user action required. You may see dialog boxes asking if you want to allow the installed software to access the network. Click allow on all of these dialogs
5. After everything is installed, the installer will make services for MediaMTX and OpenTAKServer so they can run automatically at boot. You will be prompted for your password. The password is only used to create the services.
6. If you didn't get any errors, installation should be complete and OpenTAKServer should be running. Try browsing to `http://127.0.0.1` and you will see the login page.
7. If other devices on the network can't see the login page, you may need to [configure Windows Firewall](https://learn.microsoft.com/en-us/sql/reporting-services/report-server/configure-a-firewall-for-report-server-access?view=sql-server-ver16). The list of ports that OpenTAKServer uses is [here](../architecture.md).

# Windows Manual Installation

***

1. Install [chocolatey](https://chocolatey.org/install#individual)
    1. Open Powershell as an administrator
    2. `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`
2. Run `choco install python3 openssl rabbitmq nginx sed git jdk8 -y`
3. Install Poetry
    1. Open Powershell as an administrator 
    2. `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -`
    3. `$Env:Path += ";$env:USERPROFILE\AppData\Roaming\Python\Scripts"; setx PATH "$Env:Path"` Replace <YOUR_USERNAME>
4. Create the directories `C:\users\<YOUR_USERNAME>\ots` and `C:\users\<YOUR_USERNAME>\ots\mediamtx`
5. Download [MediaMTX](https://github.com/bluenviron/mediamtx/releases/latest) and put the binary in `C:\users\<YOUR_USERNAME>\ots\mediamtx`
6. Download [OpenTAKServer's config for MediaMTX](https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/mediamtx.yml) and place it in `C:\users\<YOUR_USERNAME>\ots\mediamtx`
7. Download the latest release of OpenTAKServer from GitHub and extract it to a folder
8. Go back to the admin Powershell
9. `cd c:\path\to\opentakserver`
10. `poetry update`
11. `poetry install`
12. `poetry run python opentakserver\app.py`
13. OpenTAKServer will automatically create the database, certificates and the administrator user
14. If there is an error about not being able to open the database, do the following
    1. Open `C:\users\<YOUR_USERNAME>\ots\config.yml` in a text editor like Notepad++
    2. Change `SQLALCHEMY_DATABASE_URI` from `sqlite:////C:\Users\<YOUR_USERNAME>\ots\ots.db` to `sqlite:///C:\\Users\\<YOUR_USERNAME>\\ots\\ots.db`
    3. The difference is you should only have three slashes between `sqlite:` and `C:`, and also two slashes between the folders
    4. `poetry run python opentakserver\app.py`
15. Configure Nginx
    1. Download [nginx.conf](https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/windows_nginx_configs/nginx.conf) from the installer repo and put it in `C:\tools\nginx-<VERSION>\config`
    2. Download [proxy_params](https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/windows_nginx_configs/proxy_params) from the installer repo and put it in `C:\tools\nginx-<VERSION>\config`
    3. Make the `C:\tools\nginx-<VERSION>\config\ots` directory
    4. Download [ots_http.conf](https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/windows_nginx_configs/ots_http.conf), [ots_https.conf](https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/windows_nginx_configs/ots_https.conf), and [ots_certificate_enrollment.conf](https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/windows_nginx_configs/ots_certificate_enrollment.conf) and place them in `C:\tools\nginx-<VERSION>\config\ots`
    5. In each of the three config files, replace `NGINX_VERSION` with the version number of nginx that's installed. The version as of this writing is `1.25.4`
    6. In `ots_https.conf` and `ots_certificate_enrollment.conf` replace `SERVER_CERT_FILE` with `C:\Users\<YOUR_USERNAME>\ots\ca\certs\opentakserver\opentakserver.pem`
    7. In `ots_https.conf` and `ots_certificate_enrollment.conf` replace `SERVER_KEY_FILE` with `C:\Users\<YOUR_USERNAME>\ots\ca\certs\opentakserver\opentakserver.nopass.key`
    8. In `ots_https.conf` replace `CA_CERT_FILE` with `C:\Users\<YOUR_USERNAME>\ots\ca\ca.pem`
    9. In an admin Powershell run `nssm restart nginx`
