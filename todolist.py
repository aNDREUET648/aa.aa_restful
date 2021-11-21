from flask import Flask, abort, make_response, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

tasques = [
    {
        'id': 1,
        'categoria': 'Compras',
        'descripcio': 'Léche, Hüevos, Pizza, Queso', 
        'realitzada': False
    },
    {
        'id': 2,
        'categoria': 'Universidad',
        'descripcio': 'Acabar práctica AA.AA.', 
        'realitzada': False
    },
    {
        'id': 3,
        'categoria': 'Trabajo',
        'descripcio': 'Entregar informe semanal', 
        'realitzada': False
    },
    {
        'id': 4,
        'categoria': 'Universidad',
        'descripcio': 'Preparar examen ADIU', 
        'realitzada': False
    },
    {
      "categoria": "Compras",
      "descripcio": "Calgon, miel, suavizante",
      "id": 5,
      "realitzada": False
    },
    {
      "categoria": "Trabajo",
      "descripcio": "Revisión de todos los elemntos fuera de posición standard",
      "id": 6,
      "realitzada": False
    }
]

class ToDo(Resource): 
    '''
                    GET: obtener una tarea específica

                    (Según su 'id' (identificador))
    '''
    def get(self,tasca_id):
        tarea = [tasca for tasca in tasques if tasca['id'] == tasca_id]
        if len(tarea) == 0:
           responseBody = {"Error en cerca": "No l'he trobada"}
           return make_response(jsonify(responseBody), 404)
        return jsonify({'tasca': tarea[0]})

    '''
                    PUT: actualizar la información de una tarea específica

                    Se puede actualizar 'categoria', 'descripcio' y 'realitzada',
                    pero sólo esos campos. Uno a uno o todos a la vez
    '''
    def put(self,tasca_id):
        tarea = [tasca for tasca in tasques if tasca['id'] == tasca_id]
        if len(tarea) == 0:
           responseBody = {"Error en cerca": "No l'he trobada"}
           return make_response(jsonify(responseBody), 404)
        if not request.json:
           responseBody = {"Error en arguments o dades": "Falta categoria, json mal format o sense json"}
           return make_response(jsonify(responseBody), 400)
        
        # Tenemos 'categoria' por modificar y es distinto a lo que ya había
        if 'categoria' in request.json and tasques[tasca_id-1]['categoria'] != request.json['categoria']:
            tasques[tasca_id-1]['categoria'] = request.json['categoria']
        
        # Tenemos 'descripcio' por modificar y es distinto a lo que ya había
        if 'descripcio' in request.json and tasques[tasca_id-1]['descripcio'] != request.json['descripcio']:
            tasques[tasca_id-1]['descripcio'] = request.json['descripcio']
        
        # Tenemos 'realitzada' por modificar y es distinto a lo que ya había
        if 'realitzada' in request.json and tasques[tasca_id-1]['realitzada'] != request.json['realitzada']:
            '''
                    Resolución de problemas con Python True/False y JSON true/false

                    Si no escribes en la petición exactamente "true", siempre será "false"
            '''
            if request.json['realitzada'] == "true":
                tasques[tasca_id-1]['realitzada'] = True
            else:
                tasques[tasca_id-1]['realitzada'] = False
        return jsonify({'tasca': tasques[tasca_id-1]})

class ToDo_Crea_y_Lista(Resource):  
    '''
                    GET: obtener una lista de todas las tareas
    '''
    def get(self):
        return jsonify({'tasques': tasques})
    
    '''
                    POST: añadir una nueva tarea 
    '''
    def post(self):
       if not request.json or not 'categoria' in request.json:
          responseBody = {"Error en arguments o dades": "Falta categoria, json mal format o sense json"}
          return make_response(jsonify(responseBody), 400)
       if not 'descripcio' in request.json:
          responseBody = {"Error en arguments": "Falta afegir descripció de sa tasca"}
          return make_response(jsonify(responseBody), 400)
       tarea = {
           'id': tasques[-1]['id'] + 1,
           'categoria': request.json['categoria'],
           'descripcio': request.json['descripcio'],
           'realitzada': False
       }
       tasques.append(tarea)
       return jsonify({'tasca': tarea, 'Creada':'Nova tasca'})

class List_Categoria(Resource):
    '''
                    GET CATEGORIA: listado de todas las tareas de la categoria == "...."
                    /tasca/categoria/....
    '''
    def get(self,cat):
        tareas =[]
        for dict_item in tasques:
            if dict_item["categoria"] == cat:
                tareas.append(dict_item)
        return(jsonify(tareas))

class List_Realitzada(Resource):
    '''
                    GET REALITZADA: listado del estado de las tareas
                    /tasca/fet/1 ("SI")
                    /tasca/fet/0 ("NO")
    '''
    def get(self,flag):
        tareas =[]
        if flag == 1:
            fet = True
        elif flag == 0:
            fet = False
        else:
            responseBody = {"Error en arguments": "o 1 == SI o 0 == NO"}
            return make_response(jsonify(responseBody), 400)
        for dict_item in tasques:
            if dict_item["realitzada"] == fet:
                tareas.append(dict_item)
        return(jsonify(tareas))

class Esborra(Resource): 
    '''
                    DELETE: eliminar una tarea específica
                    (Según su 'id' (identificador))
    '''
    def delete(self,tasca_id):
        tarea = [tasca for tasca in tasques if tasca['id'] == tasca_id]
        if len(tarea) == 0:
           responseBody = {"Error en cerca": "No l'he trobada"}
           return make_response(jsonify(responseBody), 404)
        tasques.remove(tarea[0])
        return jsonify({'result': True})

'''
                    Añadir las rutas (route) hacia los recursos
'''
api.add_resource(ToDo, '/tasca/<int:tasca_id>')
api.add_resource(ToDo_Crea_y_Lista, '/tasca')
api.add_resource(List_Categoria, '/tasca/categoria/<string:cat>')
api.add_resource(List_Realitzada, '/tasca/fet/<int:flag>')
api.add_resource(Esborra, '/tasca/esborra/<int:tasca_id>')

if __name__ == '__main__':
    app.run(port='5000',debug=True)