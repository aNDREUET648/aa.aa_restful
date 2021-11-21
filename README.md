
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
Cacheable : el servidor debe indicar al cliente si las solicitudes se pueden almacenar en caché o no.
Sistema en capas : la comunicación entre un cliente y un servidor debe estar estandarizada de tal manera que permita a los intermediarios responder a las solicitudes en lugar del servidor final, sin que el cliente tenga que hacer nada diferente.
Interfaz uniforme : el método de comunicación entre un cliente y un servidor debe ser uniforme.
Código a pedido : los servidores pueden proporcionar código ejecutable o scripts para que los clientes lo ejecuten en su contexto. Esta restricción es la única que es opcional.  
 Cualquier mensaje que envíe un jugador (escribir texto en su consola) al servidor será respondido con
 un mensaje del servidor tipo: 
 
  **Gracias _Thread n_, aún quedan _p_ clientes por conectar. Vamos a esperar**
 
| id  | categoria |  descripcio  | realitzada (boolean) |
| ------------ | ------------- | ------------- | ------------- |
| 1 | Compras | Léche, Hüevos, Pizza, Queso | False |
| 2 | Universidad | Acabar práctica AA.AA. | False |
| 3 | Trabajo | Entregar informe semanal | False |
| 4 | Universidad | Preparar examen ADIU | False |
| 5 | Compras | Calgon, miel, suavizante| False |
| 6 | Trabajo | Revisión de elementos FDS | False |



usando Python y el microframework Flask .


[Restful with Python:  Requests and Flask](https://realpython.com/api-integration-in-python/)
[Wikipedia. Representational state transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)
