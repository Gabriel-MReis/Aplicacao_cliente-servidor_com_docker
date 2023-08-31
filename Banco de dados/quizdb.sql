DROP SCHEMA IF EXISTS `quizdb`;
CREATE DATABASE IF NOT EXISTS quizdb;
USE quizdb;

CREATE TABLE questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT,
    options JSON,
    answer INT
);

INSERT INTO questions (question, options, answer)
VALUES ('Qual é a capital da Itália?', '{"1":"Roma", "2":"Paris", "3":"Lisboa", "4":"Londres"}', 0);

INSERT INTO questions (question, options, answer)
VALUES ('Qual é o maior planeta do sistema solar?', '{"1":"Marte", "2":"Vênus", "3":"Júpiter", "4":"Saturno"}', 2);

INSERT INTO questions (question, options, answer)
VALUES ('Quem pintou a Mona Lisa?', '{"1":"Vincent van Gogh", "2":"Leonardo da Vinci", "3":"Pablo Picasso", "4":"Michelangelo"}', 1);