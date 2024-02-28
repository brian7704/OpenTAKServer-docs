# Database
***
OpenTAKServer uses SQLAlchemy to handle its database. SQLite is the default database engine. You can change this to any other
database engine supported by SQLAlchemy using the SQLALCHEMY_DATABASE_URI option in config.py. SQLAlchemy supports the following
engines

- SQLite
- MySQL/MariaDB
- PostgreSQL
- Microsoft SQL Server
- Oracle

See [SQLAlchemy's documentation](https://docs.sqlalchemy.org/en/20/core/engines.html) for more details.