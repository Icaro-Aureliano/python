DROP DATABASE IF EXISTS livraria;
CREATE DATABASE livraria;
USE livraria;


CREATE TABLE  livraria.livros (
  CODLIVRO bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  TITULO varchar(100) NOT NULL,
  AUTOR varchar(50) DEFAULT NULL,
  PRECO decimal(7,2) NOT NULL,
  GENERO varchar(30) DEFAULT NULL,
  PRIMARY KEY (CODLIVRO)
);


DROP TABLE IF EXISTS livraria.clientes;
CREATE TABLE  livraria.clientes (
  CPF varchar(14) NOT NULL,
  NOME varchar(50) NOT NULL,
  ENDERECO varchar(100) DEFAULT NULL,
  CIDADE varchar(30) DEFAULT NULL,
  PRIMARY KEY (CPF)
);


CREATE TABLE  livraria.vendedor (
  CODVENDEDOR bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  NOME varchar(50) DEFAULT NULL,
  CIDADE varchar(50) DEFAULT NULL,
  TELEFONE varchar(15) DEFAULT NULL,
  COMISSAO decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (CODVENDEDOR)
);


CREATE TABLE  livraria.venda (
  CODVENDA bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  CPFCLIENTE varchar(14) DEFAULT NULL,
  CODVENDEDOR bigint(20) unsigned DEFAULT NULL,
  CODLIVRO bigint(20) unsigned DEFAULT NULL,
  DATAVENDA date DEFAULT NULL,
  PRIMARY KEY (CODVENDA),
  KEY FK_CPF_CLIENTE_idx (CPFCLIENTE),
  KEY FK_COD_LIVRO (CODLIVRO),
  KEY FK_COD_VENDEDOR (CODVENDEDOR),
  CONSTRAINT FK_COD_VENDEDOR FOREIGN KEY (CODVENDEDOR) REFERENCES vendedor (CODVENDEDOR),
  CONSTRAINT FK_COD_LIVRO FOREIGN KEY (CODLIVRO) REFERENCES livroS (CODLIVRO),
  CONSTRAINT FK_CPF_CLIENTE FOREIGN KEY (CPFCLIENTE) REFERENCES clientes (CPF) ON DELETE NO ACTION ON UPDATE NO ACTION
);


INSERT INTO clientes (CPF, NOME, ENDERECO, CIDADE) VALUES
('001.001.001-01', 'José',' RUA 1 BAIRRO 1', 'GARÇA'),
('002.001.001-02', 'Livia',' RUA 2 BAIRRO 2', 'MARÍLIA'),
('003.001.001-03', 'Marcos',' RUA 3 BAIRRO 3', 'BAURU'),
('004.001.001-04', 'Áloisio',' RUA 4 BAIRRO 4', 'JAFA');


INSERT INTO livros (TITULO, AUTOR, PRECO, GENERO) VALUES
('VIDAS SECAS','Graciliano Ramos',20.50,'ROMANCE'),
('LINHAS TORTAS','Graciliano Ramos',15.0,'CRÔNICAS'),
('REINAÇÕES DE NARIZINHO','Monteiro Lobato',25.0,'INFANTIL'),
('DOM QUIXOTE','Miguel de Cervantes',23.20,'AVENTURA'),
('O ÚLTIMO REINO','Bernard Cornwell',35.0,'AVENTURA'),
('A AMIGA GENIAL','Elena Ferrante',40.0,'ROMANCE');

INSERT INTO vendedor (NOME, TELEFONE, CIDADE, COMISSAO) VALUES
('DAVI','+5514981710171','GARÇA', 4.0),
('Álvaro','+5514981710172','MARÍLIA', 5.0),
('ANDREA','+5514981710173','GARÇA', 5.0)
;

INSERT INTO venda (CPFCLIENTE, CODVENDEDOR, CODLIVRO, DATAVENDA) VALUES
('001.001.001-01', 1, 1, '2021-08-10'),
('001.001.001-01', 2, 2, '2021-03-01'),
('002.001.001-02', 2, 4, '2021-03-01'),
('002.001.001-02', 1, 6, '2021-03-01'),
('004.001.001-04', 3, 5, '2021-03-01');





