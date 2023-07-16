CREATE DATABASE horas_complementares;

USE horas_complementares;

CREATE TABLE Alunos (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  Nome VARCHAR(255),
  Email VARCHAR(255),
  Senha VARCHAR(255)
  -- Adicione outros campos relevantes
);

CREATE TABLE Modalidades (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  Nome VARCHAR(255)
);

CREATE TABLE Categorias (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  Nome VARCHAR(255),
  Modalidade_ID INT,
  Limite_Horas INT,
  FOREIGN KEY (Modalidade_ID) REFERENCES Modalidades(ID)
);

CREATE TABLE Certificados (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  Aluno_ID INT,
  Titulo VARCHAR(255),
  Data DATE,
  Modalidade_ID INT,
  Categoria_ID INT,
  Horas INT,
  FOREIGN KEY (Aluno_ID) REFERENCES Alunos(ID),
  FOREIGN KEY (Modalidade_ID) REFERENCES Modalidades(ID),
  FOREIGN KEY (Categoria_ID) REFERENCES Categorias(ID)
);

-- Inserindo dados na tabela "Modalidades"
INSERT INTO Modalidades (Nome) VALUES
('PESQUISA'),
('EXTENSÃO'),
('PROFISSIONAL'),
('OUTRAS');

-- Inserindo dados na tabela "Categorias"
-- Modalidade: PESQUISA
INSERT INTO Categorias (Nome, Modalidade_ID, Limite_Horas) VALUES
('Palestrante em Eventos', 1, 10),
('Ministrar Oficinas', 1, 10),
('Participação em Eventos', 1, 10),
('Membro de Equipe Organizadora', 1, 10);

-- Modalidade: EXTENSÃO
INSERT INTO Categorias (Nome, Modalidade_ID, Limite_Horas) VALUES
('Projetos de Extensão', 2, 40);

-- Modalidade: PROFISSIONAL
INSERT INTO Categorias (Nome, Modalidade_ID, Limite_Horas) VALUES
('Cursos de Formação Profissional', 3, 10),
('Cursos de Línguas', 3, 20),
('Estágio Não Obrigatório', 3, 30);

-- Modalidade: OUTRAS
INSERT INTO Categorias (Nome, Modalidade_ID, Limite_Horas) VALUES
('Eventos na Instituição', 4, 10),
('Participação em Defesas', 4, 4);
