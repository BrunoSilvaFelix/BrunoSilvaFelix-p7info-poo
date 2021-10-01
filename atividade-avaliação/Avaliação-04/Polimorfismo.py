class Super:
    def hello(self):
        print("Olá, sou a superclasse!")
  
class Sub (Super):
    def hello(self):
        print("Olá, sou a subclasse!")

class Subsub (Sub):
    def hello(self):
        print("Olá, sou a subsubclasse!")

teste = Subsub()
teste.hello()
