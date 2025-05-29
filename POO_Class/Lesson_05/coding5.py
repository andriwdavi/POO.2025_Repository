class Desbravador:
    def __init__(self):
        self.__nome = "Sem nome"
        self.__matricula = "Sem matricula"
    def __str__(self):
        return f"Nome: {self.__nome} | Matricula: {self.__matricula}"
    def set_nome(self, nome):
        if len(nome) < 3: raise ValueError("Nome invalido")
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_matricula(self, matricula):
        if len(matricula) != 14: raise ValueError("Matricula invalida")
        self.__matricula = matricula
    def get_matricula(self):
        return self.__matricula
    
    
x = Desbravador()
y = Desbravador()
x.set_nome("Emilly Vitoria")
x.set_matricula("20171011110001")
y.set_nome("Misael de Souza")
y.set_matricula("20241011110001")
dbvs = [x, y]
for x in dbvs:
    print(x)