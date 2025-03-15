API
===

--------------

Authentication
--------------

All API calls except for ``/api/login`` require
`authentication <authentication.md>`__. Some are restricted to
administrators only.

--------------

Pagination
----------

Most ``GET`` queries are paginated. You can include the ``page`` and
``per_page`` parameters to specify which page to get and how many
results should be returned.

--------------

/api/status
-----------

Returns information about the server including disk usage, memory,
usage, OS type and version, etc.

-  HTTP Method: ``GET``
-  Access: Everyone

--------------

/api/tcp/start
--------------

Starts the TCP CoT streaming server.

-  HTTP Method: ``GET``
-  Access: Administrators only

--------------

/api/tcp/stop
-------------

Stops the TCP CoT streaming server.

-  HTTP Method: ``GET``
-  Access: Administrators only

--------------

/api/ssl/start
--------------

Starts the SSL CoT streaming server

-  HTTP Method: ``GET``
-  Access: Administrators only

--------------

/api/ssl/stop
-------------

Stops the TCP SSL streaming server

-  HTTP Method: ``GET``
-  Access: Administrators only

--------------

/api/certificate
----------------

Downloads a certificate data package for the specified callsign

-  HTTP Method: ``GET``
-  Access: Administrators only
-  Parameters: callsign

--------------

.. _apicertificate-1:

/api/certificate
----------------

Creates a certificate data package for an EUD

-  HTTP Method: ``POST``
-  Access: Administrators only
-  Content Type: ``JSON``
-  Content: ``{'uid': 'Android-123456789', 'callsign': 'BRAVO'}``

--------------

/api/me
-------

Returns user account details

-  HTTP Method: ``GET``
-  Access: Everyone

--------------

/api/data_packages
------------------

Uploads a data package

-  HTTP Method: ``POST``
-  Access: Everyone

--------------

.. _apidata_packages-1:

/api/data_packages
------------------

Deletes a data package

-  HTTP Method: ``DELETE``
-  Access: Everyone
-  Parameters: ``hash`` - The sha256 hash of the data package to delete

--------------

.. _apidata_packages-2:

/api/data_packages
------------------

Returns info about data packages

-  HTTP Method: ``GET``
-  Access: Everyone
-  Parameters: The following parameters are all optional

   -  ``hash`` - The sha256 hash of the data package
   -  ``filename`` - Data package filename.
   -  ``creator_uid``
   -  ``keywords``
   -  ``mime_type``
   -  ``size``
   -  ``tool``
   -  ``page`` - Which page to get
   -  ``per_page`` - Number of results per page

--------------

/api/data_packages/download
---------------------------

Downloads a data package

-  HTTP Method: ``GET``
-  Access: Everyone
-  Parameters: ``hash`` - The sha256 hash of the data package to
   download

--------------

/api/cot
--------

Searches for CoTs stored in the database

-  HTTP Method: ``GET``
-  Access: Everyone
-  Parameters: The following parameters are all optional

   -  ``how``
   -  ``type``
   -  ``sender_callsign``
   -  ``sender_uid``
   -  ``page``
   -  ``per_page``

--------------

/api/alerts
-----------

Searches for alerts stored in the database

-  HTTP Method: ``GET``
-  Access: Everyone
-  Parameters:

   -  ``uid``
   -  ``sender_uid``
   -  ``alert_type``
   -  ``page``
   -  ``per_page``

--------------

/api/point
----------

Searches for points stored in the database

-  HTTP Method: ``GET``
-  Access: Everyone
-  Parameters

   -  ``uid`` - UID of the EUD that created the point
   -  ``callsign`` - Callsign of the EUD that created the point
   -  ``page``
   -  ``per_page``

--------------

/api/casevac
------------

Searches for CasEvacs that are stored in the database

-  HTTP Method: ``GET``
-  Access: Everyone
-  Parameters

   -  ``sender_uid`` - UID of the EUD that created the point
   -  ``callsign`` - Callsign of the EUD that created the point
   -  ``uid`` - UID of the CasEvac
   -  ``page``
   -  ``per_page``

--------------

/api/markers
------------

Searches for markers stored in the database

-  HTTP Method: ``GET``
-  Access: Everyone
-  Parameters

   -  ``uid`` - The marker’s unique ID
   -  ``affiliation`` - One of the following

      -  friendly
      -  hostile
      -  unknown
      -  pending
      -  assumed
      -  neutral
      -  suspect
      -  joker
      -  faker

   -  ``callsign`` - The marker’s callsign

--------------

.. _apimarkers-1:

