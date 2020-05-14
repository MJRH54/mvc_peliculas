from mysql import connector

class Model:
    """
    A data model with MySQL for a MoviesDB
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key,val) = line.strip().split(':')
                d[key] = val
            return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        #**************************************************************#
        #                        * Peliculas Methods *                 #
        #**************************************************************#

    def create_pelicula(self,idpelicula,nombre,sipnosis,flanzamiento):
        try:
            sql = 'INSERT INTO peliculas(`id_pelicula`,`nombre`,`sipnosis`,`fecha_lanzamiento`) VALUES (%s,%s,%s,%s)'
            vals = (idpelicula,nombre,sipnosis,flanzamiento)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_pelicula(self,id_pelicula):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_pelicula(self):
        try:
            sql = 'SELECT * FROM peliculas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_pelicula_nombre(self,nombre):
        try:
            sql = 'SELECT * FROM peliculas WHERE nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_pelicula(self,fields,vals):
        try:
            sql = 'UPDATE peliculas SET '+','.join(fields)+' WHERE id_pelicula = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_pelicula(self,idpelicula):
        try:
            sql = 'DELETE FROM peliculas WHERE id_pelicula = %s'
            vals = (idpelicula,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


        #**************************************************************#
        #                        * Actores Methods *                   #
        #**************************************************************#

    def create_actor(self,idactor,nombre,telefono,correo,direccion):
        try:
            sql = 'INSERT INTO actores(`id_actor`,`nombre`,`telefono`,`correo`,`direccion`) VALUES (%s,%s,%s,%s,%s)'
            vals = (idactor,nombre,telefono,correo,direccion)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_actor_id(self,id_actor):
        try:
            sql = 'SELECT * FROM actores WHERE id_actor = %s'
            vals = (id_actor,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_actores(self):
        try:
            sql = 'SELECT * FROM actores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_actor_nombre(self,nombre):
        try:
            sql = 'SELECT * FROM actores WHERE nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_actor(self,fields,vals):
        try:
            sql = 'UPDATE actores SET '+','.join(fields)+' WHERE id_actor = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_actor(self,idactor):
        try:
            sql = 'DELETE FROM actores WHERE id_actor = %s'
            vals = (idactor,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        * Directores Methods *                   #
        #**************************************************************#

    def create_director(self,iddirector,nombre,telefono,correo,direccion):
        try:
            sql = 'INSERT INTO directores(`id_director`,`nombre`,`telefono`,`correo`,`direccion`) VALUES (%s,%s,%s,%s,%s)'
            vals = (iddirector,nombre,telefono,correo,direccion)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_director_id(self,id_director):
        try:
            sql = 'SELECT * FROM directores WHERE id_director = %s'
            vals = (id_director,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_directores(self):
        try:
            sql = 'SELECT * FROM directores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_director_nombre(self,nombre):
        try:
            sql = 'SELECT * FROM directores WHERE nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_director(self,fields,vals):
        try:
            sql = 'UPDATE directores SET '+','.join(fields)+' WHERE id_director = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_director(self,iddirector):
        try:
            sql = 'DELETE FROM directores WHERE id_director = %s'
            vals = (iddirector,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        * Genero Methods *                   #
        #**************************************************************#

    def create_genero(self,idgenero,genero):
        try:
            sql = 'INSERT INTO genero(`id_genero`,`genero`) VALUES (%s,%s)'
            vals = (idgenero,genero)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_genero(self,id_genero):
        try:
            sql = 'SELECT * FROM genero WHERE id_genero = %s'
            vals = (id_genero,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_genero(self):
        try:
            sql = 'SELECT * FROM genero'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_genero_nombre(self,genero):
        try:
            sql = 'SELECT * FROM genero WHERE genero = %s'
            vals = (genero,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_genero(self,fields,vals):
        try:
            sql = 'UPDATE genero SET '+','.join(fields)+' WHERE id_genero = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_genero(self,idgenero):
        try:
            sql = 'DELETE FROM genero WHERE id_genero = %s'
            vals = (idgenero,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                  * Actores_Peliculas Methods *               #
        #**************************************************************#

    def create_actor_peliculas(self,idactor,idpelicula):
        try:
            sql = 'INSERT INTO actores_pelicula(`id_actor`,`id_pelicula`) VALUES (%s,%s)'
            vals = (idactor,idpelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_actores_peliculas(self,idactor, idpelicula):
        try:
            sql = 'SELECT actores.*, peliculas.* FROM actores_pelicula JOIN peliculas ON peliculas.id_pelicula = actores_pelicula.id_pelicula AND actores_pelicula.id_pelicula = %s JOIN actores ON actores.id_actor = actores_pelicula.id_actor AND actores_pelicula.id_actor = %s' 
            vals = (idpelicula,idactor)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_actores_peliculas(self):
        try:
            sql = 'SELECT peliculas.*, actores.* FROM actores_pelicula JOIN peliculas ON peliculas.id_pelicula = actores_pelicula.id_pelicula JOIN actores ON actores.id_actor = actores_pelicula.id_actor'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_peliculasByActor(self,idactor):
        try:
            sql = 'SELECT actores.*, peliculas.* FROM actores_pelicula JOIN actores ON actores.id_actor = actores_pelicula.id_actor AND actores_pelicula.id_actor = %s JOIN peliculas ON peliculas.id_pelicula = actores_pelicula.id_pelicula'
            vals = (idactor,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_actores_peliculas(self,fields,vals):
        try:
            sql = 'UPDATE actores_pelicula SET '+','.join(fields)+' WHERE id_actor = %s AND id_pelicula = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_actores_peliculas(self,idactor,idpelicula):
        try:
            sql = 'DELETE FROM actores_pelicula WHERE id_actor = %s AND id_pelicula = %s'
            vals = (idactor,idpelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                  * Directores_Peliculas Methods *            #
        #**************************************************************#

    def create_director_peliculas(self,iddirector,idpelicula):
        try:
            sql = 'INSERT INTO directores_pelicula(`id_director`,`id_pelicula`) VALUES (%s,%s)'
            vals = (iddirector,idpelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_directores_peliculas(self,iddirector, idpelicula):
        try:
            sql = 'SELECT  directores.*, peliculas.* FROM directores_pelicula JOIN peliculas ON peliculas.id_pelicula = directores_pelicula.id_pelicula AND directores_pelicula.id_pelicula = %s JOIN directores ON directores.id_director = directores_pelicula.id_director AND directores_pelicula.id_director = %s' 
            vals = (idpelicula,iddirector)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_directores_peliculas(self):
        try:
            sql = 'SELECT peliculas.*, directores.* FROM directores_pelicula JOIN peliculas ON peliculas.id_pelicula = directores_pelicula.id_pelicula JOIN directores ON directores.id_director = directores_pelicula.id_director'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_peliculasByDirector(self,iddirector):
        try:
            sql = 'SELECT directores.*, peliculas.* FROM directores_pelicula JOIN directores ON directores.id_director = directores_pelicula.id_director AND directores_pelicula.id_director = %s JOIN peliculas ON peliculas.id_pelicula = directores_pelicula.id_pelicula'
            vals = (iddirector,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_directores_peliculas(self,fields,vals):
        try:
            sql = 'UPDATE directores_pelicula SET '+','.join(fields)+' WHERE id_director = %s AND id_pelicula = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_directores_peliculas(self,iddirector,idpelicula):
        try:
            sql = 'DELETE FROM directores_pelicula WHERE id_director = %s AND id_pelicula = %s'
            vals = (iddirector,idpelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                   * Generos_Peliculas Methods *              #
        #**************************************************************#

    def create_genero_peliculas(self,idgenero,idpelicula):
        try:
            sql = 'INSERT INTO genero_pelicula(`id_genero`,`id_pelicula`) VALUES (%s,%s)'
            vals = (idgenero,idpelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_genero_peliculas(self,idgenero, idpelicula):
        try:
            sql = 'SELECT  genero.*, peliculas.* FROM genero_pelicula JOIN peliculas ON peliculas.id_pelicula = genero_pelicula.id_pelicula AND genero_pelicula.id_pelicula = %s JOIN genero ON genero.id_genero = genero_pelicula.id_genero AND genero_pelicula.id_genero = %s' 
            vals = (idpelicula,idgenero)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_genero_peliculas(self):
        try:
            sql = 'SELECT genero.*, peliculas.* FROM genero_pelicula JOIN peliculas ON peliculas.id_pelicula = genero_pelicula.id_pelicula JOIN genero ON genero.id_genero = genero_pelicula.id_genero'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_peliculasByGenero(self,idgenero):
        try:
            sql = 'SELECT genero.*, peliculas.* FROM genero_pelicula JOIN genero ON genero.id_genero = genero_pelicula.id_genero AND genero_pelicula.id_genero = %s JOIN peliculas ON peliculas.id_pelicula = genero_pelicula.id_pelicula'
            vals = (idgenero,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_genero_peliculas(self,fields,vals):
        try:
            sql = 'UPDATE idgenero_pelicula SET '+','.join(fields)+' WHERE id_genero = %s AND id_pelicula = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_genero_peliculas(self,idgenero,idpelicula):
        try:
            sql = 'DELETE FROM genero_pelicula WHERE id_genero = %s AND id_pelicula = %s'
            vals = (idgenero,idpelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

