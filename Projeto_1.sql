create database Projeto_1;

use projeto_1;

create table clientes(
id int auto_increment,
nome varchar (40) not null,
sobrenome varchar (40) not null,
cpf varchar (11) unique not null,
telefone varchar (15),
primary key(id)
);

create table animais(
id int auto_increment,
nome varchar(30),
especie varchar(10) not null,
raca varchar(30),
idade varchar(15),
Sexo varchar(10),
primary key(id)
);

INSERT INTO clientes (nome, sobrenome, cpf, telefone) VALUES ("lucas", "minatti", "11575296900", "47997069196");

INSERT INTO animais (nome, especie, raca, idade, sexo) VALUES ("Boreal", "Gato", "Vira-Lata", "4 anos", "macho");

select * from clientes;

select * from animais;

delete from clientes where id = 1;

drop table animais;