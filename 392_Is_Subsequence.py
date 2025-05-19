# La solucion fue implementada a traves del razonamiento que para que un string sea subsequente de otro este tiene que estar contenido dentro del string a evaluar, con eso en mente
# simplemente fuimos comparando que el string "s" tuviera los elementos de "t", pero usando dos apuntadores, uno para ir traqueando la palabra de "s" y otro para "t", de esta manera 
# de esta manera si hay una coincidencia desplazamos ambos apuntadores, si no simplemente seguimos recorriendo j, esto se hace hasta que se termine la palabra t, y una vez hecho esto
# se compara si la longitud de "i" es igual a la longitud de la palabra real. 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        k, l = len(s), len(t)

        while j < l:
            if i < k and s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        if i == k:
            return True
        else:
            return False
            