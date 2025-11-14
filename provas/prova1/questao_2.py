from datetime import date, datetime


# Criar a classe aqui, abaixo está o exemplo de uso, que não deverá ser alterado.
class Estado:
    __slots__ = ['_nome', '_sigla']

    def __init__(self, nome: str, sigla: str):
        self._nome = nome
        self._sigla = sigla

    def get_nome(self):
        return self._nome

    def get_sigla(self):
        return self._sigla

    def set_nome(self, novo_nome: str):
        self._nome = novo_nome

    def set_sigla(self, nova_sigla: str):
        self._sigla = nova_sigla


class Cidade:
    __slots__ = ['_nome', '_estado']

    def __init__(self, nome: str, estado: Estado):
        self._nome = nome
        self._estado = estado

    def get_nome(self):
        return self._nome

    def get_estado(self):
        return self._estado

    def set_estado(self, novo_estado: Estado):
        self._estado = novo_estado

    def set_nome(self, novo_nome: str):
        self._nome = novo_nome


class Endereco:
    __slots__ = ['_rua', '_numero', '_bairro', '_cep', '_cidade']

    def __init__(self, rua: str, numero: str, bairro: str, cep: str, cidade: Cidade):
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._cep = cep
        self._cidade = cidade

    def get_rua(self):
        return self._rua

    def get_numero(self):
        return self._numero

    def get_bairro(self):
        return self._bairro

    def get_cep(self):
        return self._cep

    def get_cidade(self):
        return self._cidade

    def set_rua(self, nova_rua: str):
        self._rua = nova_rua

    def set_numero(self, novo_numero: str):
        self._numero = novo_numero

    def set_bairro(self, novo_bairro: str):
        self._bairro = novo_bairro

    def set_cep(self, novo_cep: str):
        self._cep = novo_cep

    def set_cidade(self, nova_cidade: Cidade):
        self._cidade = nova_cidade


class Funcionario:
    __slots__ = ['_nome', '_nascimento', '_cpf', '_enderecos']

    def __init__(self, nome: str, nascimento: date, cpf: str, enderecos: Endereco):
        self._nome = nome
        self._nascimento = nascimento
        self._cpf = cpf
        self._enderecos = enderecos

    def get_nome(self):
        return self._nome

    def get_nascimento(self):
        return self._nascimento

    def get_cpf(self):
        return self._cpf

    def get_enderecos(self):
        return self._enderecos

    def set_nome(self, novo_nome: str):
        self._nome = novo_nome

    def set_nascimento(self, nova_nascimento: date):
        self._nascimento = nova_nascimento

    def set_cpf(self, novo_cpf: str):
        self._cpf = novo_cpf

    def set_enderecos(self, novo_endereco: Endereco):
        self._enderecos = novo_endereco


# 1. Cria uma instância de Estado
estado_sp = Estado("São Paulo", "SP")

# 2. Cria uma instância de Cidade, usando o objeto Estado
cidade_sp = Cidade("São Paulo", estado_sp)

# 3. Cria uma instância de Endereco, usando o objeto Cidade
endereco_func = Endereco(
    rua="Rua da Programação",
    numero="123",  # Changed to string as per the type hint in the class
    bairro="Centro",
    cep="01000-000",
    cidade=cidade_sp
)

# 4. Cria uma instância de Funcionario, usando o objeto Endereco
funcionario = Funcionario(
    nome="João da Silva",
    nascimento=date(1990, 5, 15),
    cpf="123.456.789-00",
    enderecos=endereco_func
)

# 5. Imprime os dados para verificar se a implementação está correta
print("--- Dados do Funcionário ---")
print(f"Nome: {funcionario.get_nome()}")
print(f"CPF: {funcionario.get_cpf()}")
print(f"Data de Nascimento: {funcionario.get_nascimento()}")

# Acesso aos dados do endereço através do objeto Endereco do funcionário
print("\n--- Dados do Endereço ---")
endereco = funcionario.get_enderecos()
print(f"Rua: {endereco.get_rua()}, {endereco.get_numero()}")
print(f"Bairro: {endereco.get_bairro()}")
print(f"CEP: {endereco.get_cep()}")

# Acesso aos dados da cidade e do estado através do objeto Endereco
cidade = endereco.get_cidade()
estado = cidade.get_estado()
print(f"Cidade: {cidade.get_nome()}")
print(f"Estado: {estado.get_nome()} ({estado.get_sigla()})")
