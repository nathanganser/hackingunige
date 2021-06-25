import math
from sympy import symbols, solve, Pow, Eq
from utilities import ASCII_to_binary, xor

def emplacements_bits_controle(nbr_de_bits):
    # 2**C - C > nbr_de_bits
    C = 1
    while 2 ** C - C <= nbr_de_bits:
        C += 1

    count = 1
    array = []
    for i in range(0, C, +1):
        array.append(count)
        count *= 2

    print(f'Puisque 2^{C} - {C} > {nbr_de_bits} ...')
    print(
        f'Les {C} bits de contrôle seront aux emplacements suivants: {array} (1 est le premier element tout à droite, et on compte de droite à gauche)')
    return array

def is_pair(array):
    count = 0
    for el in array:
        count += el

    return count % 2 == 0


# use ASCII_to_binary and don't forget to change parite_pair!

def hamming(array, parite_pair):
    #Use an inverted array (where the first two control bits are on the left of the array)
    positions_to_ignore = [0, 1, 3, 7]
    show_array = []
    for i in range(0, len(array), +1):
        if i not in positions_to_ignore:
            show_array.append(array[i])
    print(f'Checking the message: {show_array[::-1]} (has been reverted back to normal)')

    separation = 2 # 2, 4, 8
    width = 1 # 1, 2, 4, 8
    head_start = 0 # 0, 1, 2, 4
    count = 0
    while count<len(positions_to_ignore):
        temp_array = []
        for i in range(head_start, len(array), +separation):
            for e in range(0, width, +1):
                try:
                    temp_array.append(array[i+e])
                except Exception as e:
                    pass
        #print(f'Control {count}: {temp_array}, pair: {is_pair(temp_array)}')
        if parite_pair and not is_pair(temp_array):
            array[positions_to_ignore[count]] = 1
        if not parite_pair and is_pair(temp_array):
            array[positions_to_ignore[count]] = 1
        separation *=2
        width *=2
        count += 1
        if head_start == 0:
            head_start = 1
        elif head_start == 1:
            head_start = 3
        elif head_start == 3:
            head_start = 7
    print(f'Result: {array}')
    return array

#message = ASCII_to_binary("H")
#print(message)
# 1. array = [0, 0, 0, 0, X, 0, 0, 0, X, 0, X, X] (fill in and reverse)
#array = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
#array = array[::-1]
#reverse_mess = hamming(array, False)
#new_ok_message = reverse_mess[::-1]
#print(f'New OK (reversed) message: {new_ok_message}')


def correct_hamming(message, parite_pair):
    # Use an inverted array (where the first two control bits are on the left of the array)
    correction_bits = []
    reset_message = message.copy()
    for i in [0, 1, 3, 7]:
        correction_bits.append(message[i])
        reset_message[i] = 0
    array = hamming(reset_message, parite_pair)
    calculated_bits = []
    for i in [0, 1, 3, 7]:
        calculated_bits.append(array[i])
    print(f'Bits from message {correction_bits}')
    print(f'Recalculated bits {calculated_bits}')

    position_error = int(xor(correction_bits, calculated_bits), 2) -1
    if position_error == -1:
        print('Le message est correct!')
    else:
        #print(f'Avant correction, le message est {message}')
        if message[position_error] == 0:
            message[position_error] = 1
        else:
            message[position_error] = 0
        print(f"L'erreur est à la position {position_error}")
        print(f'Après correction, le message est {message}')

    return message

message = [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1]
message = message[::-1]
#reverse_mess[2] = 0
#print(f'Fakult: {reverse_mess}')
message = correct_hamming(message, False)
message = message[::-1]
print(f'Message corrigé & inversé: {message}')



# [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0]
# [0, 0, 0, 1]