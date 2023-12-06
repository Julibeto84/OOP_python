from typing import Optional, TypeVar
from abc import ABCMeta, abstractproperty, abstractmethod
import unittest

T = TypeVar('T')

# Interfaz para obtener el valor de un nodo en el árbol binario
class ValorObtenible(metaclass=ABCMeta):
    @abstractproperty
    def valor(self) -> T:
        """
        Propiedad abstracta para obtener el valor almacenado en el nodo.

        Returns:
            int: El valor almacenado en el nodo.
        """
        pass


# Interfaz para obtener el valor de un nodo en el árbol binario
class PadreObtenible(metaclass=ABCMeta):
    @abstractproperty
    def padre(self) -> 'NodoInterface':
        """
        Propiedad abstracta para obtener el nodo que representa al padre del nodo actual.

        Returns:
            NodoInterface: El nodo que representa al padre del nodo actual.
        """
        pass


# Interfaz para obtener los hijos izquierdo y derecho de un nodo en el árbol binario
class HijosObtenibles(metaclass=ABCMeta):
    @abstractproperty
    def izquierda(self) -> 'NodoInterface':
        """
        Propiedad abstracta para obtener el nodo que representa al hijo izquierdo del nodo actual.

        Returns:
            NodoInterface: El nodo que representa al hijo izquierdo del nodo actual.
        """
        pass

    @izquierda.setter
    @abstractmethod
    def izquierda(self, value: 'NodoInterface') -> None:
        """
        Propiedad abstracta para establecer el nodo que representa al hijo izquierdo del nodo actual.

        Args:
            value (NodoInterface): El nodo que representa al hijo izquierdo del nodo actual.
        """
        pass

    @abstractproperty
    def derecha(self) -> 'NodoInterface':
        """
        Propiedad abstracta para obtener el nodo que representa al hijo derecho del nodo actual.

        Returns:
            NodoInterface: El nodo que representa al hijo derecho del nodo actual.
        """
        pass

    @derecha.setter
    @abstractmethod
    def derecha(self, value: 'NodoInterface') -> None:
        """
        Propiedad abstracta para establecer el nodo que representa al hijo derecho del nodo actual.

        Args:
            value (NodoInterface): El nodo que representa al hijo derecho del nodo actual.
        """
        pass

# Interfaz completa para un nodo en el árbol binario
class NodoInterface(ValorObtenible, HijosObtenibles, PadreObtenible, metaclass=ABCMeta):
    """
    Interfaz que define los métodos que debe implementar cualquier clase que actúe como un nodo en un árbol binario.
    La interfaz incluye métodos para obtener el valor del nodo y sus hijos izquierdo y derecho.
    """
    pass


class Nodo(ValorObtenible, HijosObtenibles, PadreObtenible):
    def __init__(self, valor: T):
      self.__valor = valor
      self.__izquierda = None
      self.__derecha = None
      self.__padre = None
    
    @property
    def valor(self) -> T:
        return self.__valor
    
    @property
    def izquierda(self) -> 'NodoInterface':
        return self.__izquierda
    
    @izquierda.setter
    def izquierda(self, value: 'NodoInterface') -> None:
        self.__izquierda = value
        if value:
            value.__padre = self
        
    @property
    def derecha(self) -> 'NodoInterface':
        return self.__derecha
    
    @derecha.setter
    def derecha(self, value: 'NodoInterface') -> None:
        self.__derecha = value
        if value:
            value.__padre = self

    @property
    def padre(self) -> 'NodoInterface':
        return self.__padre

# Clase de prueba para Nodo
class TestNodo(unittest.TestCase):
    def test_obtener_valor(self):
        nodo = Nodo(10)
        self.assertEqual(nodo.valor, 10)

    def test_obtener_valor_private(self):
        nodo = Nodo(10)
        self.assertEqual(nodo._Nodo__valor, 10)

    def test_obtener_padre(self):
        nodo1 = Nodo(10)
        nodo2 = Nodo(20)
        nodo1.izquierda = nodo2
        self.assertEqual(nodo2.padre, nodo1)
        self.assertEqual(nodo2.padre.valor, 10)

    def test_obtener_padre_private(self):
        nodo1 = Nodo(10)
        nodo2 = Nodo(20)
        nodo1.izquierda = nodo2
        self.assertEqual(nodo2._Nodo__padre, nodo1)
        self.assertEqual(nodo2._Nodo__padre.valor, 10)

    def test_establecer_padre(self):
        nodo1 = Nodo(10)
        nodo2 = Nodo(20)
        nodo1.derecha = nodo2
        self.assertEqual(nodo2.padre, nodo1)
    
    def test_obtener_padre_nulo(self):
        nodo = Nodo(10)
        self.assertIsNone(nodo.padre)

    def test_obtener_izquierda(self):
        nodo = Nodo(10)
        nodo.izquierda = Nodo(5)
        self.assertIsInstance(nodo.izquierda, Nodo)

    def test_obtener_derecha(self):
        nodo = Nodo(10)
        nodo.derecha = Nodo(15)
        self.assertIsInstance(nodo.derecha, Nodo)

    def test_obtener_izquierda_private(self):
        nodo = Nodo(10)
        nodo.izquierda = Nodo(5)
        self.assertIsInstance(nodo._Nodo__izquierda, Nodo)

    def test_obtener_derecha_private(self):
        nodo = Nodo(10)
        nodo.derecha = Nodo(15)
        self.assertIsInstance(nodo._Nodo__derecha, Nodo)

    def test_obtener_valor_derecha(self):
        nodo = Nodo(10)
        nodo.derecha = Nodo(15)
        self.assertEqual(nodo.derecha.valor, 15)

    def test_obtener_valor_izquierda(self):
        nodo = Nodo(10)
        nodo.izquierda = Nodo(15)
        self.assertEqual(nodo.izquierda.valor, 15)

    def test_valor_generico(self):
        nodo_str = Nodo("Hola")
        self.assertEqual(nodo_str.valor, "Hola")

        nodo_float = Nodo(3.14)
        self.assertEqual(nodo_float.valor, 3.14)

    def test_obtener_izquierda_nula(self):
        nodo = Nodo(10)
        self.assertIsNone(nodo.izquierda)

    def test_obtener_derecha_nula(self):
        nodo = Nodo(10)
        self.assertIsNone(nodo.derecha)
        
    def test_obtener_valor_nulo(self):
        nodo = Nodo(10)
        self.assertIsNotNone(nodo.valor)

    def test_establecer_valores(self):
        nodo = Nodo(10)
        nodo.izquierda = Nodo(5)
        nodo.derecha = Nodo(15)


        self.assertIsInstance(nodo.izquierda, Nodo)
        self.assertIsInstance(nodo.derecha, Nodo)
        self.assertIsNone(nodo.padre)
        self.assertEqual(nodo.izquierda.padre, nodo.derecha.padre)


if __name__ == '__main__':
    unittest.main()
