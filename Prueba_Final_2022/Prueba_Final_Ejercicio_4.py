class Fraccion():
        def __init__(self, numerador, denominador):

            try:
                if denominador != 0:
                    self.numerador = int(numerador)
                    self.denominador = int(denominador)
            except ZeroDivisionError as e:
                print(e)
                raise Exception("ZeroFraccionError")



        def maximo_comun_divisor(self, a, b):
            temporal = 0
            while b != 0:
                temporal = b
                b = a % b
                a = temporal
            return a

        def minimo_comun_multiplo(self, a, b):
            return (a * b) / self.maximo_comun_divisor(a, b)

        def __add__(self, otra):
            mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
            diferencia_self = mcm / self.denominador
            diferencia_otra = mcm / otra.denominador
            numerador_resultado = (diferencia_self * self.numerador) + \
                                  (diferencia_otra * otra.numerador)
            return Fraccion(numerador_resultado, mcm)

        def __str__(self):
            return "(" + str(self.numerador) + "," + str(self.denominador) + ")"

fraccion1 = Fraccion (4 ,5)
fraccion2 = Fraccion (3 ,4)
print (fraccion1 + Fraccion(1,8))
fraccion4 = (4, 0)
print((fraccion4))
#fraccion3 = fraccion1 + fraccion4
#print(fraccion3)

