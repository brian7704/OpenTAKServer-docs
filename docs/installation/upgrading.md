# Upgrading

***

Starting with version 1.2.0 there is an upgrade script which handles any new dependencies and database schema
changes, as well as upgrading OpenTAKServer and the webUI. If you want to upgrade from version 1.1.10 or below, use
this script.

## Backup your database

***

The upgrade script will modify your database schema to add new tables and make changes to existing ones. Please backup
your database before upgrading. This ensures you can restore the backup copy if anything goes wrong during the schema
migration. The default database is a SQLite file at `~/ots/ots.db` in Ubuntu and Raspberry Pi, 
and `C:\Users\your_username\ots\ots.db` in Windows. Simply copying and pasting that file to another folder is
sufficient to make a backup.

## Ubuntu

***

Run this command as the same user that runs OpenTAKServer. Do not run as root.

`curl -L https://i.opentakserver.io/ubuntu_updater | bash -`

## Raspberry Pi

***

Run this command as the same user that runs OpenTAKServer. Do not run as root.

`curl -L https://i.opentakserver.io/raspberry_pi_updater | bash -`

## Bleeding Edge

***

Both the Ubuntu and Raspberry Pi upgrade scripts have an option to install the latest, unstable versions of
OpenTAKServer and OpenTAKServer-UI. This is for testing purposes only, **DO NOT USE THIS ON A PRODUCTION SERVER!** More than
likely things will break or there will be bugs.

### Ubuntu

```shell
curl -L https://i.opentakserver.io/ubuntu_updater | bash -s -- --bleeding-edge | tee ~/ots_ubuntu_upgrade.log
```

### Raspberry Pi

```shell
curl -L https://i.opentakserver.io/raspberry_pi_installer | bash -s -- --bleeding-edge | tee ~/ots_rpi_upgrade.log
```

## Windows

***

Coming soon
