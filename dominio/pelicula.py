class Pelicula:

    clasificaciones = {
        1: 'ATP',
        2: 'PG',
        3: 'PG-13',
        4: 'NC16',
        5: 'M-18'
    }
    categorias = {
        1: 'Acción',
        2: 'Aventura',
        3: 'Catástrofe',
        4: 'Ciencia Ficción',
        5: 'Comedia',
        6: 'Documentales',
        7: 'Drama',
        8: 'Fantasía'
    }
@classmethod
    # Lógica para obtener el valor textual de la clasificacion basado en su ID numerico
    # Supongamos que tenemos un diccionario de mapeo entre los ID numericos y los valores textuales
    def clasificacion(cls, clasificacion_id):
        return cls.clasificaciones.get(clasificacion_id, 'Desconocido')

    @classmethod
    # Lógica para obtener el valor textual de la clasificacion basado en su ID numerico
    # Supongamos que tenemos un diccionario de mapeo entre los ID numericos y los valores textuales
    def categoria(cls, categoria_id):
        return cls.categorias.get(categoria_id, 'Desconocido')


    def _init_(self, pelicula_id, titulo, director, anio, medio, comentario, clasificacion_id, categoria_id):
        self._pelicula_id = pelicula_id
        self._titulo = titulo
        self._director = director
        self._anio = anio
        self._medio = medio
        self._comentario = comentario
        self._clasificacion_id = clasificacion_id
        self._categoria_id = categoria_id
        self._pelicula_id = None

