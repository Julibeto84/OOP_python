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

class Nodo(NodoInterface):
    def __init__(self, valor: T):
      self.__valor = valor
      self.izquierda = None
      self.derecha = None
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
        if value != None:
            value.__padre = self
        
    @property
    def derecha(self) -> 'NodoInterface':
        return self.__derecha
    
    @derecha.setter
    def derecha(self, value: 'NodoInterface') -> None:
        self.__derecha = value
        if value != None:
            value.__padre = self
            
    @property
    def padre(self) -> 'NodoInterface':
        return self.__padre


# Interfaz para operaciones de inserción en el árbol
class OperacionesInsercion(metaclass=ABCMeta):
    @abstractmethod
    def insertar(self, valor: T, proposicion: Callable[[T, T], bool]) -> None:
        pass

    @abstractmethod
    def insertarAll(self, valores: Tuple[T], proposicion: Callable[[T, T], bool]) -> None:
        pass

# Interfaz que combina todas las operaciones de un árbol binario
class Arbol(OperacionesInsercion, metaclass=ABCMeta):
    pass


class ArbolBinario(Arbol):
    def __init__(self, raiz= None) -> None:
        self.__raiz = raiz 
        
    @property
    def raiz(self):
        return self.__raiz
    
    def insertar(self, valor: T, proposicion: Callable[[T, T], bool]) -> None:
        
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return
        self._insertar_recursiva(valor, proposicion, self.raiz)
    
    def _insertar_recursiva(self, valor: T, proposicion: Callable[[T, T], bool], nodo_actual: 'NodoInterface') -> None:
        
        if valor == nodo_actual.valor:
            return
        
        if not proposicion(valor, nodo_actual.valor) and nodo_actual.derecha is None:
            nodo_actual.derecha = Nodo(valor)
            return
        
        if proposicion(valor, nodo_actual.valor) and nodo_actual.izquierda is None:
            nodo_actual.izquierda = Nodo(valor)
            return
        
        if not proposicion(valor, nodo_actual.valor): 
            self._insertar_recursiva(valor, proposicion, nodo_actual.derecha)
            return
        
        if proposicion(valor, nodo_actual.valor):
            self._insertar_recursiva(valor, proposicion, nodo_actual.izquierda)
            return
        
    def insertarAll(self, valores: Tuple[T], proposicion: Callable[[T, T], bool]) -> None:
        for value in valores:
            self.insertar(value, proposicion)    
        
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

    def test_insertar_izquierda(self):
        arbol = ArbolBinario(Nodo(10))
        arbol.insertar(5, lambda x, y: x < y)
        self.assertEqual(arbol._ArbolBinario__raiz.izquierda.valor, 5)

    def test_insertar_derecha(self):
        arbol = ArbolBinario(Nodo(10))
        arbol.insertar(15, lambda x, y: x < y)
        self.assertEqual(arbol._ArbolBinario__raiz.derecha.valor, 15)

    def test_insertarAll(self):
        arbol = ArbolBinario(Nodo(10))
        arbol.insertarAll((5, 15, 3, 7), lambda x, y: x < y)
        self.assertEqual(arbol._ArbolBinario__raiz.izquierda.valor, 5)
        self.assertEqual(arbol._ArbolBinario__raiz.derecha.valor, 15)
        self.assertEqual(arbol._ArbolBinario__raiz.izquierda.izquierda.valor, 3)
        self.assertEqual(arbol._ArbolBinario__raiz.izquierda.derecha.valor, 7)

if __name__ == '__main__':
    unittest.main()
