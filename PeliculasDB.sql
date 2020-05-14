#Creacion de la base de datos.

CREATE DATABASE IF NOT EXISTS MoviesDB;

USE MoviesDB;

#Crecion de las tablas y sus respectivas relaciones

CREATE TABLE IF NOT EXISTS peliculas(
	
    id_pelicula int not null auto_increment,
    nombre varchar(50) not null,
    sipnosis varchar(255) not null,
    fecha_lanzamiento date,
    
    primary key (id_pelicula)

)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS actores(
	
    id_actor int not null auto_increment,
    nombre varchar(50) not null,
    telefono varchar(20) not null,
    correo varchar(255),
    direccion varchar(50),
    
    primary key (id_actor)

)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS directores(
	
    id_director int not null auto_increment,
    nombre varchar(50) not null,
    telefono varchar(20) not null,
    correo varchar(255),
    direccion varchar(50),
    
    primary key (id_director)

)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS genero(
	
    id_genero int not null auto_increment,
    genero varchar(50) not null,
    
    primary key (id_genero)

)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS genero_pelicula(
	
    id_genero int not null,
    id_pelicula int not null,
	primary key(id_genero, id_pelicula),
    constraint fkidgenero foreign key(id_genero)
    references genero(id_genero)
    on delete cascade
    on update cascade,
    
    constraint fkidpelicula_genero foreign key(id_pelicula)
    references peliculas(id_pelicula)
    on delete cascade
    on update cascade
    
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS actores_pelicula(
	
    id_actor int not null,
    id_pelicula int not null,
    
    primary key(id_actor, id_pelicula),
    constraint fkidacor foreign key(id_actor)
    references actores(id_actor)
    on delete cascade
    on update cascade,
    
    constraint fkidpelicula_actor foreign key(id_pelicula)
    references peliculas(id_pelicula)
    on delete cascade
    on update cascade
    

)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS directores_pelicula(
	
    id_director int not null,
    id_pelicula int not null,
    
    primary key(id_director, id_pelicula),
    constraint fkiddirector foreign key(id_director)
    references directores(id_director)
    on delete cascade
    on update cascade,
    
    constraint fkidpelicula_director foreign key(id_pelicula)
    references peliculas(id_pelicula)
    on delete cascade
    on update cascade
    

)ENGINE = INNODB;


insert into actores(nombre,telefono,correo,direccion) values ('Marco Rodriguez', '1234444214', 'm.rodriguez@123.com', 'Centro #34, Irapuato, Gto'),('Josefina Hernandez', '7727272991', 'jose@gmail.com','Las rosas #233, Irapuato, Gto'),('Antonio Yosafat', '992883832', 'Yosafat123@gmail.com','Rey Bravo, #45, Leon, Gto');
insert into peliculas(nombre,sipnosis,fecha_lanzamiento) values ('Avengers 1', 'Pelicula de superheroes de MARVEL\n mucha acción y diversión','2014-04-18'),('El mundo oscuro de Peter', 'Pelicula de suspenso en el cual no despegaras tus ojos de la pantalla porque si lo haces lo mas seguro es\n que no estes vivo para contarlo','2002-12-2');
insert into actores_pelicula(id_actor,id_pelicula) values (2,1)
insert into directores(nombre,telefono,correo,direccion) values ('Juan Rodriguez', '199381332', 'j.rodriguez@123.com', 'Valle del Sol #34, Irapuato, Gto'),('Jonathan Perez', '883748211', 'eaae@gmail.com','AA Avenue #233, Los Angeles, California'),('Carlos Lopez', '1177266111', 'lopezcarlos@gmail.com','4th Avenue Bravo, #45, Chicago, Chicago');
insert into directores_pelicula(id_director,id_pelicula) values (5,2),(5,1),(6,2),(7,2),(6,1)
insert into genero(genero) values ('Accion'),('Comedia'),('Suspenso'),('Terror'),('Romance')
insert into genero_pelicula(id_genero,id_pelicula) values (1,1),(2,1),(3,1),(4,2),(3,2)