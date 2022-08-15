class Solution:
    def Convert(self,string):
        list1=[]
        list1[:0]=string
        return list1
    
    def smallestNumber(self, num: int) -> int:
        if num <0:
            lista = self.Convert(str(num)[1:])
            lista.sort(reverse=True)
            tempstring = ''
            for x in lista:
                tempstring += x
            return int('-'+tempstring)
        elif num > 0:
            lista = self.Convert(str(num))
            lista.sort()
            tempstring = ''
            i = 0
            for x in lista:
                if x == '0':
                    tempstring += x
                    i += 1
                else:
                    break
            tempstring = lista[i] + tempstring
            for z in lista[i+1:]:
                tempstring += z
            return int(tempstring)
        elif num == 0:
            return 0