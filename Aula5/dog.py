

class Dog():
    def __init__(self, nome, raca,idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 5    


    def latir(self):
        print(self.nome)
        print('AUauauauau.....')
  
    def dormir(self):
        self.energia = 5
        print('ZZZZZZZZZZZZZZ {}'.format(self.energia))
        sleep(5)

    def andar(self):
        if self.energia:
            self.energia -= 1
            print('andando .... {}' .format(self.energia))
        else:
        print('dog está casando e não pode andar ')

    def __str__(self):
        return "nome: {} idade {} raça: {} " .format(
            self.nome, self.idade, self.raça
        ))
                

dog1 = Dog('bilu', 'pitbull', 1)
dog2 = Dog('rex', 'podlle', 2)

#print(dog1.dormir)
#print(dog2.dormir)
dog2.dormir()
dog1.dormir()