from data_models.movie import Movie
from data_models.tags import Tag
from data_models.links import Link
from data_models.ratings import Rating
from fastapi import FastAPI
import csv


app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/movies")
def read_movies():
    movie_list = []
    with open(
        r"C:\Users\Student\Desktop\database\movies.csv",
        "r",
        encoding="utf-8"
    ) as file:
        reader = csv.reader(file)
        next(reader, None)

        for line in reader:
            if not line:
                continue
            movie = Movie.read_csv(line=line)
            movie_list.append(movie.__dict__)

    return movie_list


@app.get("/links")
def read_links():
    links_list = []
    with open(
        r"C:\Users\Student\Desktop\database\links.csv",
        "r",
        encoding="utf-8"
    ) as file:
        reader = csv.reader(file)
        next(reader, None)

        for line in reader:
            if not line:
                continue
            link = Link.read_csv(line)
            links_list.append(link.__dict__)

    return links_list


@app.get("/ratings")
def read_ratings():
    rating_list = []
    with open(
        r"C:\Users\Student\Desktop\database\ratings.csv",
        "r",
        encoding="utf-8"
    ) as file:
        reader = csv.reader(file)
        next(reader, None)

        for line in reader:
            if not line:
                continue
            rating = Rating.read_csv(line)
            rating_list.append(rating.__dict__)

    return rating_list


@app.get("/tags")
def read_tags():
    tags_list = []
    with open(
        r"C:\Users\Student\Desktop\database\tags.csv",
        "r",
        encoding="utf-8"
    ) as file:
        reader = csv.reader(file)
        next(reader, None)

        for line in reader:
            if not line:
                continue
            tag = Tag.read_csv(line)
            tags_list.append(tag.__dict__)

    return tags_list
