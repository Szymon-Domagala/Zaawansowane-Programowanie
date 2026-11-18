import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=8081)
)
channel = connection.channel()

channel.queue_declare(queue="task_queue",durable=True)

message = json.dumps({"Zadanie": "Zadanie do wykonania", "Status": "Pending"})
channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent
    ))

print(f"Wysłano zadanie: {message}")
connection.close()
