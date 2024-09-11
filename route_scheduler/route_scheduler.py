from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import json
import random

app = FastAPI()

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

    response = requests.post(ORS_URL,json=config,headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Error al obtener ruta de ORS: {response.text}")

    try:
        response_json = response.json()
        return response_json
    except json.JSONDecodeError:
        raise HTTPException(status_code=500,detail="Error al decodificar respuesta de ORS")

@app.post("/change_route")
async def change_route(request: RouteRequest):
    try:
        mode = random.choice(['simple_route', 'avoid_polygons', 'alternative_routes'])
        route_data = get_route_from_ors(request.start, request.end, mode)
        return route_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/get_route")
async def get_route(request: RouteRequest):
    try:
        mode = random.choice(['simple_route', 'avoid_polygons', 'alternative_routes'])
        route_data = get_route_from_ors(request.start, request.end, mode)
        return route_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=8000)

