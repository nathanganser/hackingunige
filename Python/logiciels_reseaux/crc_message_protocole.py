import webbrowser


def convert_hex_to_bin(string):
    ini_string = string

    # Printing initial string
    print("Initial string", ini_string)

    # Code to convert hex to binary
    res = "{0:08b}".format(int(ini_string, 16))

    # Print the resultant string
    print("Resultant string", str(res))
    return str(res)


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


def verify_crc(security_message, crc):
    #if remainder is 0, then ok
    webbrowser.open(f'http://www.ee.unb.ca/cgi-bin/tervo/calc.pl?num={security_message}&den={crc}&f=d&e=1&p=1&m=1')
#verify_crc("1101111110112", "10101")


def pading_check(message, padding):
    padding = padding.replace("0", "")
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
    message = pading_check(message, fanion)
    message = fanion+message+fanion
    print(f'final message: {message}')
    print(message)
    return message

fanion = ""
champ_adresse_commande = ""
protocole_ip = "" #convert_hex_to_bin("0021")
donnes = "11110100"
crc = "10101"
#create_message(fanion, champ_adresse_commande+protocole_ip+donnes, crc)
