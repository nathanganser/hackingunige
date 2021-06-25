import math


# la première et dernière adresse d'un réseau est réservée (première pour définir le réseau, dernière pour broadcast


def decimaltobinary(num):
    return bin(num).replace("0b", "")


def binarytodecimal(binary):
    return int(binary,2)

def create_string(what, how_many):
    res = ""
    for el in range(0, how_many, +1):
        res = res + what
    return res


def create_subnet_range(address, mask, subnet_mask):
    print(f'creating subnet ranges for address {convert_bin_to_ip(address)} for original mask {mask} and subnet mask {subnet_mask}')
    address_start = address[0:subnet_mask] + create_string("1", mask-subnet_mask) + address[mask:len(address)-1] + "1"
    print(address_start)
    address_end = address[0:subnet_mask] + create_string("1", mask-subnet_mask) + create_string("1", 32-mask-1) + "0"
    print(address_end)
    print(f'Plage d’adresses IP allouée: {convert_bin_to_ip(address_start)} - {convert_bin_to_ip(address_end)}')
    address_dif = address[0:mask] + create_string("1", 32 - mask)
    print(f'Adresse de diffusion: {convert_bin_to_ip(address_dif)}')
    return address_start, address_end



def convert_ip_to_bin(ip):
    res = ""
    list = ip.split(".")
    for el in list:
        val = decimaltobinary(int(el))
        while len(val) < 8:
            val = "0" + val
        res += val
    return res

def convert_bin_to_ip(bin_ip):
    res = ""
    for octet in range(0, len(bin_ip), +8):
        res += str(int(bin_ip[octet:octet+8],2))
        res += "."
    return res[0: len(res)-1]


def convert_mask_to_bin(mask):
    res = ""
    for el in range(0, mask, +1):
        res = res + "1"
    for el in range(0, 32 - mask, +1):
        res = res + "0"
    return res


def detect_class(bin_ip):
    if bin_ip[0:1] == "0":
        print('Class A')
        #print('En tout il y a 26 network IDs attribuables avec un total de 16,777,214 host IDs disponibles pour chacun')
        class_identifier = bin_ip[0:1]
        network_id = bin_ip[1:8]
        host_id = bin_ip[8:32]
    if bin_ip[0:2] == "10":
        print('Class B')
        #print("En tout il y a 16,384 network IDs attribuables avec un total de 65,534 host IDs disponibles pour chacun")
        class_identifier = bin_ip[0:2]
        network_id = bin_ip[2:16]
        host_id = bin_ip[16:32]
    if bin_ip[0:3] == "110":
        print('Class C')
        #print("En tout il y a 2,097,152 network IDs attribuables avec un total de 254 host IDs disponibles pour chacun")
        class_identifier = bin_ip[0:3]
        network_id = bin_ip[3:24]
        host_id = bin_ip[24:32]
    print(f' network_id: {network_id}')
    print(f' host_id: {host_id}')
    return class_identifier, network_id, host_id


def build_reseau(departments):
    addresses_used = 0
    # make sure to count the +2 addresses that are required and can't be used for each subnet/sous-reseau
    # make sure to count +1 for the router and don't count switches!
    address_count = 0
    for dep in departments:
        address_count += dep
    mask = int(32 - math.log2(address_count))
    if mask % 2 != 0:
        mask -= 1
    final_mask = mask

    print(f'{address_count} addresses needed')
    print(f'final mask is /{final_mask}')
    if address_count > 254:
        if address_count > 65534:
            addressclass = "A"
            addressEx = "24.74.64.0"
        else:
            addressclass = "B"
            addressEx = "170.98.64.0"
    else:
        addressclass = "C"
        addressEx = "194.194.141.0"
    print(f'the address needs to be an {addressclass} address like {addressEx}')
    print('What is the address?')
    string_address = "172.10.0.0" #input()
    address = convert_ip_to_bin(string_address)
    print('-----')
    detect_class(address) # convert_ip_to_bin(input())
    print('-----')
    print(f'address: {address}')
    mask = convert_mask_to_bin(final_mask)
    print(f'mask ad: {mask}')

    espace = 32 - final_mask
    given_mask = final_mask
    for dep in departments:
        while 2 ** espace >= dep:
            espace -= 1
            given_mask += 1
        espace += 1
        given_mask -= 1
        print(' ')
        print(f'department with {dep} people will require 2^{espace} ({2**espace}) addresses ')
        print(f'Adresse de sous-réseau: {convert_bin_to_ip(address)}/{given_mask}')
        address_start = address[0:given_mask] + address[given_mask:len(address) - 1] + "1"
        address_end = address[0:given_mask] + create_string("1",32 - given_mask - 1) + "0"
        print(f'En binaire: {address_start} --> {address_end}')
        #print(f'Plage d’adresses IP allouée: {convert_bin_to_ip(address_start)} - {convert_bin_to_ip(address_end)}')
        address_dif = address[0:given_mask] + create_string("1", 32 - given_mask)
        #print(f'Adresse de diffusion: {convert_bin_to_ip(address_dif)}')

        start, end = create_subnet_range(address, given_mask, given_mask)
        addresses_used += how_many_ips(start, end) + 2
        address = address[0:given_mask - 1] + "1" + address[given_mask:len(address)]
        espace -= 1
        given_mask += 1
    print(f'Le réseau utilise {addresses_used} adresses')
    addresses_utilisable = analyse_ip(address, 16)
    print(f'Il reste {addresses_utilisable} - {addresses_used} = {addresses_utilisable-addresses_used} adresses à attribuer')


def convert_ip_to_address_reseau(ip, masque):
    class_identifier, network_id, reseau_id = detect_class(ip)
    ip = class_identifier + network_id + reseau_id
    ip_fix = ip[0:masque]
    ip_to_change = ip[masque:len(ip)]
    return ip_fix + ip_to_change.replace('1','0')

def analyse_ip(ip, masque):
    address_reseau = convert_ip_to_address_reseau(ip, masque)
    print('-- ANALYSE --')
    masque_en_ip = convert_bin_to_ip(convert_mask_to_bin(masque))
    print(f'Masque réseau {masque_en_ip}')
    print(f'Addresse réseau: {convert_bin_to_ip(address_reseau)}')
    print(f'Hôtes possibles: {2**(len(ip)-masque)-2}')
    detect_class(address_reseau)
    create_subnet_range(address_reseau, masque, masque)
    return 2**(len(ip)-masque)


#ipAlice = convert_ip_to_bin("214.71.0.0")
#analyse_ip(ipAlice, 24)
#ipBob = convert_ip_to_bin("144.77.0.0")
#analyse_ip(ipBob, 16)

def same_reseau(ip1, masque1, ip2, masque2):
    if convert_ip_to_address_reseau(ip1, masque1) == convert_ip_to_address_reseau(ip2, masque2):
        print(f'{convert_bin_to_ip(ip1)} et {convert_bin_to_ip(ip2)} sont dans le même réseau')
        return True
    else:
        return False

def how_many_ips(ip1, ip2):
    return binarytodecimal(ip2)-binarytodecimal(ip1)+1

build_reseau([1047*1.2+4, 42*1.2+4, 10*1.2+4+1, 8+4])
#analyse_ip(convert_ip_to_bin("144.77.0.0"), 16)