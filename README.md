
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

## Ejecución de las pruebas

 Existen muchas formas de probar una API REST, algunas sofisticadas como [Postman](https://www.postman.com/) (app o extensión) o [YARC! Yet Another REST Client!](https://yet-another-rest-client.com/) (extensión de Chrome), otras, más rudimentarias, pero no por ello menos efectivas, por ejemplo, la herramienta por línea de comandos [cURL](https://curl.se/).
 Las pruebas por tema de agilidad las he realizado con YARC! pero para una completa comprensión de la API mostraré el estilo de codificación con los comandos de cURL:
  
### 
 Con el fin de facilitar las pruebas he definido una serie de registros (diccionarios) por defecto. El formato de intercambio de datos que emplearé por defecto será JSON:
 
| id  | categoria |  descripcio  | realitzada (boolean) |
| ------------ | ------------- | ------------- | ------------- |
| 1 | Compras | Léche, Hüevos, Pizza, Queso | False |
| 2 | Universidad | Acabar práctica AA.AA. | False |
| 3 | Trabajo | Entregar informe semanal | False |
| 4 | Universidad | Preparar examen ADIU | False |
| 5 | Compras | Calgon, miel, suavizante| False |
| 6 | Trabajo | Revisión de elementos FDS | False |

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
