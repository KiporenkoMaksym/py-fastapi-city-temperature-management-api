import httpx


async def get_temperature(city_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city_name,
                "count": 1,
                "language": "en",
                "format": "json",
            },
        )

        data = response.json()

        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]

        response = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m",
            },
        )

        data = response.json()

        return data["current"]["temperature_2m"]
