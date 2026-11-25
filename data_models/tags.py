from dataclasses import dataclass


@dataclass
class Tag():
    userId: int
    movieId: int
    tag: str
    timestamp: int

    @classmethod
    def read_csv(cls, line: list) -> "Tag":
        return cls(
            userId=int(line[0].strip()),
            movieId=int(line[1].strip()),
            tag=line[2].strip(),
            timestamp=int(line[3])
        )
