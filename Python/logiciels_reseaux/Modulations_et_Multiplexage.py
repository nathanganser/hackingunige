import math

def calcul_capacite_transmission(largeur_de_bande, niveaux_amplitude=1, niveau_de_phase=1, niveau_de_frequence=1):
    # les différents niveaux de modulations sont des multiples de 2
    # largeur_de_bande(Hz)

    Cbaud = 2 * largeur_de_bande
    print(f'Cbaud = 2 x {largeur_de_bande} = {Cbaud}[baud]')
    N = math.log2(niveaux_amplitude*niveau_de_phase*niveau_de_frequence)
    print(f'N = log2({niveaux_amplitude} x {niveau_de_phase} x {niveau_de_frequence}) = {N} [niveaux de modulations]')
    Cbps = Cbaud * N
    print(f'Cbps = {Cbaud} x {N} = {Cbps}[bps]')

calcul_capacite_transmission(20*1000, 1,1,4)

def calcul_capacite_max_bruit(rapport_signal_bruit, largeur_de_bande):
    Cmaxbps = largeur_de_bande* math.log2(rapport_signal_bruit+1)
    print(f'Cmaxbps = {largeur_de_bande} x log2({rapport_signal_bruit} + 1) = {Cmaxbps}[bps]')
    # si la Cmaxbps est basse, on ne peut pas avoir beaucoup de niveaux de modulations

#calcul_capacite_max_bruit(67, 40*1000)

def multiplexage_frequentiel(bande_passante, allocation_bande_passante_par_utilisateur, bits_a_transmettre, multiplication_des_niveaux):
    # bande passante en Hz
    # allocation... en Hz
    # multiplication_des_niveaux: 4 x 2 x 2 par exemple
    CUsers = bande_passante/allocation_bande_passante_par_utilisateur
    print(f'CUsers = {bande_passante} / {allocation_bande_passante_par_utilisateur} = {CUsers}')
    CBaud = allocation_bande_passante_par_utilisateur * 2
    print(f'Cbaud = 2 x {allocation_bande_passante_par_utilisateur} = {CBaud}')
    Cbps = CBaud * math.log2(multiplication_des_niveaux)
    print(f'Cbps = {CBaud} x log2({multiplication_des_niveaux}) = {Cbps}[bps]')
    t = bits_a_transmettre/Cbps
    print(f't = {bits_a_transmettre} / {Cbps} = {t}[s]')
    print(f'Un utilisateur à besoin de {t * 1000}[ms] pour envoyer {bits_a_transmettre} bits.')

#multiplexage_frequentiel(20*1000, 2000, 493, 4)

def multiplexage_temporel(bande_passante, interval, bits_par_passage, multiplication_des_niveaux, bits_a_envoyer):
    # bande passante en Hz
    # interval en ms que chaque utilisateur reçoit l'entiéreté du canal
    # bits_a_envoyer est le nbr de bits que l'utilisateur peut envoyer dans l'intervalle
    # multiplication_des_niveaux: 4 x 2 x 2 par exemple
    Cbaud = bande_passante * 2
    print(f'Capacité baud = 2 x {bande_passante} = {Cbaud}')
    Cbps = Cbaud * math.log2(multiplication_des_niveaux)
    print(f'Capacité bps = {Cbaud} x log2({multiplication_des_niveaux}) = {Cbps}[bps]')
    t_en_ms = bits_par_passage / Cbps * 1000
    print(f't = {bits_par_passage} / {Cbps} = {t_en_ms}[ms]')
    print(f'Un utilisateur à besoin de {t_en_ms}[ms] pour envoyer un paquet de {bits_par_passage} bits.')
    tours = math.floor(bits_a_envoyer/8)
    bits_restants = bits_a_envoyer % 8
    temps_en_ms = tours*interval + bits_a_envoyer/Cbps*1000
    print(f'Il faut {tours} x {interval} + {bits_a_envoyer} / {Cbps/1000} = {temps_en_ms}[ms] pour envoyer {bits_a_envoyer} bits')
    utilisateurs_max = interval/t_en_ms
    print(f'Capacité Users Max = {interval} / {t_en_ms} = {utilisateurs_max} + 1 = {utilisateurs_max+1}')


multiplexage_temporel(20*1000, 4, 8, 4, 151)

def debit_effectif(largeur_de_bande, taille_de_blocs, overhead, niveaux):
    # largeur_de_bande en Hz
    # taille de blocs, 16 bits
    # sum_start_stop_bits 2+1=3
    # niveaux 8*2=16
    Cbaud = largeur_de_bande * 2
    print(f'Capacité baud = 2 x {largeur_de_bande} = {Cbaud}')
    Cbps = Cbaud * math.log2(niveaux)
    print(f'Capacité bps = {Cbaud} x log2({niveaux}) = {Cbps}[bps]')
    debit_effect = Cbps*((taille_de_blocs-overhead)/taille_de_blocs)
    print(f'Débit effectif = {Cbps} x {taille_de_blocs-overhead}/{taille_de_blocs} = {debit_effect}[bps]')

print("---")
#debit_effectif(4000, 16, 3, 8)


