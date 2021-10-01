from typing import Type

class Casa:
    def __init__(self) -> None:
        self.__endereco = "Rua dos Limoeiros"

    def acender_luzes(self) -> None:
        print("Estou Acendendo as Luze")

    def get_endereco(self) -> str:
        return self.__endereco

class Pessoa:
    def __init__(self, nome: str, local: Type[Casa]) -> None:
        self.__local = local
        self.__nome = nome

    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()

    def apresentar_local(self) -> None:
        endereço = self.__local.get_endereco()
        print(endereço)

casa_de_amigo = Casa()
ana = Pessoa("Ana", casa_de_amigo)
ana.entrar_no_local()
ana.apresentar_local()
