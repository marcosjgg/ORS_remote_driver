import asyncio
import aiohttp
import time

# Configuración de la URL y las coordenadas de prueba
URL = "http://10.1.0.3:8000/change_route"
START_COORDS = (-3.688340, 40.453219)
END_COORDS = (-3.711404, 40.423988)
NUM_REQUESTS = 10

async def fetch_route(session, url, payload):
    start_time = time.time()
    async with session.post(url, json=payload) as response:
        response_time = time.time() - start_time
        result = await response.json()
        return response.status, result, response_time

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        payload = {"start": START_COORDS, "end": END_COORDS}

        for _ in range(NUM_REQUESTS):
            tasks.append(fetch_route(session, URL, payload))

        results = await asyncio.gather(*tasks)


        for idx, (status, result, response_time) in enumerate(results):
                print(f"Request {idx + 1}: Status {status}, Time {response_time:.2f} seconds, Result {result}")

if __name__ == "__main__":
    asyncio.run(main())
