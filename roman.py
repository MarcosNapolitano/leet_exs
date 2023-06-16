class Solution:
    
    def romanToInt(self, string):
       
        keys = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        total = 0
        ultimo_valor = 0
        
        for i in range(len(string)):

            current = keys[string[i]]

            if i>0 and current>ultimo_valor:

                total+=current
                total-=ultimo_valor*2
                ultimo_valor = current
                continue
            
            total+=current
            ultimo_valor = current


        return total



a = Solution()

print(a.romanToInt("MCMXCIV"))

