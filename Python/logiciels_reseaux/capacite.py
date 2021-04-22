

bande_passante = 5000 #en Hz

capacite_en_baud = 2*bande_passante

n_bits_interval = 6 # 1, 2 ou 3 log2(x)

debit_max = 2 * bande_passante * n_bits_interval

print(f'debit max en bps: {debit_max}')