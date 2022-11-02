from Modelos.Resultado import Resultado
class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")

    def index(self):
        print("Listar todos los resultados")
        unResultado={

            "id":"r123",
            "numero_mesa": "1",
            "id_partido": "1"

        }
        return [unResultado]

    def create(self,infoResultado):
        print("Crear una resultado")
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def show(self,id):
        print("Mostrando una resultado con id ",id)
        elResultado = {
            "_id": id,
            "numero_mesa":"1",
            "id_partido": "1"
        }
        return elResultado

    def update(self,id,infoResultado):
        print("Actualizando resultado con id ",id)
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def delete(self,id):
        print("Elimiando resultado con id ",id)
        return {"deleted_count":1}