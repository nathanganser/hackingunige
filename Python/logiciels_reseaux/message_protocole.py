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
    print(f'A: {message}')
    print(f'B: {crc}')
    webbrowser.open(f'http://www.ee.unb.ca/cgi-bin/tervo/calc.pl?num={message}&den={crc}&f=d&e=1&p=1&m=1')
    print('Enter remainder:')
    remainder = input()
    if len(remainder)<16:
        for i in range(0, 16-len(remainder), +1):
            remainder = "0"+remainder
    return remainder


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


fanion = "01111110"
champ_adresse_commande = "11111111" + "00000011"
protocole_ip = convert_hex_to_bin("0021")
donnes = "0110100110010101"
crc = "1000100000010001"


def create_message(fanion, message, crc):
    remainder = calcul_crc(message, crc)
    message = message+remainder
    message = pading_check(message, fanion)
    message = fanion+message+fanion
    print(f'final message: {message}')
    print(message)
    return message

create_message(fanion, champ_adresse_commande+protocole_ip+donnes, crc)
