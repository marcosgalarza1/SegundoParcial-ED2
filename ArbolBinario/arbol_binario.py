class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        def _insertar(nodo, valor):
            if nodo is None:
                return Nodo(valor)
            if valor < nodo.valor:
                nodo.izquierda = _insertar(nodo.izquierda, valor)
            else:
                nodo.derecha = _insertar(nodo.derecha, valor)
            return nodo

        self.raiz = _insertar(self.raiz, valor)

    def buscar(self, valor):
        def _buscar(nodo, valor):
            if nodo is None:
                return False
            if nodo.valor == valor:
                return True
            elif valor < nodo.valor:
                return _buscar(nodo.izquierda, valor)
            else:
                return _buscar(nodo.derecha, valor)
        return _buscar(self.raiz, valor)

    def eliminar(self, valor):
        def _eliminar(nodo, valor):
            if nodo is None:
                return None
            if valor < nodo.valor:
                nodo.izquierda = _eliminar(nodo.izquierda, valor)
            elif valor > nodo.valor:
                nodo.derecha = _eliminar(nodo.derecha, valor)
            else:
                if nodo.izquierda is None:
                    return nodo.derecha
                elif nodo.derecha is None:
                    return nodo.izquierda
                temp = nodo.derecha
                while temp.izquierda:
                    temp = temp.izquierda
                nodo.valor = temp.valor
                nodo.derecha = _eliminar(nodo.derecha, temp.valor)
            return nodo
        self.raiz = _eliminar(self.raiz, valor)

    def inorden(self):
        def _inorden(nodo):
            return _inorden(nodo.izquierda) + [nodo.valor] + _inorden(nodo.derecha) if nodo else []
        return _inorden(self.raiz)

    def encontrar_padre(self, nodo, valor):
        """Encuentra el padre de un nodo con el valor dado."""
        if nodo is None:
            return None
        if (nodo.izquierda and nodo.izquierda.valor == valor) or (nodo.derecha and nodo.derecha.valor == valor):
            return nodo
        if valor < nodo.valor:
            return self.encontrar_padre(nodo.izquierda, valor)
        else:
            return self.encontrar_padre(nodo.derecha, valor)

    def tio(self, t, s):
        """Devuelve True si t es tío de s, False en caso contrario."""
        if self.raiz is None:
            return False

        # Encuentra los padres de t y s
        padre_t = self.encontrar_padre(self.raiz, t)
        padre_s = self.encontrar_padre(self.raiz, s)

        # Si alguno de los nodos no tiene padre, no pueden ser tío y sobrino
        if padre_t is None or padre_s is None:
            return False

        # Verifica si los padres son hermanos
        abuelo_s = self.encontrar_padre(self.raiz, padre_s.valor)
        abuelo_t = self.encontrar_padre(self.raiz, padre_t.valor)

        return abuelo_s is not None and abuelo_s == abuelo_t and padre_t != padre_s


arbol = ArbolBinario()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(18)

print(arbol.tio(5, 12))  # Devuelve True
print(arbol.tio(15, 7))  # Devuelve True
print(arbol.tio(10, 3))  # Devuelve False
