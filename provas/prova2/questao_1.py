class Lote:
    def __init__(self):
        self._triangulos = []
        self.area_total = 0.0

    def adicionar_triangulo(self, triangulo):
        if triangulo:
            self._triangulos.append(triangulo)
            self.area_total += triangulo.calcular_area()


class Triangulo:
    _lado1: float
    _lado2: float
    _lado3: float

    def __init__(self, lado1, lado2, lado3):
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3

    def calcular_area(self):
        pass


class TrianguloRetangulo(Triangulo):
    _base: float
    _altura: float

    def __init__(self, base, altura):
        super().__init__(base, altura, None)
        self._base = base
        self._altura = altura

    def calcular_area(self):
        return (self._base * self._altura) / 2


class TrianguloEquilatero(Triangulo):
    _lado: float

    def __init__(self, lado):
        super().__init__(lado, lado, lado)
        self._lado = lado

    def calcular_area(self):
        return (3 ** 0.5 / 4) * (self._lado ** 2)


class TrianguloIsosceles(Triangulo):
    _base: float
    _lado_igual: float

    def __init__(self, base, lado_igual):
        super().__init__(base, lado_igual, lado_igual)
        self._base = base
        self._lado_igual = lado_igual

    def calcular_area(self):
        if self._lado_igual <= (self._base / 2):
            return 0
        else:
            altura = (self._lado_igual**2 - (self._base/2)**2)**0.5
            return 0.5 * self._base * altura
