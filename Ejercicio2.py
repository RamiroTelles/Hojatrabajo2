print("Como te llamas?")
nombre = input()
print("H o M(Hombre o Mujer)?")
genero = input()

if genero.lower() == "m":
    if nombre.lower() < "m":
        print("Estas en el grupo A")
    else:
        print("Estas en el grupo B")

if genero.lower() == "h":
    if nombre.lower() > "n":
        print("Estas en el grupo A")
    else:
        print("Estas en el grupo B")


print("Creditos:")
print("Ramiro Agustín Télles Carcuz")
print("CUI: 3057252030301")
print("Carnet: 202010044")