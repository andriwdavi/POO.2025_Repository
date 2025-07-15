from datetime import datetime, timedelta

class treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)

    def set_id(self, id):
        if id < 0: raise ValueError("ID Inválida")
        self.__id = id
    def get_id(self):
        return self.__id
    
    def set_data(self, data):
        if data > datetime.now(): raise ValueError("Data inválida")
        self.__data = data
    def get_data(self):
        return self.__data
    
    def set_distancia(self, distancia):
        if distancia < 0: raise ValueError("Distância inválida")
        self.__distancia = distancia
    def get_distancia(self):
        return self.__distancia
    
    def set_tempo(self, tempo):
        if tempo < timedelta(0): raise ValueError("Tempo inválido")
        self.__tempo = tempo
    def get_tempo(self):
        return self.__tempo
    
    def __str__(self):
        return f"ID: {self.__id} | Data: {self.__data} | Distância: {self.__distancia} | Tempo: {self.__tempo}"
    
class treinoUI:

    @classmethod
    def menu(cls):
        menu = int(input("1 - Inserir treino | 2 - Listar treinos | 3 - Buscar treino | 4 - Atualizar dados | 5 - Excluir treino | 6 - Treino mais rápido | 7 - Sair: "))
        return menu
    
    @classmethod
    def main(cls):
        op = 0
        while op != 7:
            op = treinoUI.menu()
            match op:
                case 1: treinoUI.novo_treino()
                case 2: treinoUI.listar()
                case 3: treinoUI.buscar()
                case 4: treinoUI.atualizar()
                case 5: treinoUI.excluir()
                case 6: treinoUI.rapido()

    def inserir(cls):
        id = int(input("Inserir o ID da corrida: "))
        data = datetime.strptime(input("Informe a distância percorrida: "))
        distancia = float(input("Informe a distância percorrida: "))
        h, m, s = map(int, input("Informe a duração da corrida: ").split(":"))
        tempo = timedelta(hours= h , minutes= m , seconds = s)
        for t in cls.__treinos:
            if t.get_id() == id:
                print("ID Já cadastrado. Digite novamente")
                return

    def listar(cls):
        if len(cls.__treinos) == 0:
            print("Nenhum treino cadastrado")
        for t in cls.__treinos:
            print(t)
    
