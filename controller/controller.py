from model.model import Model
from view.view import View
from datetime import date

class Controller:
    
    """
    """""""""""""""""""""""""""""
    "   A Controller for a MoviesDB  "
    """"""""""""""""""""""""""""
    """

    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()


    """
    """""""""""""""""""""""""""""
    "   General controller      "
    """"""""""""""""""""""""""""
    """

    def main_menu(self):
        o  = '0'
        while(o != '8'):
            self.view.main_menu()
            self.view.option('8')
            o = input()
            if (o == '1'):
                self.peliculas_menu()
            elif(o == '2'):
                self.actores_menu()
            elif(o == '3'):
                self.directores_menu()
            elif(o == '4'):
                self.genero_menu()
            elif(o == '5'):
                self.actores_peliculas_menu()
            elif(o == '6'):
                self.directores_peliculas_menu()
            elif(o == '7'):
                self.genero_peliculas_menu()
            elif(o == '8'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self,fs,vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if(v!= ''):
                fields.append(f + ' = %s')
                vals.append(v)
        return fields, vals

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #"""
    #"""""""""""""""""""""""""""""
    #"  Controller  Peliculas    "
    #""""""""""""""""""""""""""""
    #"""


    def peliculas_menu(self):
        o = '0'
        while(o != '7'):
            self.view.peliculas_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_pelicula()
            elif(o == '2'):
                self.read_all_peliculas()
            elif(o == '3'):
                self.read_peliculas_id()
            elif(o == '4'):
                self.read_peliculas_nombre()
            elif(o == '5'):
                self.update_peliculas()
            elif(o == '6'):
                self.remove_peliculas()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_pelicula(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Sipnosis: ')
        Sipnosis = input()
        self.view.ask('Fecha Lanzamiento (AAAA-MM-DD): ')
        Lanzamiento =  input()
        return [Nombre,Sipnosis,Lanzamiento]

    def create_pelicula(self):
        self.view.ask('ID: ')
        i_pelicula = input()
        Nombre,Sipnosis,Lanzamiento = self.ask_pelicula()
        out = self.model.create_pelicula(i_pelicula,Nombre,Sipnosis,Lanzamiento)
        if(out == True):
            self.view.ok(i_pelicula, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('Ya existe este ID en las peliculas')
            else:
                self.view.error('NO SE PUDO AGREGAR ESTE ID. REVISA OTRA VEZ')
        return

    def read_all_peliculas(self):
        peliculas = self.model.read_all_pelicula()
        if(type(peliculas) == list):
            self.view.ver_pelicula_header('LISTADO DE PELICULAS')
            for peli in peliculas:
                self.view.ver_pelicula(peli)
            self.view.ver_pelicula_midder()
            self.view.ver_pelicula_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODAS LAS PELICULAS.')
        return
    
    def read_peliculas_id(self):
        self.view.ask('ID A BUSCAR: ')
        i_pelicula = input()
        pelicula = self.model.read_pelicula(i_pelicula)
        if( type(pelicula) == tuple):
            self.view.ver_pelicula_header('Datos de la pelicula ' + i_pelicula + ' ' )
            self.view.ver_pelicula(pelicula)
            self.view.ver_pelicula_midder()
            self.view.ver_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('ERROR EL RECUPERAR LA PELICULA. ¡Revisa!')
        return

    def read_peliculas_nombre(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        peliculas = self.model.read_pelicula_nombre(Nombre)
        if(type(peliculas) == list):
            self.view.ver_pelicula_header('LISTADO DE PELICULAS')
            for peli in peliculas:
                self.view.ver_pelicula(peli)
            self.view.ver_pelicula_midder()
            self.view.ver_pelicula_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODAS LAS PELICULAS.')
        return

    def update_peliculas(self):
        self.view.ask('ID MODIFICAR: ')
        i_pelicula = input()
        pelicula = self.model.read_pelicula(i_pelicula)
        if(type(pelicula) == tuple):
            self.view.ver_pelicula_header('Datos de la Pelicula ' + i_pelicula)
            self.view.ver_pelicula(pelicula)
            self.view.ver_pelicula_midder()
            self.view.ver_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DE LA PELICULA. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_pelicula()
        fields, vals = self.update_lists(['nombre','sipnosis','fecha_lanzamiento'], whole_vals)
        vals.append(i_pelicula)
        vals = tuple(vals)
        out = self.model.update_pelicula(fields,vals)
        if(out == True):
            self.view.ok(i_pelicula,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA. REVISA')

    def remove_peliculas(self):
        self.view.ask('ID a eliminar: ')
        i_pelicula = input()
        count = self.model.delete_pelicula(i_pelicula)
        if count != 0:
            self.view.ok(i_pelicula,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR LA PELICULA. REVISA")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #""""""""""""""""""""""""""""""
    #"  Controller  Actores    "
    #""""""""""""""""""""""""""""""

    def actores_menu(self):
        o = '0'
        while(o != '7'):
            self.view.actores_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_actor()
            elif(o == '2'):
                self.read_all_actores()
            elif(o == '3'):
                self.read_actores_id()
            elif(o == '4'):
                self.read_actores_nombre()
            elif(o == '5'):
                self.update_actores()
            elif(o == '6'):
                self.remove_actores()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_actor(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Telefono: ')
        Telefono = input()
        self.view.ask('Correo: ')
        Correo =  input()
        self.view.ask('Direccion: ')
        Direccion =  input()
        return [Nombre,Telefono,Correo,Direccion]

    def create_actor(self):
        self.view.ask('ID: ')
        i_actor = input()
        Nombre,Telefono,Correo,Direccion = self.ask_actor()
        out = self.model.create_actor(i_actor,Nombre,Telefono,Correo,Direccion)
        if(out == True):
            self.view.ok(i_actor, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('Ya existe este ID en los actores')
            else:
                self.view.error('NO SE PUDO AGREGAR ESTE ID. REVISA OTRA VEZ')
        return

    def read_all_actores(self):
        actores = self.model.read_all_actores()
        if(type(actores) == list):
            self.view.ver_actor_header('LISTADO DE ACTORES')
            for actor in actores:
                self.view.ver_actor(actor)
            self.view.ver_actor_midder()
            self.view.ver_actor_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODAS LOS ACTORES.')
        return
    
    def read_actores_id(self):
        self.view.ask('ID A BUSCAR: ')
        i_actor = input()
        actor = self.model.read_actor_id(i_actor)
        if( type(actor) == tuple):
            self.view.ver_actor_header('Datos de la actor ' + i_actor + ' ' )
            self.view.ver_actor(actor)
            self.view.ver_actor_midder()
            self.view.ver_actor_footer()
        else:
            if actor == None:
                self.view.error('EL ACTOR NO EXISTE')
            else:
                self.view.error('ERROR AL RECUPERAR EL ACTOR. ¡Revisa!')
        return

    def read_actores_nombre(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        actores = self.model.read_actor_nombre(Nombre)
        if(type(actores) == list):
            self.view.ver_actor_header('LISTADO DE ACTORES')
            for actor in actores:
                self.view.ver_actor(actor)
            self.view.ver_actor_midder()
            self.view.ver_actor_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS ACTORES.')
        return

    def update_actores(self):
        self.view.ask('ID MODIFICAR: ')
        i_actor = input()
        actor = self.model.read_actor_id(i_actor)
        if(type(actor) == tuple):
            self.view.ver_actor_header('Datos de la actor ' + i_actor)
            self.view.ver_actor(actor)
            self.view.ver_actor_midder()
            self.view.ver_actor_footer()
        else:
            if actor == None:
                self.view.error('EL ACTOR NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL ACTOR. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_actor()
        fields, vals = self.update_lists(['nombre','telefono','correo','direccion'], whole_vals)
        vals.append(i_actor)
        vals = tuple(vals)
        out = self.model.update_actor(fields,vals)
        if(out == True):
            self.view.ok(i_actor,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ACTOR. REVISA')

    def remove_actores(self):
        self.view.ask('ID a eliminar: ')
        i_actor = input()
        count = self.model.delete_actor(i_actor)
        if count != 0:
            self.view.ok(i_actor,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL ACTOR. REVISA")
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
    #""""""""""""""""""""""""""""""
    #"  Controller  Directores    "
    #""""""""""""""""""""""""""""""

    def directores_menu(self):
        o = '0'
        while(o != '7'):
            self.view.directores_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_director()
            elif(o == '2'):
                self.read_all_directores()
            elif(o == '3'):
                self.read_directores_id()
            elif(o == '4'):
                self.read_directores_nombre()
            elif(o == '5'):
                self.update_directores()
            elif(o == '6'):
                self.remove_directores()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_director(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Telefono: ')
        Telefono = input()
        self.view.ask('Correo: ')
        Correo =  input()
        self.view.ask('Direccion: ')
        Direccion =  input()
        return [Nombre,Telefono,Correo,Direccion]

    def create_director(self):
        self.view.ask('ID: ')
        i_director = input()
        Nombre,Telefono,Correo,Direccion = self.ask_director()
        out = self.model.create_director(i_director,Nombre,Telefono,Correo,Direccion)
        if(out == True):
            self.view.ok(i_director, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('Ya existe este ID en los directores')
            else:
                self.view.error('NO SE PUDO AGREGAR ESTE ID. REVISA OTRA VEZ')
        return

    def read_all_directores(self):
        directores = self.model.read_all_directores()
        if(type(directores) == list):
            self.view.ver_director_header('LISTADO DE DIRECTORES')
            for director in directores:
                self.view.ver_director(director)
            self.view.ver_director_midder()
            self.view.ver_director_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODAS LOS DIRECTORES.')
        return
    
    def read_directores_id(self):
        self.view.ask('ID A BUSCAR: ')
        i_director = input()
        director = self.model.read_director_id(i_director)
        if( type(director) == tuple):
            self.view.ver_director_header('Datos de la director ' + i_director + ' ' )
            self.view.ver_director(director)
            self.view.ver_director_midder()
            self.view.ver_director_footer()
        else:
            if director == None:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('ERROR AL RECUPERAR EL DIRECTOR. ¡Revisa!')
        return

    def read_directores_nombre(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        directores = self.model.read_director_nombre(Nombre)
        if(type(directores) == list):
            self.view.ver_director_header('LISTADO DE DIRECTORES')
            for director in directores:
                self.view.ver_director(director)
            self.view.ver_director_midder()
            self.view.ver_director_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS DIRECTORES.')
        return

    def update_directores(self):
        self.view.ask('ID MODIFICAR: ')
        i_director = input()
        director = self.model.read_director_id(i_director)
        if(type(director) == tuple):
            self.view.ver_director_header('Datos de la director ' + i_director)
            self.view.ver_director(director)
            self.view.ver_director_midder()
            self.view.ver_director_footer()
        else:
            if director == None:
                self.view.error('EL DIRECTOR NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL DIRECTOR. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_director()
        fields, vals = self.update_lists(['nombre','telefono','correo','direccion'], whole_vals)
        vals.append(i_director)
        vals = tuple(vals)
        out = self.model.update_director(fields,vals)
        if(out == True):
            self.view.ok(i_director,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL DIRECTOR. REVISA')

    def remove_directores(self):
        self.view.ask('ID a eliminar: ')
        i_director = input()
        count = self.model.delete_director(i_director)
        if count != 0:
            self.view.ok(i_director,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL DIRECTOR. REVISA")
    
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #""""""""""""""""""""""""""""""
    #"  Controller  Generos    "
    #""""""""""""""""""""""""""""""

    def genero_menu(self):
        o = '0'
        while(o != '7'):
            self.view.genero_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_genero()
            elif(o == '2'):
                self.read_all_generos()
            elif(o == '3'):
                self.read_genero_id()
            elif(o == '4'):
                self.read_genero_nombre()
            elif(o == '5'):
                self.update_genero()
            elif(o == '6'):
                self.remove_genero()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_genero(self):
        self.view.ask('Genero: ')
        Genero = input()
        return [Genero]

    def create_genero(self):
        self.view.ask('ID: ')
        i_genero = input()
        Genero = self.ask_genero()
        out = self.model.create_genero(i_genero,Genero)
        if(out == True):
            self.view.ok(i_genero, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('Ya existe este ID en los generos')
            else:
                self.view.error('NO SE PUDO AGREGAR ESTE ID. REVISA OTRA VEZ')
        return

    def read_all_generos(self):
        generos = self.model.read_all_genero()
        if(type(generos) == list):
            self.view.ver_genero_header('LISTADO DE GENEROS')
            for genero in generos:
                self.view.ver_genero(genero)
            self.view.ver_genero_midder()
            self.view.ver_genero_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODAS LOS GENEROS.')
        return
    
    def read_genero_id(self):
        self.view.ask('ID A BUSCAR: ')
        i_genero = input()
        genero = self.model.read_genero(i_genero)
        if( type(genero) == tuple):
            self.view.ver_genero_header('Datos del genero ' + i_genero + ' ' )
            self.view.ver_genero(genero)
            self.view.ver_genero_midder()
            self.view.ver_genero_footer()
        else:
            if genero == None:
                self.view.error('EL GENERO NO EXISTE')
            else:
                self.view.error('ERROR AL RECUPERAR EL GENERO. ¡Revisa!')
        return

    def read_genero_nombre(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        generos = self.model.read_genero_nombre(Nombre)
        if(type(generos) == list):
            self.view.ver_genero_header('LISTADO DE GENEROS')
            for genero in generos:
                self.view.ver_genero(genero)
            self.view.ver_genero_midder()
            self.view.ver_genero_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS GENEROS.')
        return

    def update_genero(self):
        self.view.ask('ID MODIFICAR: ')
        i_genero = input()
        genero = self.model.read_genero(i_genero)
        if(type(genero) == tuple):
            self.view.ver_genero_header('Datos del genero ' + i_genero)
            self.view.ver_genero(genero)
            self.view.ver_genero_midder()
            self.view.ver_genero_footer()
        else:
            if genero == None:
                self.view.error('EL GENERO NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL DIRECTOR. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_genero()
        fields, vals = self.update_lists(['genero'], whole_vals)
        vals.append(i_genero)
        vals = tuple(vals)
        out = self.model.update_genero(fields,vals)
        if(out == True):
            self.view.ok(i_genero,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL GENERO. REVISA')

    def remove_genero(self):
        self.view.ask('ID a eliminar: ')
        i_genero = input()
        count = self.model.delete_genero(i_genero)
        if count != 0:
            self.view.ok(i_genero,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL GENERO. REVISA")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #"""""""""""""""""""""""""""""""""""""
    #"  Controller  Peliculas_Actores    "
    #"""""""""""""""""""""""""""""""""""""

    def actores_peliculas_menu(self):
        o = '0'
        while(o != '7'):
            self.view.actores_peliculas_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_actores_peliculas()
            elif(o == '2'):
                self.read_all_actores_peliculas()
            elif(o == '3'):
                self.read_actores_peliculas_id()
            elif(o == '4'):
                self.read_pelicula_byActor()
            elif(o == '5'):
                self.update_actores_peliculas()
            elif(o == '6'):
                self.remove_actores_peliculas()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_actores_peliculas(self):
        self.view.ask('ID_ACTOR: ')
        id_actor = input()
        self.view.ask('ID_PELICULA: ')
        id_pelicula = input()
        return [id_actor,id_pelicula]

    def create_actores_peliculas(self):
        id_actor, id_pelicula = self.ask_actores_peliculas()
        out = self.model.create_actor_peliculas(id_actor,id_pelicula)
        if(out == True):
            self.view.ok_double_id(id_actor, id_pelicula, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('Ya existe la combinacion' + id_actor + '-' + id_pelicula + ' en la base de datos.')
            else:
                self.view.error('NO SE PUEDEN AGREGAR ESTOS ID. REVISA OTRA VEZ')
        return

    def read_all_actores_peliculas(self):
        act_peli = self.model.read_all_actores_peliculas()
        if(type(act_peli) == list):
            self.view.ver_actor_pelicula_header('LISTADO DE ACTORES - PELICULAS')
            for ac_pe in act_peli:
                self.view.ver_actor_pelicula_header(ac_pe)
            self.view.ver_actor_pelicula_midder()
            self.view.ver_actor_pelicula_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER LOS ACTORES Y PELICULAS.')
        return
    
    def read_actores_peliculas_id(self):
        id_actor, id_pelicula = self.ask_actores_peliculas()
        act_peli = self.model.read_actores_peliculas(id_actor,id_pelicula)
        if( type(act_peli) == tuple):
            self.view.ver_actor_pelicula_header('Datos del actor ' + id_actor + ' y pelicula ' + id_pelicula + ' ' )
            self.view.ver_actor_pelicula(act_peli)
            self.view.ver_actor_pelicula_midder()
            self.view.ver_actor_pelicula_footer()
        else:
            if act_peli == None:
                self.view.error('LA COMBINACION NO EXISTE')
            else:
                self.view.error('ERROR AL RECUPERAR LOS DATOS ACTORES - PELICULAS. ¡Revisa!')
        return

    def read_pelicula_byActor(self):
        self.view.ask('ID_ACTOR: ')
        id_actor = input()
        act_peli = self.model.read_peliculasByActor(id_actor)
        if(type(act_peli) == list):
            self.view.ver_actor_pelicula_header('LISTADO DE PELICULAS POR EL ACTOR: ' + id_actor)
            for pelicula in act_peli:
                self.view.ver_actor_pelicula(pelicula)
            self.view.ver_actor_pelicula_midder()
            self.view.ver_actor_pelicula_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS REGISTROS.')
        return

    def update_actores_peliculas(self):
        id_actor, id_pelicula = self.ask_actores_peliculas()
        act_peli = self.model.read_actores_peliculas(id_actor,id_pelicula)
        if(type(act_peli) == tuple):
            self.view.ver_actor_pelicula_header('DATOS DEL ACTOR ' + id_actor + ' Y PELICULA ' + id_pelicula)
            self.view.ver_actor_pelicula(act_peli)
            self.view.ver_actor_pelicula_midder()
            self.view.ver_actor_pelicula_footer()
        else:
            if act_peli == None:
                self.view.error('LA COMBINACION NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS REGISTROS. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_actores_peliculas()
        fields, vals = self.update_lists(['id_actor','id_pelicula'], whole_vals)
        vals.append(id_actor)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_actores_peliculas(fields,vals)
        if(out == True):
            self.view.ok_double_id(id_actor,id_pelicula,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL REGISTRO ¡REVISA!')

    def remove_actores_peliculas(self):
        id_actor, id_pelicula = self.ask_actores_peliculas()
        count = self.model.delete_actores_peliculas(id_actor,id_pelicula)
        if count != 0:
            self.view.ok_double_id(id_actor,id_pelicula,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL GENERO. REVISA")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #""""""""""""""""""""""""""""""""""""""""
    #"  Controller  Peliculas_Directores    "
    #""""""""""""""""""""""""""""""""""""""""

    def directores_peliculas_menu(self):
        o = '0'
        while(o != '7'):
            self.view.directores_peliculas_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_directores_peliculas()
            elif(o == '2'):
                self.read_all_directores_peliculas()
            elif(o == '3'):
                self.read_directores_peliculas_id()
            elif(o == '4'):
                self.read_pelicula_byDirector()
            elif(o == '5'):
                self.update_directores_peliculas()
            elif(o == '6'):
                self.remove_directores_peliculas()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_directores_peliculas(self):
        self.view.ask('ID_DIRECTOR: ')
        id_director = input()
        self.view.ask('ID_PELICULA: ')
        id_pelicula = input()
        return [id_director,id_pelicula]

    def create_directores_peliculas(self):
        id_director, id_pelicula = self.ask_directores_peliculas()
        out = self.model.create_director_peliculas(id_director,id_pelicula)
        if(out == True):
            self.view.ok_double_id(id_director, id_pelicula, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('Ya existe la combinacion' + id_director + '-' + id_pelicula + ' en la base de datos.')
            else:
                self.view.error('NO SE PUEDEN AGREGAR ESTOS ID. REVISA OTRA VEZ')
        return

    def read_all_directores_peliculas(self):
        dict_peli = self.model.read_all_directores_peliculas()
        if(type(dict_peli) == list):
            self.view.ver_director_pelicula_header('LISTADO DE DIRECTORES - PELICULAS')
            for dc_pe in dict_peli:
                self.view.ver_director_pelicula_header(dc_pe)
            self.view.ver_director_pelicula_midder()
            self.view.ver_director_pelicula_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER LOS DIRECTORES Y PELICULAS.')
        return
    
    def read_directores_peliculas_id(self):
        id_director, id_pelicula = self.ask_directores_peliculas()
        dict_peli = self.model.read_directores_peliculas(id_director,id_pelicula)
        if( type(dict_peli) == tuple):
            self.view.ver_director_pelicula_header('Datos del director ' + id_director + ' y pelicula ' + id_pelicula + ' ' )
            self.view.ver_director_pelicula(dict_peli)
            self.view.ver_director_pelicula_midder()
            self.view.ver_director_pelicula_footer()
        else:
            if dict_peli == None:
                self.view.error('LA COMBINACION NO EXISTE')
            else:
                self.view.error('ERROR AL RECUPERAR LOS DATOS DIRECTORES - PELICULAS. ¡Revisa!')
        return

    def read_pelicula_byDirector(self):
        self.view.ask('ID_DIRECTOR: ')
        id_director = input()
        dict_peli = self.model.read_peliculasByDirector(id_director)
        if(type(dict_peli) == list):
            self.view.ver_director_pelicula_header('LISTADO DE PELICULAS POR EL DIRECTOR: ' + id_director)
            for pelicula in dict_peli:
                self.view.ver_director_pelicula(pelicula)
            self.view.ver_director_pelicula_midder()
            self.view.ver_director_pelicula_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS REGISTROS.')
        return

    def update_directores_peliculas(self):
        id_director, id_pelicula = self.ask_directores_peliculas()
        dict_peli = self.model.read_directores_peliculas(id_director,id_pelicula)
        if(type(dict_peli) == tuple):
            self.view.ver_director_pelicula_header('DATOS DEL DIRECTOR ' + id_director + ' Y PELICULA ' + id_pelicula)
            self.view.ver_director_pelicula(dict_peli)
            self.view.ver_director_pelicula_midder()
            self.view.ver_director_pelicula_footer()
        else:
            if dict_peli == None:
                self.view.error('LA COMBINACION NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS REGISTROS. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_directores_peliculas()
        fields, vals = self.update_lists(['id_director','id_pelicula'], whole_vals)
        vals.append(id_director)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_directores_peliculas(fields,vals)
        if(out == True):
            self.view.ok_double_id(id_director,id_pelicula,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL REGISTRO ¡REVISA!')

    def remove_directores_peliculas(self):
        id_director, id_pelicula = self.ask_directores_peliculas()
        count = self.model.delete_directores_peliculas(id_director,id_pelicula)
        if count != 0:
            self.view.ok_double_id(id_director,id_pelicula,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL GENERO. REVISA")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #""""""""""""""""""""""""""""""""""""""""
    #"  Controller  Peliculas_Generos       "
    #""""""""""""""""""""""""""""""""""""""""

    def genero_peliculas_menu(self):
        o = '0'
        while(o != '7'):
            self.view.genero_peliculas_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_genero_peliculas()
            elif(o == '2'):
                self.read_all_genero_peliculas()
            elif(o == '3'):
                self.read_genero_peliculas_id()
            elif(o == '4'):
                self.read_pelicula_byGenero()
            elif(o == '5'):
                self.update_genero_peliculas()
            elif(o == '6'):
                self.remove_genero_peliculas()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_genero_peliculas(self):
        self.view.ask('ID_GENERO: ')
        id_genero = input()
        self.view.ask('ID_PELICULA: ')
        id_pelicula = input()
        return [id_genero,id_pelicula]

    def create_genero_peliculas(self):
        id_genero, id_pelicula = self.ask_genero_peliculas()
        out = self.model.create_genero_peliculas(id_genero,id_pelicula)
        if(out == True):
            self.view.ok_double_id(id_genero, id_pelicula, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('Ya existe la combinacion' + id_genero + '-' + id_pelicula + ' en la base de datos.')
            else:
                self.view.error('NO SE PUEDEN AGREGAR ESTOS ID. REVISA OTRA VEZ')
        return

    def read_all_genero_peliculas(self):
        gen_peli = self.model.read_all_genero_peliculas()
        if(type(gen_peli) == list):
            self.view.ver_genero_pelicula_header('LISTADO DE GENEROS - PELICULAS')
            for gen_pe in gen_peli:
                self.view.ver_genero_pelicula_header(gen_pe)
            self.view.ver_genero_pelicula_midder()
            self.view.ver_genero_pelicula_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER LOS GENEROS Y PELICULAS.')
        return
    
    def read_genero_peliculas_id(self):
        id_genero, id_pelicula = self.ask_genero_peliculas()
        gen_peli = self.model.read_genero_peliculas(id_genero,id_pelicula)
        if( type(gen_peli) == tuple):
            self.view.ver_genero_pelicula_header('Datos del genero ' + id_genero + ' y pelicula ' + id_pelicula + ' ' )
            self.view.ver_genero_pelicula(gen_peli)
            self.view.ver_genero_pelicula_midder()
            self.view.ver_genero_pelicula_footer()
        else:
            if gen_peli == None:
                self.view.error('LA COMBINACION NO EXISTE')
            else:
                self.view.error('ERROR AL RECUPERAR LOS DATOS GENEROS - PELICULAS. ¡Revisa!')
        return

    def read_pelicula_byGenero(self):
        self.view.ask('ID_GENERO: ')
        id_genero = input()
        gen_peli = self.model.read_peliculasByGenero(id_genero)
        if(type(gen_peli) == list):
            self.view.ver_genero_pelicula_header('LISTADO DE PELICULAS POR EL GENERO: ' + id_genero)
            for pelicula in gen_peli:
                self.view.ver_genero_pelicula(pelicula)
            self.view.ver_genero_pelicula_midder()
            self.view.ver_genero_pelicula_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS REGISTROS.')
        return

    def update_genero_peliculas(self):
        id_genero, id_pelicula = self.ask_genero_peliculas()
        gen_peli = self.model.read_genero_peliculas(id_genero,id_pelicula)
        if(type(gen_peli) == tuple):
            self.view.ver_genero_pelicula_header('DATOS DEL GENERO ' + id_genero + ' Y PELICULA ' + id_pelicula)
            self.view.ver_genero_pelicula(gen_peli)
            self.view.ver_genero_pelicula_midder()
            self.view.ver_genero_pelicula_footer()
        else:
            if gen_peli == None:
                self.view.error('LA COMBINACION NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS REGISTROS. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_genero_peliculas()
        fields, vals = self.update_lists(['id_genero','id_pelicula'], whole_vals)
        vals.append(id_genero)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_genero_peliculas(fields,vals)
        if(out == True):
            self.view.ok_double_id(id_genero,id_pelicula,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL REGISTRO ¡REVISA!')

    def remove_genero_peliculas(self):
        id_genero, id_pelicula = self.ask_genero_peliculas()
        count = self.model.delete_genero_peliculas(id_genero,id_pelicula)
        if count != 0:
            self.view.ok_double_id(id_genero,id_pelicula,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL GENERO. REVISA")