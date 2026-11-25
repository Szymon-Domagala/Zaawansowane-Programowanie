import time
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=8081)
)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)
channel.basic_qos(prefetch_count=1)
print("Oczekiwanie na zadanie")


def callback(ch, method, properties, body):
    task_name = body.decode("utf-8")
    print(f"Przyjeto zadanie: {task_name}")
    time.sleep(30)
    print(f"Wykonano zadanie: {task_name}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue="task_queue", on_message_callback=callback)
channel.start_consuming()
