# Cot Routing
***
OpenTAKServer uses [RabbitMQ](https://rabbitmq-website.pages.dev/) to broker CoT messages between EUD's. When an EUD
connects, OpenTAKServer starts a new thread to handle sending and receiving CoT's. It also declares and binds to a
RabbitMQ queue for the EUD. Queues are also declared for each team (Cyan, Magenta, etc) and EUDs are automatically
bound to those queues when they send a CoT with their team info.

## Data Sync
***
While OpenTAKServer doesn't yet support the DataSync plugin, RabbitMQ provides a similar functionality. Because it uses
a store-and-forward technique, any CoT's that are sent to an offline EUD are held in its queue until it reconnects.
Once it reconnects, the EUD will receive all the CoT's that it missed while offline.