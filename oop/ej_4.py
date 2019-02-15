class fraccion():
    def __init__(self):
        pass
    def calc_suma(self):
        pass
    def calc_resta(self):
        pass
    def calc_multiplicacion(self):
        pass
    def calc_division(self):
        pass
class suma(fraccion):
    def __init__(self,fraccion_1,fraccion_2):
        self.fraccion_1 = fraccion_1
        self.fraccion_2 = fraccion_2
    def calc_suma(self):
        return self.fraccion_1 + self.fraccion_2
class resta(fraccion):
    def __init__(self,fraccion_1,fraccion_2):
        self.fraccion_1 = fraccion_1
        self.fraccion_2 = fraccion_2
    def calc_resta(self):
        return self.fraccion_1 - self.fraccion_2
class multiplicacion(fraccion):
    def __init__(self,fraccion_1,fraccion_2):
        self.fraccion_1 = fraccion_1
        self.fraccion_2 = fraccion_2
    def calc_multiplicacion(self):
        return self.fraccion_1 * self.fraccion_2
class division(fraccion):
    def __init__(self,fraccion_1,fraccion_2):
        self.fraccion_1 = fraccion_1
        self.fraccion_2 = fraccion_2
    def calc_division(self):
        return self.fraccion_1 / self.fraccion_2
a = suma(2/3,3/4)
print("la suma es: ",a.calc_suma())
b = resta(2/5,5/3)
print("la resta es: ",b.calc_resta())
c = multiplicacion(3/2,7/4)
print("la multiplicacion es: ",c.calc_multiplicacion())
d = division(4/2,2/4)
print("la division es: ",d.calc_division())
