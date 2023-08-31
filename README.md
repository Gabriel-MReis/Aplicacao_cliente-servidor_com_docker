# Aplicação Cliente-Servidor com Docker

Esta é uma aplicação cliente-servidor que utiliza contêineres Docker para isolar o banco de dados e o servidor. A aplicação envia três questões de múltipla escolha para um cliente, recebe as respostas e retorna quantas questões foram respondidas corretamente.

## Pré-requisitos

- Docker instalado: [Docker Install](https://docs.docker.com/get-docker/)
- Ambiente de desenvolvimento Python

## Executando a Aplicação

### Passo 1: Banco de Dados MySQL

1. Execute o contêiner Docker para o banco de dados MySQL:
   
   ```bash
   docker run --name mysql-container --network mynetwork -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=quizdb -d mysql:latest

### Passo 2: Servidor

1. Construa a imagem Docker para o servidor:

```bash
docker build -t server-app -f Dockerfile.server .
docker run --network mynetwork -p 12345:12345 -it server-app
```

## Funcionamento da Aplicação

1. O servidor estará ouvindo na porta 12345.

2. O cliente se conecta ao servidor e recebe as questões.

3. O cliente responde às questões e envia as respostas de volta para o servidor.

4. O servidor processa as respostas e envia a pontuação de volta ao cliente.

## Observações

- Certifique-se de que os contêineres do banco de dados, servidor e cliente estejam na mesma rede Docker (`mynetwork`) para a comunicação correta.

- Certifique-se de que o código do cliente e do servidor esteja corretamente configurado para se conectar aos contêineres corretos.

---

## Autores

- Gabriel Magalhães Reis

---

## Referências

- [Docker Documentation](https://docs.docker.com/)
- [Python Socket Programming](https://docs.python.org/3/library/socket.html)
- [MySQL Docker Hub](https://hub.docker.com/_/mysql)