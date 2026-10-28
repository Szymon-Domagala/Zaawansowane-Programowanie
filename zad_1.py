def greetings(name: str = "imie", surname: str = "nazwisko") -> str:
    return f"Cześć {name} {surname}!"


response = greetings("Szymon", "Domagała")
print(response)
