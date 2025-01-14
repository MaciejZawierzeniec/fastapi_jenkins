from fastapi import FastAPI, HTTPException
from app.poke_client import get_pokemon_data

app = FastAPI()

@app.get("/pokemon/{name}")
async def read_pokemon(name: str):
    pokemon_data = await get_pokemon_data(name)
    if pokemon_data is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon_data
  
