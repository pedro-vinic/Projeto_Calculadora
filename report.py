"""
Módulo para geração de relatórios analíticos da calculadora.
"""

from db import get_connection
import csv


def gerar_relatorio():
    conn = get_connection()
    cursor = conn.cursor()

    queries = {
        "total_operacoes": "SELECT COUNT(*) FROM operations;",
        "sucesso_erro": "SELECT status, COUNT(*) FROM operations GROUP BY status;",
        "operadores": "SELECT operator, COUNT(*) FROM operations GROUP BY operator;",
        "taxa_erro": """
            SELECT
            ROUND(
                100 * SUM(CASE WHEN status = 'error' THEN 1 ELSE 0 END) / COUNT(*),
                2
            )
            FROM operations;
        """
    }

    resultados = {}

    for nome, query in queries.items():
        cursor.execute(query)
        resultados[nome] = cursor.fetchall()

    conn.close()

    with open("relatorio.csv", "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)

        for nome, dados in resultados.items():
            writer.writerow([nome])
            for linha in dados:
                writer.writerow(linha)
            writer.writerow([])

    print("Relatório gerado com sucesso: relatorio.csv")


if __name__ == "__main__":
    gerar_relatorio()
