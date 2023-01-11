class AbbNode:

    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def add(self, new_key, new_value):
        if new_key < self.key:
            # lo mando a la izquierda
            if self.left is None:
                self.left = AbbNode(new_key, new_value, None, None)
            else:
                self.left.add(new_key, new_value)
        
        elif new_key > self.key:
            # lo mando a la derecha
            if self.right is None:
                self.right = AbbNode(new_key, new_value, None, None)
            else:
                self.right.add(new_key, new_value)
        
        # else: no se hace nada
    
    def search(self, key):
        if self.key == key:
            return self.value
        
        elif key < self.key and self.left is not None:
            return self.left.search(key)
        
        elif key > self.key and self.right is not None:
            return self.right.search(key)
        
        else:
            return None
    
class Abb: # árbol de búsqueda binaria

    def __init__(self):
        self.root = None
    
    def add(self, key, value):
        # 1. El arbol está vacio
        if self.root is None:
            self.root = AbbNode(key, value, None, None)
        
        # 2. La raiz no está vacía
        self.root.add(key, value)
    
    def search(self, key):
        if self.root is None:
            return None
        
        return self.root.search(key)

arbol = Abb()
arbol.add('Leo', 'qwerd')
arbol.add('Julia', 'qwerd')
arbol.add('Maria', 'qwerd')
arbol.add('Marcelo', 'Ficha médica del Marcelo.')
arbol.add('Nadia', 'qwerd')

import pdb; pdb.set_trace()

