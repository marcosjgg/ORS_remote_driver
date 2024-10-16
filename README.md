# ORS_remote_driver
## Información general
En este proyecto, se utiliza openrouteservice locally para la implementación de un servicio de petición de rutas simultáneamente.
En modo general se crea un entorno virtual con la herrramienta de virtualización VNX (figura), con tres contenedores lxc:
 - ORS: servidor donde está instalado openrouteservice, y al cual se le harán las peticiones de ruta.
 - route_scheduler: servidor que prepara las peticiones a ORS y procesa sus respuestas.
 - remote_driver: simulación del entorno de un conductor remoto, que solicita una ruta desde una coordenada X a una coordenada Y.

