text = "bbbbbbbbbbbbbbbaaaaaaaaaaaaaacccdddd".upper()

def codificar(valor):
    codi = {}
    index = 0
    string = []
    for x in valor:
        if x in codi:
            codi[x] += 1
        else:
            codi[x] = 1

    keys_v = list(codi.keys())
    values_v = list(codi.values())

    for x in values_v:
        if int(x) >= 9:
            string.append('9')
            string.append(str(keys_v[index]))
            string.append(str(x - 9))
            string.append(keys_v[index])
            index += 1
        if int(x) < 9:
            string.append(str(x))
            string.append(keys_v[index])
            index += 1
    s = ''.join((string))
    return s

  
 print(codificar(text))
