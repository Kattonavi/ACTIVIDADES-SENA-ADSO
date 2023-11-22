class cafe():
    def queSoy(self):
        print("Soy un cafe")
        
class te():
    def queSoy(self):
        print("Soy un te")
        
def definicionBebida(bebida):
    bebida.queSoy()
    
definicionBebida(cafe())

