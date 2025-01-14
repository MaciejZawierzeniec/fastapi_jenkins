import httpx

async def get_pokemon_data(name: str):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.json()
        return None
