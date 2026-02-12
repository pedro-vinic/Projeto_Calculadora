
"""Módulo para gerenciar a conexão com o banco de dados e registrar operações."""

from getpass import getpass
import mysql.connector

def get_connection():
    """Cria e retorna uma conexão com o banco calculadora_db."""

    senha = getpass("Digite a senha do MySQL: ")

    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=senha,
        database="calculadora_db",
    )


def log_operation(a, b, operator, result, status, error_message=None):
    """
    Registra uma operação na tabela operations.

    status: 'success' ou 'error'
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO operations (a, b, operator, result, status, error_message)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (a, b, operator, result, status, error_message),
        )
        conn.commit()
    finally:
        conn.close()
