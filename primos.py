
def generar_primos(num_primos):
    if num_primos == 0:
        return []
    primos = []
    num = 2
    while len(primos) < num_primos:
        es_primo = True
        for primo in primos:
            if num % primo == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
        num += 1
    return primos
