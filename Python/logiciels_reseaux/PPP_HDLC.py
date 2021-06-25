from crc_message_protocole import calcul_crc, pading_check
import webbrowser


def create_PPP_message():
    donnee = "0110100110010101"
    fanion = "01111110"
    champ_adresse_et_commande = "1111111100000011"
    protocole_niveau_superieur = "00100001" # 0021[hex] est IP
    crc = "10001000000100001" # CRC-16 = "10001000000100001"

    # compute CRC
    message_sans_crc = champ_adresse_et_commande + protocole_niveau_superieur + donnee
    crc_remainder = calcul_crc(message_sans_crc, crc)
    message = message_sans_crc + crc_remainder
    print(f'Message en hexa: {hex(int(fanion+message+fanion, 2))}')
    message = pading_check(message, fanion)
    message = fanion + message + fanion
    print(f'Message en binaire (avec traitement de padding): {message}')
    # Padding check

create_PPP_message()

