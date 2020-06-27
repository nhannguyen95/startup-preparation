RabbitMQ is a message broker: it accepts and forwards messages. The queue is only bound by the host's memory and disk limits.

The producer, consumer and broker do not have to reside on the same host (indeed in most application they don't). An application can be both a producer and consumer.

RabbitMQ speaks multiple protocols such as AMQP, etc.

In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an _exchange_.

Receiving messages from the queue works by subscribing a callback function to a queue.

We can leverage this asynchronous consumer/producer model:
- Work queues/Task queues are used to avoid doing a resources-intensive task immediately and having to wait for it to complete. This concept is especially useful in web applications where it's impossible to handle a complex task during a short HTTP request window.

**What if client die**?

RabbitMQ supports message acknowlegments as a mechanism to handle cases where workers die. _There aren't any message timeouts; RabbitMQ will redeliver the message when the consumer dies (its channel is closed, connection is closed, or TCP connection is lost). It's fine even if processing a message takes a very, very long time._

**What if rabbitmq server die**?

2 things to make sure messages aren't lost: mark both the queue and messages as durable.



