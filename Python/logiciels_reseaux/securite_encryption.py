import math

def cesar_encryption(shift, text):
    encryption = ""

    for c in text:

        # check if character is an uppercase letter
        if c.isupper():

            # find the position in 0-25
            c_unicode = ord(c)

            c_index = ord(c) - ord("A")

            # perform the shift
            new_index = (c_index + shift) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)
            print(
                f'On trouve la position ({c_index} + {shift}) % 26 = {new_index} pour {c}, et on replace par {new_character}')

            # append to encrypted string
            encryption = encryption + new_character

        else:

            # since character is not uppercase, leave it as it is
            encryption += c

    print(f"Donc {text} devient {encryption}")

#cesar_encryption(7, "SECURITE")

def cesar_decryption(shift, encrypted_text):
    plain_text = ""

    for c in encrypted_text:

        # check if character is an uppercase letter
        if c.isupper():

            # find the position in 0-25
            c_unicode = ord(c)

            c_index = ord(c) - ord("A")

            # perform the negative shift
            new_index = (c_index - shift) % 26

            # convert to new character
            new_unicode = new_index + ord("A")

            new_character = chr(new_unicode)

            # append to plain string
            plain_text = plain_text + new_character
            print(
                f'- On trouve la position ({c_index} - {shift}) % 26 = {new_index} pour {c}, et on replace par {new_character}')


        else:

            # since character is not uppercase, leave it as it is
            plain_text += c

    print(f"Donc {encrypted_text} devient {plain_text}")

#cesar_decryption(3, "ORJLFLHO")

def VigenereGenerateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))


def VigenereEncryption(string, key):
    # EN MAJUSCULE
    key = VigenereGenerateKey(string, key)
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
        print(f'- On remplace {string[i]} par {chr(x)}')

    print("")
    print(("".join(encrypt_text)))
    return ("".join(encrypt_text))

#VigenereEncryption("CRYPTOGRAPHIE", "CLE")

def VigenereDecryption(encrypt_text, key):
    # EN MAJUSCULE
    key = VigenereGenerateKey(encrypt_text, key)
    orig_text = []
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
        print(f'- On remplace {encrypt_text[i]} par {chr(x)}')
    print("")
    print("".join(orig_text))
    return ("".join(orig_text))


#VigenereDecryption("qwumoeybu", "blue")

# Clés
p1_e = 37  # public key  (e; n) = (37; 77)
p1_d = 13  # private key  (d; n) = (13; 77)
p1_n = 77

p2_e = 39  # public key  (e; n) = (37; 77)
p2_d = 23  # private key  (d; n) = (13; 77)
p2_n = 85

message = 27


def chiffrer_bloc(n, e, message):
    C = (message ** e) % n
    print(f"{message}^{e} (mod {n}) = {C}")
    return C

#mes = chiffrer_bloc(p2_n, p2_e, message)

def dechiffrer_bloc(n, d, C):
    message = (C ** d) % n
    print(f"{C}^d (mod n) = {message}")
    return message

#dechiffrer_bloc(p1_n, p1_d, 3)


def h(x):
    hash = (25*x+2) % 40
    print(f'On trouve {hash} après avoir appliqué la function de hashage sur {x}')
    return hash


def sign(d, n, message):
    signature = (h(message) ** d) % n
    print(f"Le message signé est: h({message})^{d} (mod {n}) = {signature}")
    return signature

#si = sign(p1_d, p1_n, 13)


def verify_signature(signature, e, n, message):
    proof = (signature ** e) % n
    print(f'On vérifie la signature: {signature}^{e} (mod {n}) = {proof}')
    print(f'On confirme que {proof} == {h(message)}')
    return proof == h(message)

print(verify_signature(16, p2_e, p2_n, 26))



def create_clé(p,q):
    print(f'On choisi deux nombres premiers, {p} et {q}.')
    n = p*q
    phi_n = (p-1)*(q-1)
    print(f'On calcule n = {p} x {q} = {n}, et phi(n) = ({p}-1)({q}-1) = {phi_n}')
    print(f"On cherche e, l'exposant d'encryption e tel qu'il n'a pas de diviseur commun avec phi(n) et qu'il est plus petit que phi(n)")
    e = 97
    if math.gcd(e, phi_n) == 1 and e<phi_n:
        print(f'e = {e} par exemple')
    else:
        print('non!')
    d = (1 % phi_n)/e
    print(f"on calcule d, l'exposant de decryption, d = (1 mod phi(n))/e = {d}")
    print(f"le couple (n,e) = ({n}, {e}) est la clé publique et d = {d} la clé privée")
#create_clé(13, 17)