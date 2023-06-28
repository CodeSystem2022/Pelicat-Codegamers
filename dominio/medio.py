class Medio:
    def __init__(self, nombre):
        self._nombre = nombre
        self._medio_id = None

    @property
    def medio_id(self):
        return self._medio_id

    @medio_id.setter
    def medio_id(self, valor):
        self._medio_id = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
