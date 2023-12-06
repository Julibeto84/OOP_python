from abc import ABCMeta, abstractmethod
from typing import Callable, Optional, Optional, TypeVar, Tuple
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

# Interfaz que combina todas las operaciones de un árbol binario
class Arbol(metaclass=ABCMeta):
    pass

class ArbolBinario(Arbol):
    def __init__(self, raiz = None) -> None:
        self.__raiz = raiz
        
    @property
    def raiz(self):
        return self.__raiz
    

# Clase de prueba para ArbolBinario
class TestArbol(unittest.TestCase):
    def test_asignar_raiz(self):
        nodo = Nodo(10)
        arbol = ArbolBinario(nodo)
        self.assertEqual(arbol._ArbolBinario__raiz, nodo)

    def test_raiz_vacia(self):
        arbol = ArbolBinario()
        self.assertIsNone(arbol._ArbolBinario__raiz)

    def test_insertar_raiz(self):
        arbol = ArbolBinario(Nodo(10))
        self.assertEqual(arbol._ArbolBinario__raiz.valor, 10)


if __name__ == '__main__':
    unittest.main()