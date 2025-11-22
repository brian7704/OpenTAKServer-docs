# CoT Routing

OpenTAKServer uses [RabbitMQ](https://rabbitmq-website.pages.dev/) to broker CoT messages between EUD's. When an EUD
connects, OpenTAKServer starts a new thread to handle sending and receiving CoT's. It also declares and binds to a
RabbitMQ queue for the EUD. Queues are also declared for each team (Cyan, Magenta, etc) and EUDs are automatically
bound to those queues when they send a CoT with their team info.