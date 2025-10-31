Groups/Channels
===============

**Note**: The terms group and channel will be used interchangeably. They can be thought of as the same thing.

OpenTAKServer supports groups as of 1.6.0. Groups will allow administrators to restrict what CoT messages users will
be able to send and receive.

Direction
---------

When assigning users to a group, they can be allowed to read/receive data from that group,
write/send data to the group, or both. To allow user to send CoT messages to the group, the ``IN`` direction
is specified. To allow users to receive CoT messages from to group, the ``OUT`` direction is specified. When assigning
users to groups, either or both directions may be specified.


LDAP
----

An LDAP or Microsoft Active Directory server can optionally be used to manage groups. See the `LDAP <ldap.html>`__  page
for details on configuring this feature.

When using LDAP, OpenTAKServer will consider users that are members of the group specified by ``OTS_LDAP_ADMIN_GROUP``
to be OTS administrators. The default name for this group is ``ots_admin``.