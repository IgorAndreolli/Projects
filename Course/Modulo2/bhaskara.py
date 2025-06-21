import math


class bhaskara:
    def delta(self, a, b, c):
        return math.pow(b, 2) -4*a*c


    def main(self):
        a = float(input("Digite o valor do coeficiente 'a': "))
        b = float(input("Digite o valor do coeficiente 'b': "))
        c = float(input("Digite o valor do coeficiente 'c': "))
        print(self.calcula_raizes(a, b, c)) 

    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)
        if d == 0:
            raiz1 = (-b +math.sqrt(d))/(2 * a)
            return 1, raiz1
        
        else:
            if d < 0:
                return 0
        
            else:
                raiz1 = (-b +math.sqrt(d))/(2 * a)
                raiz2 = (-b -math.sqrt(d))/(2 * a)
                print("A primeira raiz é: ", raiz1)
                print("A segunda raiz é: ", raiz2)
                return 2, raiz1, raiz2





    