# Funciones

def is_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def rotar_numero(num):
    if not is_primo(num):
        return False
    if num < 10:
        return True
    
    s = str(num)
    for i in range(len(s)):
        rotacion = (s[i:] + s[:i])
        if not is_primo(rotacion):
            return False
    return True







        

