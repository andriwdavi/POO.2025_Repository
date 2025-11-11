class ProgramaFidelidade:
    @staticmethod
    def adicionar_pontos(cliente, valor_servico):
        pontos_adquiridos = int(valor_servico // 10)
        cliente.set_pontos(cliente.get_pontos() + pontos_adquiridos)
        ProgramaFidelidade.atualizar_nivel(cliente)

    @staticmethod
    def atualizar_nivel(cliente):
        pontos = cliente.get_pontos()
        if pontos >= 200:
            cliente.set_nivel("Ouro")
        elif pontos >= 100:
            cliente.set_nivel("Prata")
        else:
            cliente.set_nivel("Bronze")

    @staticmethod
    def calcular_desconto(cliente, valor_servico):
        if cliente.get_nivel() == "Ouro":
            return valor_servico * 0.9
        elif cliente.get_nivel() == "Prata":
            return valor_servico * 0.95
        return valor_servico
