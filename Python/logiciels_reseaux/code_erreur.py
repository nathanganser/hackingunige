val = "011010111010100010111"


def check(message, interval):
    count = 0
    for i in range(-interval, -len(message) - 1, -interval * 2):
        # print(f'looking from {i}')
        for p in range(0, interval, +1):
            # print(f'looking at {val[i-p]} at position {i-p}, length: {p}')
            try:
                if val[i - p] == "1":
                    count += 1
            except Exception as e:
                # print(f'{e}')
                pass

    if count % 2 == 0:
        # print('is pair!')
        return 0
    else:
        # print('is impair!')
        return 1


def get_controle_sequence(seq):
    con = ""
    m = -1
    while m > (-len(seq)):
        con = seq[m] + con
        m = m * 2
    print(f'Controle seq: {con}')
    return con


def invert(string):
    if string == "1":
        return "0"
    else:
        return "1"


def get_calculated_sequence(seq, parite=0):
    con = get_controle_sequence(seq)
    mult = 1
    res = ''
    for el in range(-1, -len(con) - 1, -1):
        p = check(seq, mult)
        if (p == 1 and parite == 0):
            res = invert(con[el]) + res
        elif (p == 0 and parite == 0):
            res = con[el] + res

        mult = 2 * mult
    print(f'Calculated seq: {res}')
    return res


def xor(a, b):
    res = ""
    for i in range(0, len(a), +1):
        if a[i] == b[i]:
            res += "0"
        else:
            res += "1"
    print(f'resultat xor: {res}')
    return res


def check_if_only_0(message):
    check = 1
    for i in message:
        if i == "1":
            check = 0
    return check


def complete_calcul(message, parite=0):
    controle = get_controle_sequence(message)
    calcule = get_calculated_sequence(message, parite)
    res = xor(controle, calcule)
    if check_if_only_0(res) == 1:
        print('message sans erreur')
    else:
        print(f'Erreur dans message a position {res}')


complete_calcul(val)