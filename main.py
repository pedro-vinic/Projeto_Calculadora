from calculadora import Calculadora, NumeroInvalidoError, OperadorInvalidoError

class Executar():
    def main(self):
        calculo = Calculadora()
        calculo.mensagem_inicial()            
        while True:
            try:
                resultado = calculo.menu()
                if resultado == "sair":
                    print("-"*40)
                    print("Encerrando a calculadora. Até mais!")
                    break
                elif resultado == "erro":
                    print("-"*40)
                    print("Entrada inválida. Por favor, insira números válidos.")
                    continue
                
                num1, operador, num2 = resultado
                resultado = calculo.calcular(num1, operador, num2)
                if isinstance(resultado, str) and "Erro" in resultado:
                    print("-"*40)
                    print(resultado)
                    print("-"*40)
                else:
                    print("-"*40)
                    print(f"O resultado de {num1} {operador} {num2} é: {resultado}")
                    print("-"*40)

                pergunta = input("Deseja realizar outra operação? (s/n): ").lower().strip()
                if pergunta != 's':
                    print("-"*40)
                    print("Encerrando a calculadora. Até mais!")
                    break
                
            except NumeroInvalidoError as e:
                print("-"*40)
                print(e)

            except OperadorInvalidoError as e:
                print("-"*40)
                print(e)

if __name__ == "__main__":
    calculando = Executar()
    calculando.main()