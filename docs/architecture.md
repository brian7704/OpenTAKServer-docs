# Architecture

***

## Ports

***

Below is a table of all default ports used by OpenTAKServer.

| Port  | Component     | Protocol | Interface            | Description                                                             |
|-------|---------------|----------|----------------------|-------------------------------------------------------------------------|
| 80    | Nginx         | TCP      | All                  | Web UI and proxy for HTTP API requests to OpenTAKServer port 8081       |
| 443   | Nginx         | TCP      | All                  | Web UI and proxy for HTTPS requests to OpenTAKServer port 8081          |
| 1935  | MediaMTX      | TCP      | All                  | Publish and view RTMP video streams                                     |
| 1936  | MediaMTX      | TCP      | All                  | Publish and view RTMPS video streams                                    |
| 5672  | RabbitMQ      | TCP      | All                  | For AMPQ clients, should be blocked from external access in most cases  |
| 6502  | Mumble Server | TCP      | Loopback (127.0.0.1) | Mumble's ICE server, used by OpenTAKServer to provide authentication    |
| 8000  | MediaMTX      | UDP      | All                  | Publish and view RTP video streams                                      |
| 8001  | MediaMTX      | UDP      | All                  | Publish and view RTCP video streams                                     |
| 8080  | Nginx         | TCP      | All                  | Web UI and proxy for HTTP API requests to OpenTAKServer port 8081       |
| 8081  | OpenTAKServer | TCP      | Loopback (127.0.0.1) | OTS listens on this port on the loopback interface for HTTP(S) requests |
| 8189  | MediaMTX      | UDP      | All                  | WebRTC                                                                  |
| 8088  | OpenTAKServer | TCP      | All                  | TCP CoT streaming port                                                  |
| 8089  | OpenTAKServer | TCP      | All                  | SSL CoT streaming port                                                  |
| 8443  | Nginx         | TCP      | All                  | Web UI and proxy for HTTPS API requests to OpenTAKServer port 8081      |
| 8446  | Nginx         | TCP      | All                  | Web UI and proxy for certificate enrollment to OpenTAKServer port 8081  |
| 8322  | MediaMTX      | TCP      | All                  | Publish and view RTSP(S) video streams                                  |
| 8554  | MediaMTX      | TCP/UDP  | All                  | Publish and view RTSP video streams                                     |
| 8888  | MediaMTX      | TCP      | All                  | View HLS video streams                                                  |
| 8889  | MediaMTX      | TCP      | All                  | Publish and view WebRTC streams                                         |
| 8890  | MediaMTX      | UDP      | All                  | Publish and view SRT streams                                            |
| 9997  | MediaMTX      | TCP      | Loopback (127.0.0.1) | MediaMTX's API                                                          |
| 25672 | RabbitMQ      | TCP      | All                  | RabbitMQ Federation, external access should be blocked in most cases    |
| 64738 | Mumble Server | TCP/UDP  | All                  | Mumble server voice streams                                             |

## Diagram

***

Here is an attempt at a diagram to help visualize the components used in OpenTAKServer and how they interact.

![!Diagram](images/diagram.png)