class contador():
    def __init__(self,recuento):
        self.recuento = recuento
    def incrementar(self):
        self.recuento +1
    def decrementar(self):
        self.recuento -1
c = contador(0)
