# Database

OpenTAKServer uses SQLAlchemy to handle its database. Although SQLAlchemy supports many different databases such as SQLite,
MySQL, and PostgreSQL, OpenTAKServer only support PostgreSQL with the PostGIS extension. As of version 1.7.14, the
`points` table includes a PostGIS Geography field. In future versions of OTS, API endpoints will be added to search data
geographically using this field.
