from utilities import *
from data_streaming import calculate_debit

def combien_de_segments(segments, W, ACK=0):
    # dessin -> https://projects.invisionapp.com/freehand/document/zct6TT7KY
    i = 0
    while segments[i] != ACK:
        i += 1
    segments_a_envoyer = 0
    while segments[i+segments_a_envoyer] - segments[i] <= W:
        segments_a_envoyer += 1
    segments_a_envoyer -= 1
    print(f"Encore {segments_a_envoyer} segments peuvent être envoyés, donc jusqu'au segment {segments[i+segments_a_envoyer]}. Au delà, la différence entre le dernier segment transmis & confirmé ({ACK}) et le prochain segment à envoyer ({segments[i+segments_a_envoyer+1]}) dépasse la valeur reçue pour W ({W})")


def compute_buffer_size(size_of_segments_in_buffer, buffer_size):
    current_buffer = buffer_size

    for el in size_of_segments_in_buffer:
        current_buffer -= el

    print(f"l'espace disponible dans le buffer est {buffer_size} moins la somme des bits des sequences encore dans le buffer, donc {current_buffer} bits")
    return current_buffer

def find_temporisateur(one_direction_travel_time, beta):
    temp = one_direction_travel_time*2*beta
    print(f'La valeur du temporisateur est {one_direction_travel_time} x 2 x {beta} = {temp} ms')
    return temp

def taille_buffer_emetteur(one_direction_travel_time, debit_max, taille_segment=65535):
    RTT = one_direction_travel_time*2
    BDP = RTT * debit_max
    print(f"Avec un RTT de {one_direction_travel_time} x 2 = {RTT} ms et un débit max (B) de {debit_max} bits/s, la taille du buffeur de l'emetteur doit être RTT x B = {convert_bits_to_octets(BDP)} octets")

    return convert_bits_to_octets(BDP)


def taille_buffer_recepteur(debit_reel_en_bits, taille_fichier):
    information = {
        # in Mo/s
        # "son du microphone": 10,
        # "son du jeu": 5,
        # "vidéo de la camera": 0, #bits_to_Mo(convert_pixel_to_bits(200000, 20, 3*8)),
        "vidéo de l'écran": bits_to_Mo(convert_pixel_to_bits(480 * 280, 30, 3 * 8))
    }
    debit_requis_en_bits = Mo_to_bits(calculate_debit(information))
    duree_du_stream = taille_fichier/debit_requis_en_bits
    print("")
    print(f"La duree du transfert sera {taille_fichier} (taille fichier) / {debit_requis_en_bits} =  {duree_du_stream} secondes.")
    difference_debit = debit_reel_en_bits-debit_requis_en_bits
    print(f"La différence de débit qu'il va falloir compenser avec le buffer est de {debit_reel_en_bits} - {debit_requis_en_bits} = {difference_debit} bits/s")
    a_pretelecharger = duree_du_stream *difference_debit*-1
    print(f"Donc au moment de commencer le stream, il faut déjà avoir téléchargé {duree_du_stream} x {difference_debit*-1} = {a_pretelecharger} bits, soit {Mo_to_Go(bits_to_Mo(a_pretelecharger))} Go")
    print(f"La taille du buffer doit donc être au moins {Mo_to_Go(bits_to_Mo(a_pretelecharger))} Go.")
    print(f"Car durant les {duree_du_stream} secondes que va durer le stream, seulement {Mo_to_Go(bits_to_Mo(duree_du_stream*debit_reel_en_bits))} Go seront téléchargés à travers la connection en live.")
#combien_de_segments([0, 256, 512, 1024, 1536, 2048, 3072,4096, 5012], 2048, ACK=2048)

taille_buffer_recepteur(4*(2**20),Go_to_bits(4))