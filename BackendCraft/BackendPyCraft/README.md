PyTypeCraft
===========
La siguiente api, fue realizada con FastApi, el cual es un framework de desarrollo web de alto rendimiento para crear APIs
(Interfaces de Programacion de Aplicaciones) en Python. Se escogio este framework por su facilidad de uso, y por el tiempo 
de desarrollo que se tenia para realizar la api.
## Instalacion
Para instalar la api, se debe clonar el repositorio, y luego llegar hasta la carpeta "BackendPyCraft". Y ejecutar los siguientes comandos
#### Donde fastapi-env es el nombre del entorno virtual pero de puede cambiar
```bash
     python3.9.0 -m venv fastapi-env
```
tenemos que activar el entorno virtual, y si no se cambio el nombre anteriormente, se ejecuta el siguiente comando
```bash
     source fastapi-env/bin/activate
```
luego tenemos que installar FastApi y Uvicorn, con el siguiente comando
```bash
     pip install fastapi
     pip install uvicorn
```
y de ultimo, si realizamos bien los pasos anterior deberiamos ejecutar:
```bash
     uvicorn api_rest:app --reload
```
y ya tendriamos la api corriendo en el puerto  http://127.0.0.1:8000