text = "bbbbbbbbbbbbbbbaaaaaaaaaaaaaacccdddd".upper()


def codificar(valor):
    codi = {}
    index = 0
    string = []
    for x in valor:     # here is gonna count the letters with the dict
        if x in codi:
            codi[x] += 1
        else:
            codi[x] = 1

    keys_v = list(codi.keys())      # take the number of letters and pass to list
    values_v = list(codi.values())      # take the letters and pass to list

    for x in values_v:
        if int(x) >= 9:   # here is gonna check if there more than 9 letters
            string.append('9')
            string.append(str(keys_v[index]))
            string.append(str(x - 9))
            string.append(keys_v[index])
            index += 1
        if int(x) < 9:  # here if there less than 9 letters
            string.append(str(x))
            string.append(keys_v[index])
            index += 1
    s = ''.join((string))
    return s


print(codificar(text))
