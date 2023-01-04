class Nodo:

    def __init__(self, valor, sgte):
        self.valor = valor
        self.sgte = sgte


class Lista:

    def __init__(self):
        self.primero = None
    
    def prepend(self, valor):
        # si la lista está vacía
        if self.primero is None:
            self.primero = Nodo(valor, None)
            return
        
        #caso genérico, lista no vacía
        self.primero = Nodo(valor, self.primero)
    
    def append(self, valor):
        # si la lista está vacía
        if self.primero == None:
            self.primero = Nodo(valor, None)
            return
        
        # caso general, la lista no está vacía
        it = self.primero
        while it.sgte is not None:
            it = it.sgte
        
        it.sgte = Nodo(valor, None)
    
    def len(self):
        if self.primero is None:
            return 0
        
        it = self.primero
        count = 1
        while it.sgte is not None:
            it = it.sgte
            count += 1
        
        return count
    
    def print(self):
        palabra = '['

        if self.primero is None:
            return palabra + ']'
        
        it = self.primero
        while True:
            palabra += '"' + it.valor + '"'
            if it.sgte is None:
                break
            it = it.sgte
            palabra += ', '
        
        print(palabra + ']')
    
    def contiene(self, valor):
        if self.primero is None:
            return False
        
        it = self.primero
        while True:
            if it.valor == valor:
                return True
            if it.sgte is None:
                break
            it = it.sgte
        
        return False
    
    def eliminar(self, valor):
        if self.primero is None:
            return
        
        if self.primero.valor == valor:
            self.primero = self.primero.sgte
            return
        
        # acá sabemos que existen al menos 2 nodos
        it = self.primero
        while it.sgte is not None:
            if it.sgte.valor == valor:
                it.sgte = it.sgte.sgte
                return
            it = it.sgte
    
    def ordenar(self):
        if self.primero is None or self.primero.sgte is None:
            return
        
        largo = self.len()
        it = self.primero
        while it.sgte is not None:
            if it.valor > it.sgte.valor:
                aux = it.sgte
                it.sgte = it.sgte.sgte
                aux.sgte = it
            it = it.sgte



        

        

if __name__ == '__main__':
    lst = Lista()
    lst.append('hola')
    lst.append('hello')
    lst.append('hallo')
    
    lst.prepend('adiós')
    lst.prepend('chao Pescao')

    #lst.eliminar('Hallo')
    import pdb; pdb.set_trace()



    
