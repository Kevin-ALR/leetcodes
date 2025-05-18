# Solucion 1: Empezando del final al inicio, si observamos que el elemento anterior es menor lo restamos del actual
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sol = 0
        i = len(s) - 1

        while i >= 0:
            if (values[s[i]] > values[s[i - 1]] and i > 0):
                sol += values[s[i]] - values[s[i - 1]]
                i -= 2
                print(i)
            else:
                sol += values[s[i]]
                i -= 1
        return sol
    

# Solucion 2: Empezando del inicio al final realizando las operaciones correspondientes si es menor que el de la derecha lo restamos, si no lo sumamos

class Solution:
    def romanToInt(self, s: str) -> int:
        v = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = 0
        i = 0 
        j = len(s)

        while i < j:
            if i < j - 1 and v[s[i]] > v[s[1]]:
                sum -= v[s[i]]
            else:
                sum += v[s[i]]
            i += 1
        
        return sum