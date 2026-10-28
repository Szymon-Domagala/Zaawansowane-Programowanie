import requests
import argparse


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        address_1: str | None,
        address_2: str | None,
        address_3: str | None,
        city: str,
        state_province: str,
        postal_code: str,
        country: str,
        longitude: float | None,
        latitude: float | None,
        phone: str | None,
        website_url: str | None,
        state: str,
        street: str | None,
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self):
        return (
            f"ID: {self.id}"
            f"\nName: {self.name}"
            f"\nBrewery type: {self.brewery_type}"
            f"\nAddress 1: {self.address_1}"
            f"\nAddress 2: {self.address_2}"
            f"\nAddress 3: {self.address_3}"
            f"\nCity: {self.city}"
            f"\nState province: {self.state_province}"
            f"\nPostal code: {self.postal_code}"
            f"\nCountry: {self.country}"
            f"\nLongitude: {self.longitude}"
            f"\nLatitude: {self.latitude}"
            f"\nPhone: {self.phone}"
            f"\nWebsite URL: {self.website_url}"
            f"\nState: {self.state}"
            f"\nStreet: {self.street}"
        )


parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str, help="Miasto z którego pochodzi piwo")
args = parser.parse_args()

url = f"https://api.openbrewerydb.org/v1/breweries"

query_params = {"per_page": 20}

if args.city:
    query_params["by_city"] = args.city
try:
    response = requests.get(url, params=query_params)
    response.raise_for_status()
    api_data = response.json()

    brewery_list = [Brewery(**elements) for elements in api_data]

    index = 1
    for beer in brewery_list:
        print(
            f"=================================== {index} ==================================="
        )
        print(beer)
        index += 1
except requests.exceptions.RequestException as e:
    print(f"Błąd pobierania: {e}")
