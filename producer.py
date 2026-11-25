import pika
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--quantity",
    type=int,
    default=100,
    help="Ilosc zadan w kolojce"
)
args = parser.parse_args()

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=8081)
)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)

for i in range(args.quantity):
    message = f"{i + 1}. Zadanie do wykonania"
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        ))

print(f"Wysłano zadania")
connection.close()
