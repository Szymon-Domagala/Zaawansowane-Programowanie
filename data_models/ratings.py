from dataclasses import dataclass


@dataclass
class Rating():
    userId: int
    movieId: int
    rating: float
    timestamp: float

    @classmethod
    def read_csv(cls, line: list) -> "Rating":
        return cls(
            userId=int(line[0].strip()),
            movieId=int(line[1].strip()),
            rating=float(line[2].strip()),
            timestamp=float(line[3])
        )
