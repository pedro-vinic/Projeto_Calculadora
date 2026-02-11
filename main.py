"""
Módulo principal da aplicação.

Responsável por iniciar e executar o fluxo interativo da calculadora.
"""

from calculadora import Calculadora
from erros import (
    NumeroInvalidoError,
    OperadorInvalidoError,
    DivisaoPorZeroError,
    ExceptionGenericaError,
)


class Executar:
    """Classe responsável por executar o fluxo principal da calculadora."""

    def main(self):
        """Executa o loop principal da aplicação."""
        calculo = Calculadora()
        calculo.mensagem_inicial()

        while True:
            try:
                dados = calculo.menu()

                if dados == "sair":
                    print("-" * 40)
                    print("Encerrando a calculadora. Até mais!")
                    break

                num1, operador, num2 = dados
                resultado = calculo.calcular(num1, operador, num2)

                print("-" * 40)
                print(f"O resultado de {num1} {operador} {num2} é: {resultado}")
                print("-" * 40)

                while True:
                    pergunta = input("Deseja realizar outra operação? (s/n): ").strip().lower()

                    if pergunta == "s":
                        break  # volta para o início do while principal

                    elif pergunta == "n":
                        print("-" * 40)
                        print("Encerrando a calculadora. Até mais!")
                        return  # encerra o método main()

                    else:
                        print("Resposta inválida. Digite apenas 's' para sim ou 'n' para não.")

            except NumeroInvalidoError as e:
                print("-" * 40)
                print(f"Erro: {e}")
                print("-" * 40)

            except OperadorInvalidoError as e:
                print("-" * 40)
                print(f"Erro: {e}")
                print("-" * 40)

            except DivisaoPorZeroError as e:
                print("-" * 40)
                print(f"Erro: {e}")
                print("-" * 40)

            except ExceptionGenericaError as e:
                print("-" * 40)
                print(f"Erro inesperado: {e}")
                print("-" * 40)


if __name__ == "__main__":
    executando = Executar()
    executando.main()
