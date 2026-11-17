import time
import os

path = "que.txt"
lock_path = "que.lock"


def lock_file():
    while True:
        try:
            with open(lock_path, "x"):
                pass
            break
        except FileExistsError:
            time.sleep(0.5)


def lock_release():
    if os.path.exists(lock_path):
        os.remove(lock_path)


if __name__ == "__main__":
    while True:
        task_line = 0
        found = False
        time.sleep(5)

        lock_file()
        try:
            if os.path.exists(path):
                new_lines = []
                with open(path, "r", encoding="utf-8") as file:
                    for index, line in enumerate(file):
                        raw_line = line.rstrip()
                        parts = raw_line.rsplit(" ", 1)
                        if parts[-1] == "pending" and not found:
                            parts[-1] = "in_progress"
                            task_line = index
                            found = True
                            print(f"Przejęto zadanie - {task_line + 1}")
                        modified_line = " ".join(parts) + "\n"
                        new_lines.append(modified_line)

                if found:
                    with open(path, "w", encoding="utf-8") as file:
                        file.writelines(new_lines)
        finally:
            lock_release()

        if found:
            time.sleep(30)

            lock_file()
            try:
                new_lines = []
                with open(path, "r", encoding="utf-8") as file:
                    for index, line in enumerate(file):
                        raw_line = line.rstrip()
                        parts = raw_line.rsplit(" ", 1)
                        if index == task_line:
                            parts[-1] = "done"
                            print(f"Wykonano zadanie - {task_line + 1}")
                        modified_line = " ".join(parts) + "\n"
                        new_lines.append(modified_line)

                with open(path, "w", encoding="utf-8") as file:
                    file.writelines(new_lines)
            finally:
                lock_release()
