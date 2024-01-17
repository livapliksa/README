# Ievadiet lietotāja vārdu un uzvārdu
vards = input("Ievadiet savu vārdu: ")
uzvards = input("Ievadiet savu uzvārdu: ")

# Izveidojam teksta rindiņu ar ievadīto informāciju
informacija = f"Vārds: {vards}\nUzvārds: {uzvards}"

# Ierakstīt informāciju failā
with open("ziema.txt", "w") as faila_ritis:
    faila_ritis.write(informacija)

print("Informācija ir ierakstīta failā 'ziema.txt'.")