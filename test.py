from befehls_verlauf import BefehlsVerlauf

b = BefehlsVerlauf(5)

for i in range(7):
    b.append(i)

print(b.befehle)