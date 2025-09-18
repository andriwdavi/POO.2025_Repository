class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)
    def set_id(self, valor):
        if valor < 0: raise ValueError("Valor inválido")
        self.__id = valor
    def set_descricao(self, valor):
        if valor == "": raise ValueError("Valor inválido")
        self.__descricao = valor
    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor inválido")
        self.__valor = valor
    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor 