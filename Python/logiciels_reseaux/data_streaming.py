from utilities import *



information = {
    # in Mo/s
    #"son": bits_to_Mo(4*(10**7)),
    #"images": 50*bits_to_Mo(4*(10**6)),
    #"son du microphone": 10, # Mo
    "son du jeu": 7, # Mo
    #"vidéo de la camera": bits_to_Mo(convert_pixel_to_bits(200000, 20, 3*8)),
    #"vidéo de l'écran": bits_to_Mo(convert_pixel_to_bits(1080*720, 60, 3*8))

}
def calculate_debit(information):
    Mo_total = 0
    for el in information:
        Mo_total += information.get(el)
        print(f"On sait que la quantité d'information transmise par le {el} est de {information.get(el)} Mo/s.")
    print(f"Donc au total, il faut un débit de {Mo_total} Mo/s")
    return Mo_total

#calculate_debit(information)


def time_to_download(debit_internet, durée_video):
    # En Mo & Secondes
    debit_stream = calculate_debit(information)
    total_file_size = debit_stream*durée_video
    print(f"La taille totale du fichier à télécharger est {debit_stream} x {durée_video} = {Mo_to_Go(total_file_size)} Go")
    total_download_size = durée_video*debit_internet
    print(f"Durant toute la durée de la vidéo, la quantité totale d'information qu'on arrive à télécharger avec le débit actuel est {durée_video} x {debit_internet} = {Mo_to_Go(total_download_size)} Go.")
    difference_to_store = total_file_size - total_download_size
    print(f"La différence à sauvegarder dans le buffer est donc {Mo_to_Go(total_file_size)} - {Mo_to_Go(total_download_size)} = {Mo_to_Go(difference_to_store)} Go")
    time_to_download_difference = Mo_to_Go(difference_to_store)*debit_internet/10/60
    print(f"Le temps nécesaire pour télécharger cette différence s'élève à {time_to_download_difference} minutes.")

print('--')
#time_to_download(100,  100*60)