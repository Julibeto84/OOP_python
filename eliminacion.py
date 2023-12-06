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

# Clase que implementa la interfaz para representar un nodo en el árbol binario
class Nodo(NodoInterface):

    def __init__(self, valor: int):
        """
        Constructor de la clase Nodo.

        Args:
            valor (int): El valor que se almacenará en el nodo.
        """
        self.__valor: int = valor
        self.izquierda: Optional[NodoInterface] = None
        self.derecha: Optional[NodoInterface] = None
        self.padre: Optional[NodoInterface] = None


    @property
    def padre(self) -> 'NodoInterface':
        """
        Implementación del método para obtener el valor almacenado en el nodo.

        Returns:
            int: El valor almacenado en el nodo.
        """
        return self.__padre
    
    @padre.setter
    def padre(self, valor: 'NodoInterface') -> None:
        self.__padre = valor

    @property
    def izquierda(self) -> 'NodoInterface':
        """
        Implementación del método para obtener el nodo que representa al hijo izquierdo del nodo actual.

        Returns:
            NodoInterface: El nodo que representa al hijo izquierdo del nodo actual.
        """
        return self.__izquierda
    
    @izquierda.setter
    def izquierda(self, valor: 'NodoInterface') -> None:
        if not valor is None:
            valor.padre = self
        self.__izquierda = valor

    @property
    def derecha(self) -> 'NodoInterface':
        """
        Implementación del método para obtener el valor almacenado en el nodo.

        Returns:
            int: El valor almacenado en el nodo.
        """
        return self.__derecha
    
    @derecha.setter
    def derecha(self, valor: 'NodoInterface') -> None:
        if not valor is None:
            valor.padre = self
        self.__derecha = valor


    @property
    def valor(self) -> int:
        """
        Implementación del método para obtener el nodo que representa al hijo derecho del nodo actual.

        Returns:
            NodoInterface: El nodo que representa al hijo derecho del nodo actual.
        """
        return self.__valor

# Interfaz para operaciones de inserción en el árbol
class OperacionesInsercion(metaclass=ABCMeta):
    @abstractmethod
    def insertar(self, valor: T, proposicion: Callable[[T, T], bool]) -> None:
        pass

    @abstractmethod
    def insertarAll(self, valores: Tuple[T], proposicion: Callable[[T, T], bool]) -> None:
        pass

