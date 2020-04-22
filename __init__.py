"""
Creado el 11 de Julio de 2018

Editado 10 de abril 2020 Paul Carrasco


"""


class Persona(object):
    """
    Crea un ciudadano virtual
    """

    def __init__(self, n, e):
        """
        Constructor de la clase Persona

        :param n: Nombre.
        :param e: Edad
        :type n: str
        :type e: int

        """
        self.nombre = n
        self.edad = e
        self.calorias = 0

    def dormir(self):
        """
        La persona esta durmiendo placidamente...
        """
        print("Zzz..")

    def comer(self):
        """
        La persona esta comiendo...

        :return: Retorna la cantidad de calorias
        :rtype: float

        """
        return self.calorias


if __name__ == "__main__":
    n = input("Nombre: ")
    e = int(input("Edad: "))
    p = Persona(n, e)


