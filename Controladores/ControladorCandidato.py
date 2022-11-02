from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")

    def index(self):
        print("Listar todos los candidatos")
        unCandidato={

            "cedula":"24000000",
            "numero_resolucion": "1000111",
            "nombre": "Kim",
            "apellido": "Jong-Un"

        }
        return [unCandidato]

    def create(self,infoCandidato):
        print("Crear una candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def show(self,cedula):
        print("Mostrando una candidato con cedula ",cedula)
        elCandidato = {
            "cedula": 24000000,
            "numero_resolucion": "1000111",
            "nombre": "Kim",
            "apellido": "Jong-Un"
        }
        return elCandidato

    def update(self,id,infoCandidato):
        print("Actualizando candidato con id ",id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self,id):
        print("Elimiando candidato con id ",id)
        return {"deleted_count":1}