class Operadores():
    operacoes = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else "Error: Divisão po zero."
    }

    @staticmethod
    def calcular(num1, operador, num2):
        return Operadores.operacoes[operador](num1, num2)