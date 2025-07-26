class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def esta_cheia(self):
        return self.tamanho == self.capacidade

    def obter_tamanho(self):
        return self.tamanho

    def obter_elemento(self, posicao):
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError("Posição inválida.")
        return self.dados[posicao - 1]

    def modificar_elemento(self, posicao, valor):
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError("Posição inválida.")
        self.dados[posicao - 1] = valor

    def inserir(self, posicao, valor):
        if self.esta_cheia():
            raise OverflowError("Lista cheia.")
        if posicao < 1 or posicao > self.tamanho + 1:
            raise IndexError("Posição inválida.")
        for i in range(self.tamanho, posicao - 1, -1):
            self.dados[i] = self.dados[i - 1]
        self.dados[posicao - 1] = valor
        self.tamanho += 1

    def remover(self, posicao):
        if self.esta_vazia():
            raise ValueError("Lista vazia.")
        if posicao < 1 or posicao > self.tamanho:
            raise IndexError("Posição inválida.")
        removido = self.dados[posicao - 1]
        for i in range(posicao - 1, self.tamanho - 1):
            self.dados[i] = self.dados[i + 1]
        self.dados[self.tamanho - 1] = None
        self.tamanho -= 1
        return removido