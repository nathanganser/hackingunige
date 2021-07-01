import webbrowser
from utilities import bin_to_hex, convert_hex_to_bin




def calcul_crc(message, crc):
    zeros_to_add = len(crc)-1
    for i in range(0, zeros_to_add, +1):
        message += "0"
    print(f'A: {message}')
    print(f'B: {crc}')
    webbrowser.open(f'http://www.ee.unb.ca/cgi-bin/tervo/calc.pl?num={message}&den={crc}&f=d&e=1&p=1&m=1')
    print('Enter remainder:')
    remainder = input()
    if len(remainder)<zeros_to_add:
        for i in range(0, zeros_to_add-len(remainder), +1):
            remainder = "0"+remainder
    print(f'Trame à envoyer pour le CRC: {remainder}')
    return remainder

#calcul_crc("10000110", "110110")

def verify_crc(security_message, crc):
    #if remainder is 0, then ok
    webbrowser.open(f'http://www.ee.unb.ca/cgi-bin/tervo/calc.pl?num={security_message}&den={crc}&f=d&e=1&p=1&m=1')
#verify_crc("0101100110111", "110110")


def pading_check(message, padding):
    padding = padding.replace("0", "")
    padding = padding[0:len(padding)]
    going = True
    pos_to_check_from = 0
    while going:
        position = message.find(padding, pos_to_check_from, len(message))
        if position >= 0:
            #print(f'-> {message[position + len(padding):-1]}')
            message = message[0:position] + padding[0:-1] + "0" + padding[-1] + message[position + len(padding):len(message)]
            pos_to_check_from = position + 1
        else:
            going = False
            return message





def create_message(fanion, message, crc):
    remainder = calcul_crc(message, crc)
    message = message+remainder
    print(f'in Hex (before padding check): {bin_to_hex(fanion+ message+fanion)}')
    message = pading_check(message, fanion)
    message = fanion+message+fanion
    print(f'final message (with padding check): {message}')
    return message

fanion = "01111110"
champ_adresse_commande = "1111111100000011"
protocole_ip = convert_hex_to_bin("0021")
donnes = "0110100110010101"
crc = "10001000000100001"
#mes = create_message(fanion, champ_adresse_commande+protocole_ip+donnes, crc)
