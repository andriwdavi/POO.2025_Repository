class Contato:
    def __init__(self, i, n, e, f):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
    def get_nome(self):
        return self.__nome    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_fone(self, fone):
        self.__fone = fone
        
class ContatoUI:
    __contatos = []

    @classmethod
    def main(cls):
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Fim")
        return int(input("Informe uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        c = Contato(id, nome, email, fone)
        cls.__contatos.append(c)

    @classmethod
    def listar(cls):
        for c in cls.__contatos:
            print(c)

    @classmethod
    def atualizar(cls):
        ContatoUI.listar()
        x = int(input("Informe o ID do contato que deseja atualizar:\n"))
        for c in cls.__contatos:
            if x == c.get_id():
                contatoEncontrado = c

        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        contatoEncontrado.set_nome(nome)
        contatoEncontrado.set_email(email)
        contatoEncontrado.set_fone(fone)
        
    @classmethod
    def excluir(cls):
        pass

    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome do contato: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome):
                print(c)

ContatoUI.main()


