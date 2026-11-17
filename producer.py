import argparse
import consumer

parser = argparse.ArgumentParser()
parser.add_argument(
    "--quantity",
    type=int,
    default=100,
    help="Ilość zadań w kolejce"
    )
args = parser.parse_args()

consumer.lock_file()
path = consumer.path

try:
    for i in range(args.quantity):
        with open(path, "a", encoding="utf-8") as file:
            file.write("Zadanie do wykonania - pending\n")
finally:
    consumer.lock_release()
