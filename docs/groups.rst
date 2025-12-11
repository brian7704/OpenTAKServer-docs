Groups/Channels
===============

**Note**: The terms group and channel will be used interchangeably. They can be thought of as the same thing.

OpenTAKServer supports groups as of 1.6.0. Groups will allow administrators to restrict what CoT messages users will
be able to send and receive.

The __ANON__ Group
------------------

Users who aren't assigned to any group will be automatically assigned to the ``__ANON__`` group. Likewise, any missions that
are not assigned to a group will be assigned to this group. The __ANON__ group is the only group that can't be deleted.

Default Groups
--------------

There are four groups automatically when OpenTAKServer starts, ``__ANON__``, ``ADS-B``, ``AIS``, and ``Meshtastic``. The ``__ANON__``
group is integral to the TAK ecosystem and can't be changed or deleted. However the names of the ``ADS-B``, ``AIS``, and
``Meshtastic`` groups can be changed via the ``OTS_ADSB_GROUP``, ``OTS_AIS_GROUP``, and ``OTS_MESHTASTIC_GROUP`` respectively.

The Airplanes.live scheduled job will publish all data to the group specified in ``OTS_ADSB_GROUP``, the AISHub scheduled
job will publish to the group specified in ``OTS_AIS_GROUP``, and data received via MQTT from Meshtastic nodes will be published
to the group specified in ``OTS_MESHTASTIC_GROUP``. This allows users to enable or disable whichever channels they want. However,
the server administrator can change these settings to ``__ANON__`` to send ADS-B, AIS, or Meshtastic data to everyone.

Direction
---------

When assigning users to a group, they can be allowed to read/receive data from that group,
write/send data to the group, or both. To allow user to send CoT messages to the group, the ``IN`` direction
is specified. To allow users to receive CoT messages from to group, the ``OUT`` direction is specified. When assigning
users to groups, either or both directions may be specified.


LDAP
----

An LDAP or Microsoft Active Directory server can optionally be used to manage groups. See the :ref:`ldap`  page
for details on configuring this feature.

When using LDAP, OpenTAKServer will consider users that are members of the group specified by ``OTS_LDAP_ADMIN_GROUP``
to be OTS administrators. The default name for this group is ``ots_admin``.

LDAP groups must be prefixed with the value of ``OTS_LDAP_GROUP_PREFIX`` (default: ``ots_``). Groups without this prefix
are ignored. Additionally, group direction is specified with ``_READ`` and ``_WRITE`` suffixes. These suffixes are case
insensitive. For this reason, when creating a TAK group on your LDAP server you will actually need to create three groups.
For example, if the group is called ``group1`` you would create ``ots_group1``, ``ots_group1_read``, and ``ots_group1_write``.
All three are required. Then an administrator can assign ``ots_group1_read`` and ``ots_group1_write`` to users as needed.