# Interfaz para operaciones de búsqueda en el árbol
class OperacionesBusqueda(metaclass=ABCMeta):

    @abstractmethod
    def buscar(self, valor: T) -> Optional[NodoInterface]:
        pass

    @abstractmethod
    def buscarAll(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        pass

    @abstractmethod
    def buscarWhere(self, proposicion: Callable[[Optional[NodoInterface]], bool]) -> Tuple[Optional[NodoInterface]]:
        pass

# Interfaz para operaciones de eliminación eßßßn el árbol
class OperacionesEliminacion(metaclass=ABCMeta):
    @abstractmethod
    def eliminar(self, valor: T) -> None:
        pass

    @abstractmethod
    def eliminarAll(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        pass

    @abstractmethod
    def eliminarWhere(self, proposicion: Callable[[Optional[NodoInterface]], bool]) -> Tuple[Optional[NodoInterface]]:
        pass

# Interfaz que combina todas las operaciones de un árbol binario
class Arbol(OperacionesInsercion, OperacionesBusqueda, OperacionesEliminacion, metaclass=ABCMeta):
    pass

class ArbolBinario(Arbol):

    def __init__(self, raiz=None) -> None:
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
    
    def buscar(self, valor: T) -> Optional[NodoInterface]:
        return self._buscar_recursiva(valor, self.__raiz)

    def buscarAll(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        resultados = []
        self._buscarAll_recursiva(valor, self.__raiz, resultados)
        return tuple(resultados)

    def buscarWhere(self, proposicion: Callable[[Optional[NodoInterface]], bool]) -> Tuple[Optional[NodoInterface]]:
        resultados = []
        self._buscarWhere_recursiva(proposicion, self.__raiz, resultados)
        return tuple(resultados)

    def _buscar_recursiva(self, valor: T, nodo_actual: Optional[NodoInterface]) -> Optional[NodoInterface]:
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual

        if valor < nodo_actual.valor:
            return self._buscar_recursiva(valor, nodo_actual.izquierda)
        
        if valor > nodo_actual.valor:
            return self._buscar_recursiva(valor, nodo_actual.derecha)

    def _buscarAll_recursiva(self, valor: T, nodo_actual: Optional[NodoInterface], resultados: list[Optional[NodoInterface]]) -> None:
        if nodo_actual is None:
            return

        if nodo_actual.valor == valor:
            resultados.append(nodo_actual)

        self._buscarAll_recursiva(valor, nodo_actual.izquierda, resultados)
        self._buscarAll_recursiva(valor, nodo_actual.derecha, resultados)

    def _buscarWhere_recursiva(self, proposicion: Callable[[Optional[NodoInterface]], bool], nodo_actual: Optional[NodoInterface], resultados: list[Optional[NodoInterface]]) -> None:
        if nodo_actual is None:
            return

        if proposicion(nodo_actual):
            resultados.append(nodo_actual)

        self._buscarWhere_recursiva(proposicion, nodo_actual.izquierda, resultados)
        self._buscarWhere_recursiva(proposicion, nodo_actual.derecha, resultados)
        
    def eliminar(self, valor: T) -> None:
        self.__raiz = self._eliminar_recursiva(valor, self.__raiz)

    def _eliminar_recursiva(self, valor: T, nodo_actual: Optional[NodoInterface]) -> Optional[NodoInterface]:
        if nodo_actual is None:
            return None

        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar_recursiva(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar_recursiva(valor, nodo_actual.derecha)
        else:
            # Nodo a eliminar encontrado
            nodo_actual = self._eliminar_nodo(nodo_actual)

        return nodo_actual

    def _eliminar_nodo(self, nodo_actual: NodoInterface) -> Optional[NodoInterface]:
        if nodo_actual.izquierda is None:
            return nodo_actual.derecha
        elif nodo_actual.derecha is None:
            return nodo_actual.izquierda

        # El nodo tiene dos hijos, encontrar el sucesor inmediato
        sucesor = self._encontrar_minimo(nodo_actual.derecha)
        # Crear un nuevo nodo con el valor del sucesor
        nuevo_nodo = Nodo(sucesor.valor)
        nuevo_nodo.izquierda = nodo_actual.izquierda
        nuevo_nodo.derecha = self._eliminar_recursiva(sucesor.valor, nodo_actual.derecha)

        return nuevo_nodo


    def _encontrar_minimo(self, nodo_actual: NodoInterface) -> NodoInterface:
        while nodo_actual.izquierda is not None:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual

    def eliminarAll(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        resultados = []
        self.__raiz = self._eliminarAll_recursiva(valor, self.__raiz, resultados)
        return tuple(resultados)

    def _eliminarAll_recursiva(self, valor: T, nodo_actual: Optional[NodoInterface], resultados: list[Optional[NodoInterface]]) -> Optional[NodoInterface]:
        if nodo_actual is None:
            return None

        if valor == nodo_actual.valor:
            resultados.append(nodo_actual)
            nodo_actual = self._eliminarAll_recursiva(valor, nodo_actual.izquierda, resultados)
            nodo_actual = self._eliminarAll_recursiva(valor, nodo_actual.derecha, resultados)
        else:
            nodo_actual.izquierda = self._eliminarAll_recursiva(valor, nodo_actual.izquierda, resultados)
            nodo_actual.derecha = self._eliminarAll_recursiva(valor, nodo_actual.derecha, resultados)

        return nodo_actual

    def eliminarWhere(self, proposicion: Callable[[Optional[NodoInterface]], bool]) -> Tuple[Optional[NodoInterface]]:
        resultados = []
        self.__raiz = self._eliminarWhere_recursiva(proposicion, self.__raiz, resultados)
        return tuple(resultados)

    def _eliminarWhere_recursiva(self, proposicion: Callable[[Optional[NodoInterface]], bool], nodo_actual: Optional[NodoInterface], resultados: list[Optional[NodoInterface]]) -> Optional[NodoInterface]:
        if nodo_actual is None:
            return None

        if proposicion(nodo_actual):
            resultados.append(nodo_actual)
            return None  

        nodo_actual.izquierda = self._eliminarWhere_recursiva(proposicion, nodo_actual.izquierda, resultados)
        nodo_actual.derecha = self._eliminarWhere_recursiva(proposicion, nodo_actual.derecha, resultados)

        return nodo_actual


        
    

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

    def setUp(self):
        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(15)
        nodo4 = Nodo(3)
        nodo5 = Nodo(7)
        nodo1.izquierda = nodo2
        nodo1.derecha = nodo3
        nodo2.izquierda = nodo4
        nodo2.derecha = nodo5
        self.arbol = ArbolBinario(nodo1)

    def test_buscar_existente(self):
        resultado = self.arbol.buscar(10)
        self.assertEqual(resultado.valor, 10)

    def test_buscar_no_existente(self):
        resultado = self.arbol.buscar(20)
        self.assertIsNone(resultado)

    def test_buscarAll_existente(self):
        resultados = self.arbol.buscarAll(5)
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].valor, 5)

    def test_buscarAll_no_existente(self):
        resultados = self.arbol.buscarAll(20)
        self.assertEqual(len(resultados), 0)

    def test_buscarWhere_proposicion(self):
        def es_menor_que_10(nodo: Optional[NodoInterface]) -> bool:
            return nodo is not None and nodo.valor < 10

        resultados = self.arbol.buscarWhere(es_menor_que_10)
        self.assertEqual(len(resultados), 3)
        self.assertTrue(all(resultado.valor < 10 for resultado in resultados))

    def test_eliminar_existente(self):
        self.arbol.eliminar(5)
        resultado = self.arbol.buscar(5)
        self.assertIsNone(resultado)

    def test_eliminar_no_existente(self):
        self.arbol.eliminar(20)
        resultado = self.arbol.buscar(20)
        self.assertIsNone(resultado)

    def test_eliminarAll_existente(self):
        self.arbol.eliminarAll(5)
        resultados = self.arbol.buscarAll(5)
        self.assertEqual(len(resultados), 0)

    def test_eliminarAll_no_existente(self):
        self.arbol.eliminarAll(20)
        resultados = self.arbol.buscarAll(20)
        self.assertEqual(len(resultados), 0)

    def test_eliminarWhere_proposicion(self):
        def es_menor_que_10(nodo: Optional[NodoInterface]) -> bool:
            return nodo is not None and nodo.valor < 10

        self.arbol.eliminarWhere(es_menor_que_10)
        resultados = self.arbol.buscarWhere(es_menor_que_10)
        self.assertEqual(len(resultados), 0)


if __name__ == '__main__':
    unittest.main()
