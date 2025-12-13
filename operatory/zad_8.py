from typing import List
import requests
import argparse

URL_API = 'https://api.openbrewerydb.org/v1/breweries'


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        street: str,
        city: str,
        state: str,
        postal_code: str,
        country: str,
        phone: str,
        website_url: str
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return (f"Brewery '{self.name}' ({self.brewery_type})\n"
                f"Address: {self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}\n"
                f"Phone: {self.phone}\n"
                f"Website: {self.website_url}\n")


def get_breweries_from_api(city: str | None = None) -> list:
    params = {"per_page": 20}
    if city:
        params["by_city"] = city
    response = requests.get(URL_API, params=params)
    response.raise_for_status()
    return response.json()


def brewery_factory(breweries: list) -> List[Brewery]:
    return [Brewery(
        id=b.get("id", ""),
        name=b.get("name", ""),
        brewery_type=b.get("brewery_type", ""),
        street=b.get("street", ""),
        city=b.get("city", ""),
        state=b.get("state", ""),
        postal_code=b.get("postal_code", ""),
        country=b.get("country", ""),
        phone=b.get("phone", ""),
        website_url=b.get("website_url", "")
    ) for b in breweries]


def get_args():
    parser = argparse.ArgumentParser(description='Display breweries, optionally filtered by city.')
    parser.add_argument('-c', '--city', help='Filter breweries by city', required=False)
    return vars(parser.parse_args())


def main():
    args = get_args()
    breweries_data = get_breweries_from_api(city=args['city'])
    brewery_list = brewery_factory(breweries_data)

    if not brewery_list:
        print("No breweries found.")
    for brewery in brewery_list:
        print(brewery)


if __name__ == "__main__":
    main()
