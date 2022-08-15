class Solution:
    def isHappy(self, n: int) -> bool:
        liczba = str(n)
        pierwszliczba = n
        suma = 0
        i = 0
        num_dict = {'1':1, '2':4, '3':9, '4':16, '5':25, '6':36, '7':49, '8':64, '9':81, '0':0}
        lista = []
        while(True):
            for x in liczba:
                suma += num_dict[x]
            if suma == 1:
                return True
            if suma in lista:
                return False
            lista.append(suma)
            liczba = str(suma)
            suma = 0
            i+= 1