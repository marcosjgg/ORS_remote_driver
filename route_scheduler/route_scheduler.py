from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import json
import random
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dirección del servidor ORS
ORS_URL = 'http://10.1.0.2:8082/ors/v2/directions/driving-car'

class RouteRequest(BaseModel):
    start: tuple
    end: tuple

def load_mode_config(mode):
        with open(f'{mode}.json', 'r') as file:
            return json.load(file)

def get_route_from_ors(start, end, mode):
    config = load_mode_config(mode)
    config['coordinates'] = [start, end]

    headers = {
            'Content-Type':'application/json'
            }

    logger.info(f"Sending request to ORS for mode: {mode}")
    start_ors = time.time()
    response = requests.post(ORS_URL, json=config, headers=headers)
    end_ors = time.time()


    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Error al obtener ruta de ORS: {response.text}")

    try:
        response_json = response.json()
        logger.info(f"Received response from ORS for mode: {mode}, Time taken: {end_ors - start_ors:.2f} seconds")
        return response_json
    except json.JSONDecodeError:
        raise HTTPException(status_code=500,detail="Error al decodificar respuesta de ORS")

@app.post("/change_route")
async def change_route(request: RouteRequest):
    try:
        start_time = time.time()
        logger.info(f"Recieved request: {request}")
        
        mode = random.choice(['simple_route', 'avoid_polygons', 'alternative_routes'])
        route_data = get_route_from_ors(request.start, request.end, mode)
        
        end_time = time.time()
        logger.info(f"Processed request: {request}, Total time taken: {end_time - start_time:2.f} seconds")
        return route_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/get_route")
async def get_route(request: RouteRequest):
    try:
        start_time = time.time()
        logger.info(f"Received request: {request}")
        
        mode = random.choice(['simple_route', 'avoid_polygons', 'alternative_routes'])
        route_data = get_route_from_ors(request.start, request.end, mode)
        
        end_time = time.time() 
        logger.info(f"Processed request: {request}, Total time taken: {end_time - start_time:.2f} seconds")
        return route_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=8000)

