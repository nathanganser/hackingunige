def convert_ko_to_bits(ko_value):
    # kilo octets are kilo bytes
    return ko_value*8000

def convert_bits_to_octets(bits):
    return bits/8

def xor(a, b):
    res = ""
    for i in range(0, len(a), +1):
        if a[i] == b[i]:
            res += "0"
        else:
            res += "1"
    #print(f'resultat xor: {res}')
    return res

def bits_to_Mo(bits):
    octets = bits/8
    Mo = octets/1000000
    print(f'Après conversion, les {bits} bits valent {Mo} Mo.')
    return Mo

def Mo_to_bits(Mo):
    Megabits = Mo*8
    bits = Megabits*1000000
    print(f'Après conversion, les {Mo} Mo valent {bits} bits.')
    return bits

def Go_to_bits(Go):
    Gbits = Go*8
    bits = Gbits*1000000000
    print(f'Après conversion, les {Go} Go valent {bits} bits.')
    return bits

def Go_to_Mo(Go):
    Mo = Go * 1000
    print(f"Aprs conversion, les {Go} Go valent  {Mo} Mo.")
    return Mo
def Mo_to_Go(Mo):
    Go = Mo / 1000
    print(f'Après conversion, les {Mo} Mo valent {Go} Go.')
    return  Go

def convert_pixel_to_bits(pixels, img_per_second, bits_per_pixel):
    bits_par_image = pixels*bits_per_pixel
    bits_par_seconde = bits_par_image*img_per_second
    print(f"On sait que chaque image contient {pixels} pixels et que {img_per_second} images sont enregistrées par seconde. De plus, on sait qu'il nous faut {bits_per_pixel} bits par pixel qu'on veut représenter.")
    print(f"Chaque image contient donc {pixels} x {bits_per_pixel} = {bits_par_image} bits, ce qui représente {bits_par_image} x {img_per_second} = {bits_par_seconde} bits par seconde.")
    return bits_par_seconde


def ASCII_to_binary(message):
    mes = bin(ord(message))[2:]
    while len(mes)<len(message)*8:
        mes = "0"+mes
    return mes

