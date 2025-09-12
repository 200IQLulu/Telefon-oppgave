#oppgave 1

telefonbok = []

Person1 = {
    "navn": "Ola",
    "nummer": 18164173
}

Person2 = {
    "navn": "Kari",
    "nummer": 19045254
}

telefonbok.append(Person1)
telefonbok.append(Person2)

#oppgave 2

def vis_alle(telefonbok):
    for person in telefonbok:
        print(f"{person['navn']}: {person['nummer']}")

# Oppgave 3
def legg_til():
    navn = input("Skriv inn navn: ")
    nummer = int(input("Skriv inn nummer: "))

    ny_person = {"navn": navn, "nummer": nummer}
    telefonbok.append(ny_person)

    print(f"{navn} ble lagt til i telefonboka.")

legg_til()