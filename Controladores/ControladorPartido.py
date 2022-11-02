from Modelos.Partido import Partido
class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")

    def index(self):
        print("Listar todos los partidos")
        unPartido={

            "nombre":"Conservador Liberal",
            "lema": "Union por la nacion"

        }
        return [unPartido]

    def create(self,infoPartido):
        print("Crear un partido")
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def show(self,id):
        print("Mostrando un partido con id ",id)
        elPartido = {
            "_id": id,
            "nombre": "Conservador Liberal",
            "lema": "Union por la nacion"
        }
        return elPartido

    def update(self,id,infoPartido):
        print("Actualizando partido con id ",id)
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def delete(self,id):
        print("Elimiando partido con id ",id)
        return {"deleted_count":1}