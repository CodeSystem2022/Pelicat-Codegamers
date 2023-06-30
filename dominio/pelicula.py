from sty import fg, bg, ef, rs

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
    # Metodo para obtener el valor textual de la clasificacion basado en su ID numerico
    def clasificacion(cls, clasificacion_id):
        return cls.clasificaciones.get(clasificacion_id, 'Desconocido')

    @classmethod
    # Metodo para obtener el valor textual de la clasificacion basado en su ID numerico
    def categoria(cls, categoria_id):
        return cls.categorias.get(categoria_id, 'Desconocido')


    def __init__(self, pelicula_id, titulo, director, anio, medio, comentario, clasificacion_id, categoria_id):
        self._pelicula_id = pelicula_id
        self._titulo = titulo
        self._director = director
        self._anio = anio
        self._medio = medio
        self._comentario = comentario
        self._clasificacion_id = clasificacion_id
        self._categoria_id = categoria_id

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, valor):
        self._director = valor

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        self._anio = valor

    @property
    def medio(self):
        return self._medio

    @medio.setter
    def medio(self, valor):
        self._medio = valor

    @property
    def comentario(self):
        return self._comentario

    @comentario.setter
    def comentario(self, valor):
        self._comentario = valor

    @property
    def clasificacion_id(self):
        return self._clasificacion_id

    @clasificacion_id.setter
    def clasificacion_id(self, valor):
        self._clasificacion_id = valor

    @property
    def categoria_id(self):
        return self._categoria_id

    @categoria_id.setter
    def categoria_id(self, valor):
        self._categoria_id = valor

    @property
    def pelicula_id(self):
        return self._pelicula_id

    @pelicula_id.setter
    def pelicula_id(self, valor):
        self._pelicula_id = valor

    def __str__(self):
        retorno = bg.red + ef.italic + f'{self.pelicula_id}: {self.titulo}\n' + rs.italic + bg.rs
        retorno += bg.da_blue + f'{self.director} ({self._anio}) Medio: {self.medio}\n'
        retorno += f'Comentario: {self.comentario}\n'
        retorno += 'Clasificación: '+Pelicula.clasificaciones[self.clasificacion_id]
        retorno += ' Categoría: '+Pelicula.categorias[self.categoria_id] +'\n'  + bg.rs
        return retorno
