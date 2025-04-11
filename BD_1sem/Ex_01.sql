create database escola;
create table curso (
	codCurso char(3) primary key not null,
    nome varchar(30),
    mensalidade decimal(10,2)
);
create table aluno (
	ra char(9) primary key not null,
    rg char(9) not null,
    nome char(30),
    codCurso char(3),
    foreign key (codCurso) references curso(codCurso)
);
create table disciplina (
	codDisc char(5) primary key not null,
    nome char(30),
    codCurso char(3),
    nroCreditos int,
    foreign key(codCurso) references curso(codCurso)
);
create table boletim (
	ra char(9) not null,
    codDisc char(5) not null,
    nota decimal(10,2),
    primary key (ra, codDisc),
    foreign key (ra) references aluno (ra),
    foreign key (codDisc) references disciplina (codDisc)
);
insert into curso values ('AS', 'ANALISE DE SISTEMAS', 1000);
insert into curso values ('CC', 'CIENCIA DA COMPUTACAO', 950);
insert into curso values ('SI', 'SISTEMAS DE INFORMACAO', 800);
insert into aluno values ('123', '12345', 'BIANCA MARIA PEDROSA', 'AS');
insert into aluno values ('212', '21234', 'TATIANE CITTON', 'AS');
insert into aluno values ('221', '22145', 'ALEXANDRE PEDROSA', 'CC');
insert into aluno values ('231', '23144', 'ALEXANDRE MONTEIRO', 'CC');
insert into aluno values ('321', '32111', 'MARCIA RIBEIRO', 'CC');
insert into aluno values ('661', '66123', 'JUSSARA MARANDOLA', 'SI');
insert into aluno values ('765', '76512', 'WALTER RODRIGUES', 'SI');
insert into disciplina values ('BD', 'BANCO DE DADOS', 'CC', 4);
insert into disciplina values ('BDA', 'BANCO DE DADOS AVANCADOS', 'CC', 6);
insert into disciplina values ('BDOO', 'BANCO DE DADOS O OBJETOS', 'SI', 4);
insert into disciplina values ('SBD', 'SISTEMA DE BANCO DE DADOS', 'AS', 4);
insert into disciplina values ('DBD', 'DESENVOLVIMENTO BANCO DE DADOS', 'SI', 6);
insert into disciplina values ('IBD', 'INTRODUCAO A BANCO DE DADOS', 'AS', 2);
insert into boletim values ('123', 'BDS', 10);
insert into boletim values ('212', 'IBD', 7.5);
insert into boletim values ('231', 'BD', 9);
insert into boletim values ('231', 'BDA', 9.6);
insert into boletim values ('661', 'DBD', 8);
insert into boletim values ('765', 'DBD', 6);