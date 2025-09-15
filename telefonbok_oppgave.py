#oppgave 1

telefonbok = []

Person1 = {
    "navn": "Audun",
    "nummer": 18164173
}

Person2 = {
    "navn": "Nicolai",
    "nummer": 19045254
}

telefonbok.append(Person1)
telefonbok.append(Person2)

#oppgave 2

def vis_alle():
    for person in telefonbok:
        print(f"{person['navn']}: {person['nummer']}")

# Oppgave 3
def legg_til():
    navn = input("Skriv inn navn: ")
    nummer = int(input("Skriv inn nummer: "))

    ny_person = {"navn": navn, "nummer": nummer}
    telefonbok.append(ny_person)

    print(f"{navn} ble lagt til i telefonboka.")

#oppgave 4

def søk():
    navn = input("Hvem vil du søke ettter?: ")

    for person in telefonbok:
        if person['navn'].lower() == navn:
            print(f"{person['navn']} finnes i listen")
            break
    else:
        print(f"{person} er ikke i listen")

# Oppgave 5

while True:

    # lager en variabel med navn meny som holder teksten til menyen
    meny = """
        1. vis alle 
        2. leg til 
        3. søk
        4. avsultt
    """

    print(meny) # printer ut menyen

    valg = input("Hva vil du gjøre: ")

    if valg.lower() in ["vis alle", "1"]:
        vis_alle()
    elif valg.lower() in ["leg til", "2"]:
        legg_til()
    elif valg.lower() in ["søk", "3"]:
        søk()
    elif valg.lower() in ["avsull", "exit", "4"]:
        print("avsultter programet....")
        break
    else:
        print(f"{valg} finnes ikke i menyen")

