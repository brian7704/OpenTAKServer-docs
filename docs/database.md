# Database
***
OpenTAKServer uses SQLAlchemy to handle its database. SQLite is the default database engine. You can change this to any other
database engine supported by SQLAlchemy using the `SQLALCHEMY_DATABASE_URI` option in `config.yml`. SQLAlchemy supports the following
engines

- SQLite
- MySQL/MariaDB
- PostgreSQL
- Microsoft SQL Server
- Oracle

See [SQLAlchemy's documentation](https://docs.sqlalchemy.org/en/20/core/engines.html) for more details.

## PostgreSQL 
*** 

OpenTAKServer can be configured to use PostgreSQL as its database backend.

### Prerequisites

Before configuring OpenTAKServer to run on PostgreSQL, ensure you have:
- The database CA certificate (if an SSL connection is desired or required)
- Access to your PostgreSQL database with a typical database client
- Database connection details (hostname, port, username, password)

### Installation

Install the required PostgreSQL adapter in OpenTAKServer: 

```shell
sudo apt-get install libpq-dev
cd ~/.opentakserver_venv
bin/pip install psycopg2
```
If `ssl_mode=required` is on, download the database CA certificate from your provider and place it in the `~/ots` directory. 

Modify the settings in `~/ots/config.yml` to include:

```yaml
SQLALCHEMY_DATABASE_URI: postgresql://[user]:[password]@[hostname]:[port]/[database]?sslmode=require
SQLALCHEMY_ENGINE_OPTIONS:
  pool_pre_ping: true
  connect_args:
    sslmode: require
    sslrootcert: database-ca.crt
```

Replace `[user]`, `[password]`, `[hostname]`, `[port]`, and `[database]` with your actual database connection details. You can leave `SQLALCHEMY_ENGINE_OPTIONS` as is if the database does not use an SSL connection. 

### Troubleshooting
OpenTAKServer does not produce detailed error reports when something is wrong with the configuration file or database. It's easier to temporarily turn the service off and run the program directly for debugging. 

To get detailed feedback about connection issues, run OpenTAKServer directly instead of as a service:

```shell
sudo systemctl stop opentakserver.service
~/.opentakserver_venv/bin/opentakserver
```

If you encounter schema permission issues, ensure the database user owns the `public` schema. You may need to recreate it with the correct ownership.

Finally, stop the OTS process in the terminal (Ctrl+C) and restart the service:
```shell
sudo systemctl start opentakserver.service
```
