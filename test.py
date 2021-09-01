from befehls_verlauf import BefehlsVerlauf

input = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8, 9, 10, 10, 11, 12, 13]

anzahl = len(input) + 3

verlauf = BefehlsVerlauf(anzahl)


for elem in input:
    verlauf.append(elem)
    print(str(verlauf.lese_pointer) + ":\t\t" + str(verlauf.read()))

print("====================================================================")

for i in range(anzahl):
    print(str(verlauf.lese_pointer) + ":\t\t" + str(verlauf.read()))
    verlauf.pointer_up()