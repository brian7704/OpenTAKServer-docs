# Upgrading

***

Starting with version 1.2.0 there is an upgrade script which handles any new dependencies and database schema
changes, as well as upgrading OpenTAKServer and the webUI.

## Backup your database

***

The upgrade script will modify your database schema to add new tables and make changes to existing ones. Please backup
your database before upgrading. This ensures you can restore the backup copy if anything goes wrong during the schema
migration. The default database is a SQLite file at `~/ots/ots.db` in Ubuntu and Raspberry Pi, 
and `C:\Users\your_username\ots\ots.db` in Windows. Simply copying and pasting that file to another folder is
sufficient to make a backup.

## Upgrading Ubuntu and Raspberry Pi

***

Run this command as the same user that OpenTAKServer runs as. Do not run it as root.

```
~/.opentakserver_venv/bin/python <(curl https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/upgrade.py -s -N)
```

## Upgrading Windows

***

Run the following commands in Powershell

```powershell
cd "$env:USERPROFILE\ots"
curl https://raw.githubusercontent.com/brian7704/OpenTAKServer-Installer/master/upgrade.py -s -N -o upgrade.py
.\.venv\Scripts\python.exe .\upgrade.py
```