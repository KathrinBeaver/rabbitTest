#!/usr/bin/env python
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.basic_consume(on_message_callback=callback,
                      queue='hello')

channel.start_consuming()
