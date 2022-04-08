class Fibonacci:
    def __iter__(self):
        self.anterior = 0
        self.proximo = 1
        self.interacoes = ""
        return self

    def __next__(self):
        sequencia_fibonacci = [self.anterior]
        try:
            self.interacao = int(input("Digite sequência Fibonacci: "))
            if self.interacao == 0:
                raise StopIteration
        except:
            print("!!! Operação cancelada !!!")
        for x in range(self.interacao - 1):
            soma = self.anterior + self.proximo
            self.anterior = self.proximo
            self.proximo = soma
            sequencia_fibonacci.append(self.proximo)
        return sequencia_fibonacci

    def sequencia_fibonacci():
        fibonacci = Fibonacci()
        fibonacci = iter(fibonacci)
        sequencia_fibonacci = {
            posicao_da_sequencia + 1: valor_da_sequencia for posicao_da_sequencia,
            valor_da_sequencia in enumerate(next(fibonacci))
        }
        print(sequencia_fibonacci)
        return sequencia_fibonacci