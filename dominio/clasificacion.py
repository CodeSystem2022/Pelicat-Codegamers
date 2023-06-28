class Clasificacion:
    def __init__(self, nombre):
        self._nombre = nombre
        self._clasificacion_id = None

    @property
    def clasificacion_id(self):
        return self._clasificacion_id

    @clasificacion_id.setter
    def clasificacion_id(self, valor):
        self._clasificacion_id = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
