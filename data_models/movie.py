from dataclasses import dataclass


@dataclass
class Movie():
    id: int
    title: str
    description: str

    @classmethod
    def read_csv(cls, line: list) -> "Movie":
        return cls(
            id=int(line[0].strip()),
            title=line[1].strip(),
            description=line[2]
        )
