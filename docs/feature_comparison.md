# Feature Comparison

|                                            | OpenTAKServer        | FreeTAKServer                   | TAKServer            |
|--------------------------------------------|----------------------|---------------------------------|----------------------|
| TCP                                        | Yes                  | Yes                             | Yes                  |
| SSL                                        | Yes                  | Yes                             | Yes                  |
| Automatic Certificate Authority Generation | Yes                  | No                              | No                   |
| Certificate Enrollment                     | Yes                  | No                              | Yes                  |
| Federation                                 | Yes[^1]               | No                              | Yes                  |
| Data Packages                              | Yes                  | Yes                             | Yes                  |
| DataSync                                   | Yes                  | Yes                             | Yes                  |
| ExCheck                                    | Coming Soon          | Yes                             | Yes                  |
| Reports Plugin                             | Yes                  | No                              | Yes                  |
| Video Streaming                            | Yes                  | Yes                             | Installed Separately |
| Video Stream Recording/Playback            | Yes                  | No                              | No                   |
| Mumble Server Authentication               | Yes                  | No                              | No                   |
| Web UI                                     | Yes                  | Yes                             | Yes                  |
| EUD Authentication                         | Yes                  | No                              | Yes                  |
| ADS-B Data From Airplanes.live             | Yes                  | No                              | No                   |
| AIS Data From AISHub.net                   | Yes                  | No                              | No                   |
| Database                                   | SqlAlchemy (PostGIS) | SqlAlchemy (Defaults to SQLite) | PostgreSQL           |
| Runs on Raspberry Pi                       | Yes                  | Yes                             | Yes                  |
| Meshtastic support                         | Yes                  | No                              | No                   |
| Update Server                              | Yes                  | No                              | No                   |
| Device Profiles                            | Yes                  | No                              | Yes                  |
| Groups/Channels                            | Yes                  | No                              | Yes                  |
| Actively Developed                         | Yes                  | No                              | Yes                  |

[^1]: Federation support added in 1.8.0. Currently only supports outgoing connections to FedHub and the GOTS takserver. Missions, tokens, and incoming connections to be added at a later date