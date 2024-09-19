import asyncio
import aiohttp
import time
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Configuración de la URL y las coordenadas de prueba
URL = "http://10.1.0.3:8000/get_route"
START_COORDS = (-3.688340, 40.453219)
END_COORDS = (-3.711404, 40.423988)
NUM_REQUESTS = 10

async def fetch_route(session, url, payload, request_id):
    start_time = time.time()
    logger.info(f"Sending request {request_id}")
    async with session.post(url, json=payload) as response:
        response_time = time.time() - start_time
        result = await response.json()
        mode = result.get('mode', 'unknown')
        logger.info(f"Respuesta recibida {request_id}, Modo: {mode}, Estado: {response.status}, Tiempo de respuesta desde ORS: {response_time:.2f} segundos")
        return response.status, result, response_time

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        payload = {"start": START_COORDS, "end": END_COORDS}

        for i in range(NUM_REQUESTS):
            tasks.append(fetch_route(session, URL, payload, i +1))

        results = await asyncio.gather(*tasks)


        for idx, (status, result, response_time) in enumerate(results):
            mode = result.get('mode', 'unknown')
            logger.info(f"Request {idx + 1}: Estado {status}, Modo {mode}, Tiempo {response_time:.2f} segundos, Resultado {result}")
                

if __name__ == "__main__":
    asyncio.run(main())
