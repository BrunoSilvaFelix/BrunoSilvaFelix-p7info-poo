import enum


class TipoCliente(enum.Enum):
    PESSOA_FISICA = 1
    PESSOA_JURIDICA = 2

    def __str__(self):
        return self.name


if __name__ == '__main__':
    print("Os numeros enum sao: ")
    for tipo in (TipoCliente):
        print(type(tipo))
        print(tipo)
