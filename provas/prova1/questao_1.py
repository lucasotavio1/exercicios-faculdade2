# Criar a classe aqui, abaixo está o exemplo de uso, que não deverá ser alterado.
class ProcessadorDeDados:
    def __init__(self, nome: str):
        self._nome = nome

    def get_nome(self): return self._nome

    def _somar_valores(self, valores): return sum(valores)

    def processar_valores(self, *valores: int):
        if not valores:
            return 0.0
        else:
            total = self._somar_valores(valores)
            media = total / len(valores)
            return float(media)


# Exemplo de uso:
processador = ProcessadorDeDados("Processador de Média")


processador = ProcessadorDeDados("Processador de Média")

# Passando 3 argumentos
media_1 = processador.processar_valores(10, 20, 30)
print(f"Média de 10, 20, 30: {media_1}")

# Passando 5 argumentos
media_2 = processador.processar_valores(5, 15, 25, 35, 45)
print(f"Média de 5, 15, 25, 35, 45: {media_2}")

# Passando um único argumento
media_3 = processador.processar_valores(100)
print(f"Média de 100: {media_3}")

# Passando nenhum argumento
media_4 = processador.processar_valores()
print(f"Média sem valores: {media_4}")
