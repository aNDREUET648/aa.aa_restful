
# Arquitecturas Avanzadas. Práctica 2. 

_API para gestionar listas de tareas TODO. Implementado en Flask-RESTful_

## Enunciado

 Design an API how manages a list of TODO tasks. The requirements are:

Manage multiples lists. Lists by category. I.e. Shopping, Work, House,...
  - Get a list of all TODO items by default from all categories or specifing one category
  - Add new item in a specific list
  - Remove one item from a specific list


 ---
[Enunciado Original](https://github.com/aNDREUET648/aa.aa_restful/blob/master/Restful_with_Flask.ipynb). Final del documento Actividad A3
 
 
## Aspectos iniciales

  Una API de REST, o API de RESTful, es una interfaz de programación de aplicaciones (API o API web) diseñada con los conceptos de la arquitectura REST y permite la interacción con los servicios web de RESTful:
  - **Recurso**: todo dentro de una API RESTful debe ser un recurso.
  - **URI**: los recursos en REST siempre se manipulan a partir de la URI (Identificadores Universales de Recursos).
  - **Acción**: todas las peticiones a tu API RESTful deben estar asociadas a uno de los verbos de HTTP: GET, POST, PUT y DELETE.
    
 Las características de un sistema REST están definidas por seis reglas de diseño:

  - **Cliente-Servidor**: Debe existir una separación entre el servidor que ofrece un servicio y el cliente que lo consume.
  - **Stateless**: Cada solicitud de un cliente debe contener toda la información requerida por el servidor para llevar a cabo la solicitud. El servidor no puede almacenar información proporcionada por el cliente en una solicitud y utilizarla en otra solicitud.
  - **Cacheable**: el servidor debe indicar al cliente si las solicitudes se pueden almacenar en caché o no.
  - **Sistema en capas**: el cliente puede acceder a los recursos del servidor de forma indirecta a través de otras capas, como un proxy o un equilibrador de carga sin que el cliente tenga que hacer nada diferente.
  - **Interfaz uniforme**: el servidor proporcionará una interfaz uniforme para acceder a los recursos sin definir su representación.
  - **Código a pedido (opcional)**: los servidores pueden proporcionar código ejecutable o scripts para que los clientes lo ejecuten en su contexto. 

## Identificación de los recursos

 Para el consumo de los servicios que ofrece la API REST es necesario definir los recursos. Al tratarse de una lista de tareas, mi único recurso expuesto será **tasca**, el cual tiene los siguientes campos:
 
 - **id**: URI único para la tarea. Tipo int.
 - **categoria**: Descripción corta de la tarea. Tipo string.
 - **descripcio**: Descripción larga de la tarea.  Tipo string.
 - **realitzada**: Estado de finalización de la tarea. Tipo boolean.
 
## Definición de los "puntos finales"(endpoints)

| Método HTTP | Endpoint |  Descripció  |
| -------- | --------- | ---------- |
|   GET    | /tasca    |   Lista de todas las tareas  |
|   GET    | /tasca/<int:tasca_id> | Vsualización de una tarea específica |
|   GET    | /tasca/categoria/<string:cat> | Lista de todas las tareas de una determinada categoría |
|   GET    | /tasca/fet/0    | Lista todas las tareas pendientes |
|   GET    | /tasca/fet/1    | Lista todas las tareas realizadas |
|   PUT    | /tasca/<int:tasca_id> | Actualiza una tarea determinada. 'categoria', 'descripcio' y 'realitzada' |
|   POST   | /tasca    | Añade una nueva tarea |
|   DELETE | /tasca/esborra/<int:tasca_id> | Eliminar una tarea determinada |

## Ejecución de la interfaz

 Existen muchas formas de probar una API REST, algunas sofisticadas como [Postman](https://www.postman.com/) (app o extensión) o [YARC! Yet Another REST Client!](https://yet-another-rest-client.com/) (extensión de Chrome), otras, más rudimentarias, pero no por ello menos efectivas, por ejemplo, la herramienta por línea de comandos [cURL](https://curl.se/).
 Las pruebas por tema de agilidad las he realizado con YARC! pero para una completa comprensión de la API mostraré el estilo de codificación con los comandos de cURL:

## Pruebas
 
 Con el fin de facilitar las pruebas he definido una serie de registros (diccionarios) por defecto. El formato de intercambio de datos que emplearé por defecto será JSON:
 
| id  | categoria |  descripcio  | realitzada (boolean) |
| ------------ | ------------- | ------------- | ------------- |
| 1 | Compras | Léche, Hüevos, Pizza, Queso | False |
| 2 | Universidad | Acabar práctica AA.AA. | False |
| 3 | Trabajo | Entregar informe semanal | False |
| 4 | Universidad | Preparar examen ADIU | False |
| 5 | Compras | Calgon, miel, suavizante| False |
| 6 | Trabajo | Revisión de elementos FDS | False |


Tras iniciar la aplicación 
 
```
$python3 todolist.py
```
 
Abrimos sesión desde otro terminal (local o remoto perteneciente a la LAN) e iremos invocando el comando curl para la realización de las peticiones: 

### HTTP GET - Lista de todas las tareas
```
$curl http://localhost:9999/tasca
```
### HTTP GET - Visualización de la tarea 4
```
$curl http://localhost:9999/tasca/4
```
### HTTP GET - Lista de todas las tareas con la categoría Universidad
```
$curl http://localhost:9999/tasca/categoria/Universidad
```
### HTTP GET - Lista de todas las tareas pendientes
```
$curl http://localhost:9999/tasca/fet/0
```
### HTTP PUT - Actualiza la tarea 3 y diremos que está acabada
En este caso, debemos indicar que el encabezado que le pasaremos será tipo json (opción -H) y el método HTTP PUT (opción -X).
Los datos los especificamos con -d (o --data) y el formato es entre comillas simples.
Destacar que JSON reconoce true y false como operaciones booleanas, en cambio, Python las ve como True o False
```
$curl -H "Content-Type: application/json" -d '{"realitzada":"true"}' -X PUT http://localhost:9999/tasca/3
```
Si todo ha sido correcto nos devolverá:
```
{"Tasca actualitzada": {"categoria":"Trabajo","descripcio":"Entregar informe semanal", "id": 3, "realitzada": true}}
```


### HTTP POST - Añade una nueva tarea
```
$curl -H "Content-Type: application/json" -d '{"categoria":"Trabajo","descripcio":"Cerrar línea GALILEA","realitzada":"true"}' -X POST http://localhost:9999/tasca
```
Si todo ha sido correcto nos devolverá:
```
{"Creada": "Nova tasca", "tasca":{"categoria":"Trabajo","descripcio":"Cerrar línea GALILEA", "id": 7, "realitzada": true}}
```


### HTTP DELETE - Eliminar tarea 2
```
$curl -X DELETE http://localhost:9999/tasca/esborra/2
```
Si el resultado es satisfactorio nos devolverá un json:
```
{"eliminat": true}
```
## Particularidades ⚙️

_Servidor_


La claúsula __main__ simplemente visualiza los hilos activos en ese momento. 
Cabe destacar que si se ejecuta desde un _Visual Studio Code_ aparecen inicialmente 6 hilos:
### 


## Dependencias

Para la realización de la API en Python he requerido de los siguientes "micro" framework y extensiones:

 - Flask              2.0.2    (micro framework para Python)
 - Flask-Jsonpify     1.5.0    (extensión para Flask)
 - Flask-RESTful      0.3.9    (extensión para Flask)


## Bibliografía y documentación utilizada

[Restful with Python:  Requests and Flask](https://realpython.com/api-integration-in-python/)

[Wikipedia. Representational state transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)

[FlaskRESTful Website](https://flask-restful.readthedocs.io/en/latest/index.html)

[Flask Website](https://flask.palletsprojects.com/en/2.0.x/)
