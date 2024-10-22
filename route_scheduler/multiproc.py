from fastapi import FastAPI
from concurrent.futures import ProcessPoolExecutor
import time
import multiprocessing

app = FastAPI()

# Creamos un pool de procesos con el número de núcleos de CPU disponibles
executor = ProcessPoolExecutor(max_workers=multiprocessing.cpu_count())

def cpu_intensive_task(seconds: int):
    start = time.time()
    # Una tarea intensiva en CPU (por ejemplo, contar números grandes)
    count = 0
    for i in range(10**7):
        count += i ** 2
    end = time.time()
    return f"Tarea completada en {end - start} segundos."

@app.get("/cpu-intensive")
async def run_cpu_task():
    # Ejecutamos la tarea en un proceso paralelo
    future = executor.submit(cpu_intensive_task, 5)
    result = await asyncio.wrap_future(future)  # Esperamos el resultado
    return {"message": result}

