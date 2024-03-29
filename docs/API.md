# API

***

## Authentication

All API calls except for `/api/login` require [authentication](authentication.md). Some are restricted to administrators only.

***

## Pagination

Most `GET` queries are paginated. You can include the `page` and `per_page` parameters to specify which page to get and
how many results should be returned.

***

## /api/status

Returns information about the server including disk usage, memory, usage, OS type and version, etc.

- HTTP Method: `GET`
- Access: Everyone

***

## /api/tcp/start

Starts the TCP CoT streaming server.

- HTTP Method: `GET`
- Access: Administrators only

***

## /api/tcp/stop

Stops the TCP CoT streaming server.

- HTTP Method: `GET`
- Access: Administrators only
 
***

## /api/ssl/start

Starts the SSL CoT streaming server

- HTTP Method: `GET`
- Access: Administrators only 

***

## /api/ssl/stop

Stops the TCP SSL streaming server

- HTTP Method: `GET`
- Access: Administrators only

***

## /api/certificate

Downloads a certificate data package for the specified callsign

- HTTP Method: `GET`
- Access: Administrators only
- Parameters: callsign

***

## /api/certificate

Creates a certificate data package for an EUD

- HTTP Method: `POST`
- Access: Administrators only
- Content Type: `JSON`
- Content: `{'uid': 'Android-123456789', 'callsign': 'BRAVO'}`

***

## /api/me

Returns user account details

- HTTP Method: `GET`
- Access: Everyone

***

## /api/data_packages

Uploads a data package

- HTTP Method: `POST`
- Access: Everyone

***

## /api/data_packages

Deletes a data package

- HTTP Method: `DELETE`
- Access: Everyone
- Parameters: `hash` - The sha256 hash of the data package to delete

***

## /api/data_packages

Returns info about data packages

- HTTP Method: `GET`
- Access: Everyone
- Parameters: The following parameters are all optional
    - `hash` - The sha256 hash of the data package
    - `filename` - Data package filename.
    - `creator_uid`
    - `keywords`
    - `mime_type`
    - `size`
    - `tool`
    - `page` - Which page to get
    - `per_page` - Number of results per page

***

## /api/data_packages/download

Downloads a data package

- HTTP Method: `GET`
- Access: Everyone
- Parameters: `hash` - The sha256 hash of the data package to download

***

## /api/cot

Searches for CoTs stored in the database

- HTTP Method: `GET`
- Access: Everyone
- Parameters: The following parameters are all optional
    - `how`
    - `type`
    - `sender_callsign`
    - `sender_uid`
    - `page`
    - `per_page`

***

## /api/alerts

Searches for alerts stored in the database

- HTTP Method: `GET`
- Access: Everyone
- Parameters:
    - `uid`
    - `sender_uid`
    - `alert_type`
    - `page`
    - `per_page`

***

## /api/point

Searches for points stored in the database

- HTTP Method: `GET`
- Access: Everyone
- Parameters
    - `uid` - UID of the EUD that created the point
    - `callsign` - Callsign of the EUD that created the point
    - `page`
    - `per_page`

***

## /api/casevac

Searches for CasEvacs that are stored in the database

- HTTP Method: `GET`
- Access: Everyone
- Parameters
    - `sender_uid` - UID of the EUD that created the point
    - `callsign` - Callsign of the EUD that created the point
    - `uid` - UID of the CasEvac
    - `page`
    - `per_page`

***

## /api/user/add