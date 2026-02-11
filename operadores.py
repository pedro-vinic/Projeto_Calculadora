"""Módulo de operadores matemáticos para a calculadora."""

from erros import DivisaoPorZeroError


class Operadores:
    """Classe contendo métodos estáticos para realizar operações matemáticas."""

    @staticmethod
    def dividir(a, b):
        """Realiza a divisão de a por b, verificando se b é zero."""            
        if b == 0:
            raise DivisaoPorZeroError("Não é possível dividir por zero.")
        return a / b

    @staticmethod
    def calcular(num1, operador, num2):
        """Realiza a operação matemática com base no operador fornecido."""
        operacoes = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": Operadores.dividir,
        }

        return operacoes[operador](num1, num2)
