import json
import socket
import mysql.connector

def load_questions():
    connection = mysql.connector.connect(
        host='mysql-container',
        user='root',
        password='root',
        database='quizdb'
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    cursor.close()
    connection.close()

    return questions

def handle_client(client_socket, questions):
    correct_answers = []
    correct = 0
    for idx, question in enumerate(questions):
        question_text = question['question']
        optionsjs = question['options']
        answer = question['answer']

        options = json.loads(optionsjs)

        client_socket.send(f"Questão {idx + 1}: {question_text}\n".encode())
        
        for i, option in sorted(options.items()):
            client_socket.send(f"{i}. {option}\n".encode())
            if (int(i)-1) == answer:
                correct_answers.append(option)

        client_socket.send("Sua resposta: ".encode())
        user_answer = int(client_socket.recv(1024).decode()) - 1

        if user_answer == answer:
            correct += 1

    client_socket.send(f"\nVocê acertou {correct} questões de {len(questions)}.\n".encode())
    client_socket.send("Respostas esperadas:\n".encode())
    for idx in range(0,len(correct_answers)):
        client_socket.send(f"Questão {idx + 1}: {correct_answers[idx]}\n".encode())

    client_socket.close()

def main():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor ouvindo em {host}:{port}")

    questions = load_questions()
    
    while True:
        client_socket, _ = server_socket.accept()
        print(f"Conexão recebida de {_}")
        handle_client(client_socket, questions)

if __name__ == '__main__':
    main()