class Categoria:
    def __init__(self, nombre):
        self._nombre = nombre
        self._categoria_id = None

    @property
    def categoria_id(self):
        return self._categoria_id

    @categoria_id.setter
    def categoria_id(self, valor):
        self._categoria_id = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valoror