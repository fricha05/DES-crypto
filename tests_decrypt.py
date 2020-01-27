from DES import *

# Pour tester, changer le nom du fichier et de la clé
file1=open("Messages/Chiffrement_DES_de_1.txt", "r")
key1=open("Messages/Clef_de_1.txt", "r")
key1Txt = str(key1.read())
print(key1Txt)
key1List = []
for c in key1Txt:
    key1List.append(int(c))
key1List = paquets_n_bits(key1List, 8)
print(key1List)

file1Txt = file1.read()
file1Bin = conv_bin(file1Txt)
file1List = []
for c in file1Bin:
    file1List.append(int(c))

test_decrypt1 = dechiffrement(file1List, key1List)



print(nib_vnoc(str(concat_clefs(test_decrypt1)).strip('[]').replace(', ', '')))

file1.close()
key1.close()