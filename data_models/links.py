from dataclasses import dataclass


@dataclass
class Link():
    movieId: int
    imdbId: str
    tmdbId: int

    @classmethod
    def read_csv(cls, line: list) -> "Link":
        return cls(
            movieId=int(line[0].strip()),
            imdbId=line[1].strip(),
            tmdbId=int(line[2]) if line[2].strip() else None
        )
