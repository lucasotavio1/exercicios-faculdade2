import math
from typing import List


class ListaCPF:
    __slots__ = ['_cpf', '_valores']

    def __init__(self, cpf: str):
        self._cpf = cpf
        self._valores = []
        self._processar()

    def _processar(self):
        for digito_str in self._cpf:
            try:
                digito = int(digito_str)
                if digito == 1:
                    self._valores.append(1.0)
                elif digito - 1 == 0 or digito < 0:
                    self._valores.append(-1.0)
                else:
                    self._valores.append(math.factorial(digito) / (digito - 1))
            except ValueError:
                self._valores.append(-1.0)

    def get_valores(self) -> List[float]:
        return self._valores


class ListaNascimento:
    __slots__ = ['_data_nascimento', '_valores']

    def __init__(self, data_nascimento: str):
        self._data_nascimento = data_nascimento
        self._valores = []
        self._processar()

    def _processar(self):
        for digito_str in self._data_nascimento:
            try:
                digito = int(digito_str)
                if digito == 0:
                    self._valores.append(1.0)
                else:
                    self._valores.append(math.factorial(digito) / digito)
            except ValueError:
                self._valores.append(1.0)

    def get_valores(self) -> List[float]:
        return self._valores


class AnalisadorDeListas:
    __slots__ = ['_lista_a', '_lista_b']

    def __init__(self, lista_a: List[float], lista_b: List[float]):
        self._lista_a = lista_a
        self._lista_b = lista_b

    def analisar(self):
        set_a = set(self._lista_a)
        set_b = set(self._lista_b)
        lista_c = list(set_a.symmetric_difference(set_b))

        print("--- Análise de Dados ---")
        print(f"Lista CPF: {self._lista_a}")
        print(f"Lista Nascimento: {self._lista_b}")
        print(f"Lista C (elementos únicos em uma das listas): {lista_c}")

        all_in_cpf = all(item in set_a for item in lista_c)
        print(
            f"Todos os números da Lista C podem ser encontrados na Lista CPF: {all_in_cpf}")

        all_in_nascimento = all(item in set_b for item in lista_c)
        print(
            f"Todos os números da Lista C podem ser encontrados na Lista Nascimento: {all_in_nascimento}")


# --- Execução do Código ---
# Coleta de dados do usuário
cpf_digitado = input("Digite o CPF (sem pontos e traços): ")
data_nascimento_digitada = input("Digite a data de nascimento (ddmmaaaa): ")

# Cria instâncias das classes de processamento
lista_cpf = ListaCPF(cpf_digitado)
lista_nascimento = ListaNascimento(data_nascimento_digitada)

# Cria uma instância da classe de análise, acessando os valores através dos métodos get
analisador = AnalisadorDeListas(
    lista_cpf.get_valores(), lista_nascimento.get_valores())

# Executa a análise
analisador.analisar()
