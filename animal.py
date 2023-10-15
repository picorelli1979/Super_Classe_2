# AQUI ESTÁ A  SUPER CLASSE: 
class Animal:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def voz(self):
        print(f'{self.nome} fez barulho')

# AQUI ESTÁ 2 SUB CLASSES 
class Mamifero(Animal):
    def __init__(self, nome, idade, cor, patas):
        super().__init__(nome, idade)
        self.cor = cor
        self.patas = patas

class Reptil(Animal):
    def __init__(self, nome, idade, veneno):
        super().__init__(nome, idade)
        self.veneno = veneno

# AQUI ESTÁ 3 CLASSES DE ANIMAIS RECEBENDO SUA ESPECIE :

class Gato(Mamifero):
    def __init__(self, nome, idade, cor, patas, bigodes):
        super().__init__(nome, idade, cor, patas)
        self.bigodes = bigodes
    def voz(self):
        print(f'{self.nome} fez miau')

class Cachorro(Mamifero):
    def __init__(self, nome, idade, cor, patas, comida):
        super().__init__(nome, idade, cor, patas)
        self.comida = comida
    def voz(self):
        print(f'{self.nome} fez auau')
        
class Baleia(Mamifero):
    def __init__(self, nome, idade, cor, peso, tamanho):
        super().__init__(nome, idade, cor, peso)
        self.tamanho = tamanho 
    def mergulhar(self):
        print(f'Uma Baleia chamada {self.nome} e medindo {self.tamanho} desceu há 2.000metros de Profundidade!!!!')              

class Cobra(Reptil):
    def __init__(self, nome, idade, veneno):
        super().__init__(nome, idade, veneno)
    def voz(self):
        print(f'{self.nome} fez s-s-s-s-ssssss')
        
class Iguana_Verde(Reptil):
    def __init__(self, nome, idade, chicotada):
        super().__init__(nome, idade,chicotada)
        self.chicotada = chicotada
    def ferroada(self):
        print(f'{self.nome} deu uma {self.chicotada} e João ficou com Febre.....')            