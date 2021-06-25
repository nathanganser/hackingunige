from utilities import convert_pixel_to_bits, convert_bits_to_octets, Go_to_bits, bits_to_Mo, Mo_to_bits
from data_streaming import calculate_debit

def combien_de_segments(segments, W, ACK=0):
    # combien_de_segments([0, 256, 512, 1024, 1536, 2048, 3072,4096, 5012], 2048, ACK=2048)
    # dessin -> https://projects.invisionapp.com/freehand/document/zct6TT7KY
    i = 0
    while segments[i] != ACK:
        i += 1
    segments_a_envoyer = 0
    while segments[i+segments_a_envoyer] - segments[i] <= W:
        segments_a_envoyer += 1
    segments_a_envoyer -= 1
    print(f"Encore {segments_a_envoyer} segments peuvent être envoyés, donc du bit {segments[i]} jusqu'au bit {segments[i+segments_a_envoyer]}. Au delà, la différence entre le dernier segment transmis & confirmé ({ACK}) et le prochain segment à envoyer ({segments[i+segments_a_envoyer]}) dépasse la valeur reçue pour W ({W})")

#combien_de_segments([0, 1024, 2048, 3072, 4096, 5120, 6144], 2048, 1024)

def compute_buffer_size(size_of_segments_in_buffer, buffer_size):
    # tout en octets
    # compute_buffer_size([512,512], 4096)
    current_buffer = buffer_size

    for el in size_of_segments_in_buffer:
        current_buffer -= el

    print(f"L'espace disponible dans le buffer est {buffer_size} octets moins la somme des octets des sequences encore dans le buffer {size_of_segments_in_buffer}, donc {current_buffer} octets")

    return current_buffer

#compute_buffer_size([512, 2500-2048], 4096)


def find_temporisateur(one_direction_travel_time, beta):
    # one_direction_travel_time [ms]
    temp = one_direction_travel_time*2*beta
    print(f'La valeur du temporisateur est {one_direction_travel_time} x 2 x {beta} = {temp} ms')
    return temp

find_temporisateur(170, 3)

def taille_buffer_emetteur(one_direction_travel_time, debit_max, taille_segment=65535):
    # debit max en octet, travel_time in SECONDS
    # taille_buffer_emetteur(0.170, 4*(2**20))
    RTT = one_direction_travel_time*2
    BDP = RTT * debit_max
    print(f"Avec un RTT de {one_direction_travel_time} x 2 = {RTT} s et un débit max (B) de {debit_max} octets/s, la taille du buffeur de l'emetteur doit être RTT x B = {BDP} octets")

    return convert_bits_to_octets(BDP)

taille_buffer_emetteur(170/1000,4*(2**20))

def taille_buffer_recepteur(debit_reel_en_bits, taille_fichier):
    #, taille_fichier en bits
    information = {
        # in Mo/s
        # "son du microphone": 10,
        # "son du jeu": 5,
        # "vidéo de la camera": 0, #bits_to_Mo(convert_pixel_to_bits(200000, 20, 3*8)),
        "vidéo de l'écran": bits_to_Mo(convert_pixel_to_bits(420 * 280, 30, 24))
    }
    debit_requis_en_bits = Mo_to_bits(calculate_debit(information))

    duree_du_stream = taille_fichier/debit_requis_en_bits
    print("")
    print(f"La duree du transfert sera {taille_fichier} (taille fichier) / {debit_requis_en_bits} =  {duree_du_stream} secondes.")
    difference_debit = debit_requis_en_bits-debit_reel_en_bits
    print(f"CORRIGE: EBr = {debit_requis_en_bits} - {debit_reel_en_bits} = {difference_debit} bits")
    print(f"La différence de débit qu'il va falloir compenser avec le buffer est de {debit_reel_en_bits} - {debit_requis_en_bits} = {difference_debit} bits/s")
    a_pretelecharger = duree_du_stream *difference_debit
    print(f"Donc au moment de commencer le stream, il faut déjà avoir téléchargé {duree_du_stream}[s] x {difference_debit}[bits] = {bits_to_Mo(a_pretelecharger)} Mo")
    print(f"La taille du buffer doit donc être au moins {bits_to_Mo(a_pretelecharger)} Mo")

taille_buffer_recepteur(4*(2**20)*8, Go_to_bits(4))
print('--')
