class Viagem:
    def __init__(self):
        self.__destino = "Sem destino"
        self.__distancia = 0.0
        self.__litros = 0.0
    def set_destino(self, destino):
        if len(destino) < 3: raise ValueError("Digite um destino válido")
        self.__destino = destino
    def get_destino(self):
        return self.__destino
    def set_distancia(self, distancia):
        if distancia <= 0: raise ValueError("A distância não pode ser 0 ou negativa")
    def get_distancia(self):
        return self.__distancia
    def set_litros(self, litros):
        if litros <= 0: raise ValueError("Os litros não podem ser 0 ou negativos")
    def get_litros(self):
        return self.__litros
    def Consumo(self, consumo):
        consumo = self.__distancia / self.__litros
        return consumo
class ViagemUI:
    def menu():
        print("1 - Calcular | 2 - Fim")
        return int(input("Escolha uma opção"))
    def main():
        option = ViagemUI.menu()
        while option != 2:
            match option:
                case 1: ViagemUI(calculo)
    def calculo():
        x = Viagem()
        x.set_destino
        x.set_distancia
        x.set_litros    