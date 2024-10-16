# ORS_remote_driver
## Información general
En este proyecto, se utiliza openrouteservice locally para la implementación de un servicio de petición de rutas simultáneamente.
En modo general se crea un entorno virtual con la herrramienta de virtualización VNX (figura), con tres contenedores lxc:
 - ORS: servidor donde está instalado openrouteservice, y al cual se le harán las peticiones de ruta.
 - route_scheduler: servidor que prepara las peticiones a ORS y procesa sus respuestas.
 - remote_driver: simulación del entorno de un conductor remoto, que solicita una ruta desde una coordenada X a una coordenada Y.

## Instalación de ORS de manera local
Se instala openrouteservice de manera local, tal como se indica en la página web oficial https://giscience.github.io/openrouteservice/run-instance/building-from-source.

Dentro del contenedor ORS, seguir los pasos de instalación.

### Configuraciones
Para cargar los datos de la localización geográfica deseada, se deben descargar del sitio web https://download.geofabrik.de/ y ser cargados en la ruta ors-api/src/test/files y eliminar el archivo por defecto heidelberg.osm.gz.

** Los formatos soportados de OSM son .osm, .osm.gz, .osm.zip y .pbf.

Con el objetivo de que los datos geográficos sean inicializados en ORS, hay que eliminar los datos dentro de los directorios ./graphs y  ./elevation_cache.

Modificar el archivo ors-config.yml con el nombre del archivo descargado.
Luego de realizar esta configuración inicial, iniciar ORS con el comando mvn spring-boot:run

## route_scheduler
Se puede inicializar route_scheduler ejecutando el script route_scheduler.py

Para su correcto funcionamiento, se requiere la instalación en el entorno de FastAPI y de Pydantic.

## remote_driver
Para inicializar el contenedor de remote_driver, se ejecuta el script parallel_requests.py
