from Modelos.Mesa import Mesa
class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todos los mesas")
        unMesa={

            "numero":"1",
            "cantidad_inscritos": "120"

        }
        return [unMesa]

    def create(self,infoMesa):
        print("Crear una mesa")
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__

    def show(self,id):
        print("Mostrando una mesa con id ",id)
        elMesa = {
            "_id": id,
            "numero":"1",
            "cantidad_inscritos": "120"
        }
        return elMesa

    def update(self,id,infoMesa):
        print("Actualizando mesa con id ",id)
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__

    def delete(self,id):
        print("Elimiando mesa con id ",id)
        return {"deleted_count":1}