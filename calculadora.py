"""Módulo principal da calculadora, responsável por interagir com o usuário e realizar os cálculos."""

from operadores import Operadores
from erros import NumeroInvalidoError, OperadorInvalidoError


class Calculadora:
    """Classe principal da calculadora, responsável 
    por interagir com o usuário e realizar os cálculos."""
    
    def __init__(self):
        """Inicializa os atributos da calculadora."""
        self.num1 = None
        self.operador = None
        self.num2 = None

    def mensagem_inicial(self):
        """Exibe a mensagem de boas-vindas e as operações disponíveis."""
        print("Bem-vindo à Calculadora Simples!")
        print("Operações disponíveis: +, -, *, /")

    def menu(self):
        """Exibe o menu de entrada para o usuário e coleta os dados necessários para o cálculo."""
        print("-" * 40)
        print("Escolha dois números e um operador para realizar a operação.")
        print("Digite 'sair' para encerrar a calculadora a qualquer momento.")
        print("-" * 40)

        num1 = input("Digite o primeiro número: ").strip()
        if num1.lower() == "sair":
            return "sair"

        operador = input("Digite o operador (+, -, *, /): ").strip()
        if operador.lower() == "sair":
            return "sair"

        num2 = input("Digite o segundo número: ").strip()
        if num2.lower() == "sair":
            return "sair"

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError as exc:
            raise NumeroInvalidoError("Você deve digitar apenas números válidos.") from exc

        simbolos = {"+", "-", "*", "/"}
        if operador not in simbolos:
            raise OperadorInvalidoError(
                f"Operador '{operador}' inválido. Use apenas (+, -, *, /)."
            )

        return num1, operador, num2

    def calcular(self, num1, operador, num2):
        """Realiza o cálculo com base nos números e operador fornecidos, 
        utilizando a classe Operadores para executar a operação."""
        return Operadores.calcular(num1, operador, num2)
