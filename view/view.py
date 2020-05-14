class View:

    """
    """""""""""""""""""""""""""""
    "   A view for a MoviesDB  "
    """"""""""""""""""""""""""""
    """

    def start(self):
        print("""""""""""""""""""""""""")
        print("      ¡Bienvenido!      ")
        print("""""""""""""""""""""""""")
    
    def end(self):
        print("""""""""""""""""""""""""")
        print("     ¡Hasta pronto!     ")
        print("""""""""""""""""""""""""")

    def main_menu(self):
        print("""""""""""""""""""""""""")
        print(" -- Menú Principal   --  ")
        print("""""""""""""""""""""""""")


        print("1. Peliculas")
        print("2. Actores")
        print("3. Directores")
        print("4. Generos")
        print("5. Actores y Peliculas")
        print("6. Directores y Peliculas")
        print("7. Generos y Peliculas")
        print("8. Salir")

    def option(self, last):
        print("Selecciona una opcion (1 - " + last + '): ', end="")
    
    def not_valid_option(self):
        print("¡Opción no valida.!")
    
    def ask(self, output):
        print(output, end="")
    
    def msg(self,output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+ ' se '+op+' correctamente! + ')
        print('+'*(len(str(id))+len(op)+24))
    

    def ok_double_id(self, id1, id2, op):
        print('+'*(len(str(id1))+len(op)+24))
        print('+ ¡'+str(id1)+ ' y ' + str(id2) + ' se '+op+' correctamente! + ')
        print('+'*(len(str(id1))+len(op)+24))

    def error(self,err):
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))
    

    """
    """""""""""""""""""""""""""""
    "   View for Peliculas     "
    """"""""""""""""""""""""""""
    """

    def peliculas_menu(self):
        print("*************************************")
        print("*    * -- Submenú Peliculas -- *    *")
        print("*************************************")
        print("1. Agregar pelicula")
        print("2. Leer todas las peliculas")
        print("3. Leer pelicula por id")
        print("4. Leer pelicula por nombre")
        print("5. Actualizar pelicula")
        print("6. Eliminar pelicula")
        print("7. Regresar al menú principal")

    def ver_pelicula(self,record):
        print('ID:',record[0])
        print('Nombre:',record[1])
        print('Sipnosis:',record[2])
        print('Lanzamiento:',record[3])

    def ver_pelicula_header(self, header):
        print(header.center(78,'*'))
        print('-'*78)

    def ver_pelicula_midder(self):
        print('-'*78)

    def ver_pelicula_footer(self):
        print('*'*78)

    """
    """""""""""""""""""""""""""""
    "   View for Actores       "
    """"""""""""""""""""""""""""
    """

    def actores_menu(self):
        print("*************************************")
        print("*     * -- Submenú Actores -- *     *")
        print("*************************************")
        print("1. Agregar actor")
        print("2. Leer todos los actores")
        print("3. Leer actor por id")
        print("4. Leer actor por nombre")
        print("5. Actualizar actor")
        print("6. Eliminar actor")
        print("7. Regresar al menú principal")

    def ver_actor(self,record):
        print('ID:',record[0])
        print('Nombre:',record[1])
        print('Telefono:',record[2])
        print('Correo:',record[3])
        print('Direccion:',record[4])

    def ver_actor_header(self, header):
        print(header.center(78,'*'))
        print('-'*78)

    def ver_actor_midder(self):
        print('-'*78)

    def ver_actor_footer(self):
        print('*'*78)

    """
    """""""""""""""""""""""""""""
    "   View for Directores       "
    """"""""""""""""""""""""""""
    """

    def directores_menu(self):
        print("*************************************")
        print("*   * -- Submenú Directores -- *    *")
        print("*************************************")
        print("1. Agregar director")
        print("2. Leer todos los directores")
        print("3. Leer director por id")
        print("4. Leer director por nombre")
        print("5. Actualizar director")
        print("6. Eliminar director")
        print("7. Regresar al menú principal")

    def ver_director(self,record):
        print('ID:',record[0])
        print('Nombre:',record[1])
        print('Telefono:',record[2])
        print('Correo:',record[3])
        print('Direccion',record[4])

    def ver_director_header(self, header):
        print(header.center(78,'*'))
        print('-'*78)

    def ver_director_midder(self):
        print('-'*78)

    def ver_director_footer(self):
        print('*'*78)

    """
    """""""""""""""""""""""""""""
    "   View for Generos       "
    """"""""""""""""""""""""""""
    """

    def genero_menu(self):
        print("*************************************")
        print("*     * -- Submenú Generos -- *     *")
        print("*************************************")
        print("1. Agregar genero")
        print("2. Leer todos los generos")
        print("3. Leer genero por id")
        print("4. Leer genero por nombre")
        print("5. Actualizar genero")
        print("6. Eliminar genero")
        print("7. Regresar al menú principal")

    def ver_genero(self,record):
        print('ID:',record[0])
        print('Nombre:',record[1])


    def ver_genero_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_genero_midder(self):
        print('-'*48)

    def ver_genero_footer(self):
        print('*'*48)


    """
    """""""""""""""""""""""""""""
    "   View for Peliculas_Actores       "
    """"""""""""""""""""""""""""
    """

    def actores_peliculas_menu(self):
        print("*************************************************")
        print("*     * -- Submenú Peliculas y Actores -- *     *")
        print("*************************************************")
        print("1. Agregar pelicula - actor")
        print("2. Leer todas las peliculas de todos los actores")
        print("3. Leer pelicula y actor por id")
        print("4. Leer pelicula por id de actor")
        print("5. Actualizar actor - pelicula")
        print("6. Eliminar actor-pelicula")
        print("7. Regresar al menú principal")

    def ver_actor_pelicula(self,record):
        print('ID_Actor:',record[0])
        print('ID_Pelicula:',record[5])
        print("Datos del actor".center(81,'*'))
        self.ver_actor(record[0:5])
        print("Datos de la pelicula".center(81,'*'))
        self.ver_pelicula(record[5:])

    def ver_actor_pelicula_header(self, header):
        print(str(header).center(180,'*'))
        print('-'*180)

    def ver_actor_pelicula_midder(self):
        print('/'*180)

    def ver_actor_pelicula_footer(self):
        print('*'*180)

    """
    """""""""""""""""""""""""""""
    "   View for Peliculas_Directores       "
    """"""""""""""""""""""""""""
    """

    def directores_peliculas_menu(self):
        print("****************************************************")
        print("*     * -- Submenú Peliculas y directores -- *     *")
        print("****************************************************")
        print("1. Agregar pelicula - director")
        print("2. Leer todas las peliculas de todos los directores")
        print("3. Leer pelicula y director por id")
        print("4. Leer pelicula por id de director")
        print("5. Actualizar director - pelicula")
        print("6. Eliminar director-pelicula")
        print("7. Regresar al menú principal")

    def ver_director_pelicula(self,record):
        print('ID_director:',record[0])
        print('ID_Pelicula:',record[5])
        print("Datos del director".center(81,'*'))
        self.ver_director(record[0:5])
        print("Datos de la pelicula".center(81,'*'))
        self.ver_pelicula(record[5:])

    def ver_director_pelicula_header(self, header):
        print(str(header).center(180,'*'))
        print('-'*180)

    def ver_director_pelicula_midder(self):
        print('/'*180)

    def ver_director_pelicula_footer(self):
        print('*'*180)

    """
    """""""""""""""""""""""""""""
    "   View for Peliculas_Genero       "
    """"""""""""""""""""""""""""
    """

    def genero_peliculas_menu(self):
        print("************************************************")
        print("*     * -- Submenú Peliculas y genero -- *     *")
        print("************************************************")
        print("1. Agregar pelicula - genero")
        print("2. Leer todas las peliculas de todos los genero")
        print("3. Leer pelicula y genero por id")
        print("4. Leer pelicula por id de genero")
        print("5. Actualizar genero - pelicula")
        print("6. Eliminar genero-pelicula")
        print("7. Regresar al menú principal")

    def ver_genero_pelicula(self,record):
        print('ID_genero:',record[0])
        print('ID_Pelicula:',record[2])
        print("Datos del genero".center(180,'*'))
        self.ver_genero(record[0:2])
        print("Datos de la pelicula".center(180,'*'))
        self.ver_pelicula(record[2:])

    def ver_genero_pelicula_header(self, header):
        print(str(header).center(48,'*'))
        print('-'*180)

    def ver_genero_pelicula_midder(self):
        print('/'*180)

    def ver_genero_pelicula_footer(self):
        print('*'*180)

