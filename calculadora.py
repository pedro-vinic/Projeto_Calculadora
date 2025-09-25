from operadores import Operadores

class Calculadora:

    def __init__(self):
        self.num1 = None
        self.operador = None
        self.num2 = None

    def mensagem_inicial(self):
        print("Bem-vindo à Calculadora Simples!")
        print("Operações disponíveis: soma, subtração, multiplicação, divisão.")

    def menu(self):
        print("-" * 40)
        print("Escolha dois números e um operador para realizar a operação.")
        print("Digite 'sair' para encerrar a calculadora a qualquer momento.")
        print("-" * 40)
        
        num1 = input("Digite o primeiro número: ")
        if num1.lower().strip() == 'sair':
            return "sair"
        
        operador = input("Digite o operador (+, -, *, /): ")
        if operador.lower().strip() == 'sair':
            return "sair"
        
        num2 = input("Digite o segundo número: ")
        if num2.lower().strip() == 'sair':
            return "sair"
        
        try:
            num1 = float(num1)
            num2 = float(num2)
            
        except ValueError:
            raise NumeroInvalidoError("Você deve digitar apenas números válidos")
        
        simbolos = {"+", "-", "*", "/"}
        if operador not in simbolos:
            raise OperadorInvalidoError(f"Operador '{operador}' inválido. Use apenas (+, -, *, /).")
        
        return num1, operador, num2
    

    def calcular(self, num1, operador, num2):
        return Operadores.calcular(num1, operador, num2)
    

class NumeroInvalidoError(Exception):
    pass

class OperadorInvalidoError(Exception):
    pass
    