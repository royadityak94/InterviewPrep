''''Fetch API asynchronously
    Using httpx and asyncio
'''
# Importing the required libraries
import httpx 
import asyncio
import pandas as pd

def format_parsed_record(input_json): 
    formatted_dict = {
        'name': input_json['name'],
        'order': input_json['order'],
        'species': input_json['species'], 
        'sprites': input_json['sprites']
    }
    return formatted_dict

async def get_pokemon(client, url):
    response = await client.get(url)
    pokemon = response.json()
    return format_parsed_record(pokemon)

async def crawler():
    all_pokemon = []
    async with httpx.AsyncClient() as client: 
        tasks = []
        for index in range(904):
            url = f'https://pokeapi.co/api/v2/pokemon/{index+1}'
            tasks += asyncio.ensure_future(get_pokemon(client, url)),

        all_tasks = await asyncio.gather(*tasks)
        for task in all_tasks:
            all_pokemon += task,
    return all_pokemon

def main():
    pokemons = asyncio.run(crawler())
    df = pd.DataFrame.from_dict(pokemons)
    print (df)


if __name__ == '__main__':
    main()