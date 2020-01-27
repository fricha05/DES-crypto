import operator
from Bonus.ConvAlphaBin import *

IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
IP_INV = [
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25,
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1,  58, 50, 42, 34, 26, 18,
    10, 2,  59, 51, 43, 35, 27,
    19, 11, 3,  60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14, 6,  61, 53, 45, 37, 29,
    21, 13, 5,  28, 20, 12, 4
]
PC2 = [
    14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]
 
E  = [
    32, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

S = [
        [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
        [0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
        [4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
        [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]
    ], [
        [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
        [3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
        [0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
        [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9] 
    ],[
        [10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
        [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
        [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
        [1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12] 
    ],[
        [7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
        [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
        [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
        [3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]
    ],[
        [2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
        [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
        [4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
        [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]
    ],[
        [12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
        [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
        [9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
        [4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]
    ],[
        [4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
        [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
        [1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
        [6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]
    ],[
        [13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
        [1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
        [7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
        [2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]
    ]

bigKey = [
    [0,1,0,1,1,1,1,0],
    [0,1,0,1,1,0,1,1],
    [0,1,0,1,0,0,1,0],
    [0,1,1,1,1,1,1,1],
    [0,1,0,1,0,0,0,1],
    [0,0,0,1,1,0,1,0],
    [1,0,1,1,1,1,0,0],
    [1,0,0,1,0,0,0,1]
]

#crée les 16 sous clés à partir de k
def creation_sous_cles_utiles(key):
    res = []
    for row in range(len(key)) :
        new = []
        for e in range(len(key[row])-1) :
            new.append(key[row][e])
        res.append(new)
    return res

# reductedKey = creation_sous_cles(bigKey)
# bigKey
# reductedKey

#concatène tous les éléments d'une clé
def concat_clefs(keys):
    res = []
    for row in keys :
        res.extend(row)
    return res

# concat_clefs(reductedKey)

#prends la clé concaténée e et applique la permutation f
def permutation_generale(e, f):
    res = []
    for pos in range (len(f)) :
        res.append(e[f[pos]-1])
    return res

#separe une cle en 2 cle gauche et droites
def split_key(key):
    res = []
    left = []
    right = []
    size = len(key)
    for i in range(size//2):
        left.append(key[i])
    for i in range(size//2, size):
        right.append(key[i])
    res.append(left)
    res.append(right)
    return res

# splitted_key = split_key(permutated_key)

#décale la clé de n bits vers la gauche
def decalage_gauche_par_n_bits(n, key):
    tmp = []
    for pos in range (len(key)) :
        if(pos == len(key)-1):
            tmp.append(key[0])
        else :
            tmp.append(key[pos+n])
    return tmp

def generation_sous_clefs(bigKey, left, right):
    sous_clefs = []
    for ronde in range(16):
        left = decalage_gauche_par_n_bits(1, left)
        right = decalage_gauche_par_n_bits(1, right)
        k = permutation_generale(concat_clefs([left, right]), PC2)
        sous_clefs.append(k)
    return sous_clefs

# generation_sous_clefs(bigKey, splitted_key[0], splitted_key[1])



def sous_clefs_depuis_cle_complete(fullKey):
    # keys = creation_sous_cles_utiles(fullKey)
    cp1_key = permutation_generale(concat_clefs(fullKey), PC1)
    cp1_left = split_key(cp1_key)[0]
    cp1_right = split_key(cp1_key)[1]
    res = generation_sous_clefs(fullKey, cp1_left, cp1_right)
    return res

# print("Sous clefs : \n" + str(sous_clefs_depuis_cle_complete(bigKey)))
keys = sous_clefs_depuis_cle_complete(bigKey)

M = [
    1,1,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,
    1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,0,0,1,0,
    1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,1,
    0,0,1,1,1,0,1,0,1,1,0,1,1,1,1,1
]

def message_divider(m):
    blocs = []

    full_paquets_count = len(m)//64
    for i in range(full_paquets_count+1) :
        new = []
        for j in range(64):
            if( i*64+j < len(m) ):
                new.append(m[i*64+j])
            else:
                new.append(0)
        blocs.append(new)
    return blocs

def paquets_n_bits(e, n):
    res = []
    new = []
    for j in range(len(e)):
        if(j%n==0):
            if(j!=0):
                res.append(new)
            new = []
        new.append(e[j])
    res.append(new)
    return res

def ou_exclusif(a, b):
    res = []
    for i in range(len(a)):
        res.append(operator.xor(a[i], b[i]))
    return res

def binary_to_decimal(n):
    return int(n,2)

def decimal_to_binary(n):
    return bin(n).replace("0b","")

def replace_bloc_with_S(b, s):
    ligne = int(binary_to_decimal(str(b[0]) + str(b[5])))
    colonne = int(binary_to_decimal(str(b[1]) + str(b[2]) + str(b[3]) + str(b[4])))
    tmp = decimal_to_binary(s[ligne][colonne])
    res = []
    while(len(tmp) + len(res) < 4):
        res.append(0)
    for c in str(tmp):
        res.append(int(c))
    return res


def ronde(bloc, key):
    splitted = split_key(bloc)
    G = splitted[0]
    D = splitted[1]
    ED = permutation_generale(D, E)
    XOR = ou_exclusif(ED, key)
    XOR = paquets_n_bits(XOR, 6)
    msg = []
    for b in range(len(XOR)):
        msg.append(replace_bloc_with_S(XOR[b], S[b]))
    r = concat_clefs(msg)
    r = permutation_generale(r, P)
    newD = ou_exclusif(r, G)
    newG = D
    return concat_clefs([[newG], [newD]])


def chiffrement(m, fullKey):
    keys = sous_clefs_depuis_cle_complete(fullKey)
    msg = message_divider(m)
    res = []
    for i in range(len(msg)):
        p = permutation_generale(msg[i], IP)
        for r in range(16):
            p = concat_clefs(ronde(p, keys[r]))
        res.append(permutation_generale(p, IP_INV))
    return res

def rondeDecrypt(bloc, key):
    splitted = split_key(bloc)
    D = splitted[0]
    G = splitted[1]
    ED = permutation_generale(D, E)
    XOR = ou_exclusif(ED, key)
    XOR = paquets_n_bits(XOR, 6)
    msg = []
    for b in range(len(XOR)):
        msg.append(replace_bloc_with_S(XOR[b], S[b]))
    r = concat_clefs(msg)
    r = permutation_generale(r, P)
    newD = ou_exclusif(r, G)
    newG = D
    return concat_clefs([[newD], [newG]])

def dechiffrement(m, fullKey):
    keys = sous_clefs_depuis_cle_complete(fullKey)
    msg = message_divider(m)
    res = []
    for i in range(len(msg)):
        p = permutation_generale(msg[i], IP)
        for r in range(16):
            p = concat_clefs(rondeDecrypt(p, keys[15 - r]))
        res.append(permutation_generale(p, IP_INV))
    return res

cryptedM = concat_clefs(chiffrement(M, bigKey))

print("M in binary : " + str(M).strip('[]').replace(', ', ''))

print("M : " + nib_vnoc(str(M).strip('[]').replace(', ', '')))

print("cryptedM : " + str(cryptedM).strip('[]').replace(', ', ''))

print("cryptedM in text : " + nib_vnoc(str(cryptedM).strip('[]').replace(', ', '')))

decryptedM = concat_clefs(dechiffrement(cryptedM, bigKey))

print("decryptedM : " + str(decryptedM).strip('[]').replace(', ', ''))

print("final res : " + str(nib_vnoc(str(decryptedM).strip('[]').replace(', ', ''))))