/api/markers
------------

Adds a new marker or updates an existing one

-  HTTP Method: ``POST``
-  Access: Everyone
-  Content Type: JSON
-  Required data in the JSON body

   -  ``latitude`` - float, must be >= -90 and <= 90
   -  ``longitude`` - float, must be >= -180 and <= 180
   -  ``name`` - name/callsign of the marker
   -  ``uid`` - An identifier in UUID4 format. If no marker exists with
      this UUID, a new on is created. Otherwise, the existing marker is
      updated.

-  Optional data in the JSON body

   -  ``type`` - The CoT type, defaults to ``a-u-G`` if none is given.
      There are too many possible valid values to list but here are a
      few examples. See `this
      chart <https://www.spatialillusions.com/milsymbol/docs/milsymbol-2525c.html#heading-1>`__
      from milsymbol for more examples.

      -  ``a-f-G`` - Affiliation friendly, battle dimension ground
      -  ``a-h-U`` - Affiliation hostile, battle dimension subsurface
      -  ``a-j-A`` - Affiliation joker, battle dimension airborne

   -  ``course`` - The direction of travel in compass degrees. Must be
      >= 0 and < 360. Defaults to 0.
   -  ``azimuth`` - The azimuth in compass degrees. Must be >= 0 and <
      360. Defaults to 0.
   -  ``speed`` - The speed in INSERT_UNIT_HERE. Must be >= 0. Defaults
      to 0.
   -  ``battery`` - The remaining battery percentage. Must be >= 0 and
      <= 100. Defaults to NULL.
   -  ``fov`` - The camera’s field of vision in compass degrees. This
      will show a camera’s view shed on the map.
   -  ``ce`` - Circular 1-sigma or a circular area about the location in
      meters
   -  ``hae`` - Height above the WGS ellipsoid in meters
   -  ``le`` - Linear 1-sigma error or an altitude range about the
      location in meters

--------------

.. _apimarkers-2:

/api/markers
------------

Deletes a marker

-  HTTP Method: ``DELETE``
-  Access: Everyone
-  Parameters

   -  ``uid`` - The marker’s UID

--------------

.. _apicasevac-1:

/api/casevac
------------

Searches for CasEvacs in the database

-  HTTP Method: ``GET``
-  Access: Everyone
-  Parameters

   -  ``callsign`` - The CasEvac’s Callsign

      -  ``uid`` - The CasEvac’s UID

--------------

.. _apicasevac-2:

/api/casevac
------------

Add or update a CasEvac

-  HTTP Method ``POST``
-  Access: Everyone
-  Content Type: JSON
-  Required data in JSON body

   -  ``uid`` - An identifier in UUID4 format. If no marker exists with
      this UUID, a new on is created. Otherwise, the existing marker is
      updated.
   -  ``title`` - Name of the CasEvac that will appear on the map
   -  ``latitude`` - float, must be >= -90 and <= 90
   -  ``longitude`` - float, must be >= -180 and <= 180

-  Optional data in the JSON body

   -  ``ambulatory`` - Integer
   -  ``casevac`` - Boolean
   -  ``child`` - Integer
   -  ``enemy`` - Integer
   -  ``epw`` - Integer
   -  ``equipment_detail`` - String
   -  ``equipment_none`` - Boolean
   -  ``equipment_other`` - Boolean
   -  ``extration_equipment`` - Boolean
   -  ``freq`` - Integer
   -  ``friendlies`` - String
   -  ``hlz_marking`` - Integer
   -  ``hlz_remarks`` - String
   -  ``hoist`` - Boolean
   -  ``litter`` - Integer
   -  ``marked_by`` - String
   -  ``medline_remarks`` - String
   -  ``nonus_civilian`` - Integer
   -  ``nonus_military`` - Integer
   -  ``obstacles`` - String
   -  ``priority`` - Integer
   -  ``routine`` - Integer
   -  ``security`` - Integer
   -  ``terrain_loose`` - Boolean
   -  ``terrain_other`` - Boolean
   -  ``terrain_other_detail`` - Boolean
   -  ``terrain_detail`` - String
   -  ``terrain_none`` - Boolean
   -  ``terrain_rough`` - Boolean
   -  ``terrain_slope`` - Boolean
   -  ``terrain_slope_dir`` - String
   -  ``urgent`` - Integer
   -  ``us_civilian`` - Integer
   -  ``us_military`` - Integer
   -  ``ventilator`` - Boolean
   -  ``winds_are_from`` - String
   -  ``zone_prot_selection`` - Integer
