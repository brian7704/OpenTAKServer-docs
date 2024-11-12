# Windows Installer Script

***

The Windows installer script supports Windows 10, 11, and recent versions of Windows Server. It uses the [Chocolatey](https://chocolatey.org/)
package manager to install nginx and RabbitMQ

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
2. `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://i.opentakserver.io/windows_installer'))`
3. You may be prompted about the script being untrusted. If so, enter `R` at the prompt and press `Enter` to run it anyway.
4. At this point the script will run with minimal user action required. You may see dialog boxes asking if you want to allow the installed software to access the network. Click allow on all of these dialogs
5. After everything is installed, the installer will make services for MediaMTX and OpenTAKServer so they can run automatically at boot. You will be prompted for your password. The password is only used to create the services.
6. If you didn't get any errors, installation should be complete and OpenTAKServer should be running. Try browsing to `http://127.0.0.1` and you will see the login page.
7. If other devices on the network can't see the login page, you may need to [configure Windows Firewall](https://learn.microsoft.com/en-us/sql/reporting-services/report-server/configure-a-firewall-for-report-server-access?view=sql-server-ver16). The list of ports that OpenTAKServer uses is [here](../architecture.md).
