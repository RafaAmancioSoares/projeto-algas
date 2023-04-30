create database algas_transactions;
-- drop database algas_transactions;
use algas_transactions;

create table transaction_with_memory (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    transacao INT,
    tempo_exec varchar(60),
    max_mem float(15),
    min_mem float(15)
);

create table transaction_without_memory (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    transacao INT,
    tempo_exec varchar(60),
    max_mem float(15),
    min_mem float(15)
);

create table passos_adulto_sedentario (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    data varchar(7)
);

create table passos_adulto_pouco_ativo (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    data varchar(7)
);

create table passos_adulto_ativo (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    data varchar(7)
);

create table passos_adulto (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    data varchar(7)
);

create table execucoes_algas (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    data_exec DATETIME,
    tempo_exec varchar(60)
);
-- INSERT INTO 
-- transaction_without_memory(transacao, tempo_exec, max_mem, min_mem)
-- VALUES
-- (10, '111', '222', '333');

SELECT * FROM transaction_without_memory;
SELECT * FROM transaction_with_memory;
SELECT * FROM passos_adulto_sedentario;
SELECT * FROM passos_adulto_pouco_ativo;
SELECT * FROM passos_adulto_ativo;
SELECT * FROM execucoes_algas;