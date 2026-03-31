#movement vesmirne lode
while True:
    print("Zadejte input: ")
    inpu = input()
    if inpu == "d":
        print("Lod se pohybuje doprava.")
    elif inpu == "a":
        print("Lod se pohybuje doleva.")

#strileni

    elif inpu == "f":
        print("Lod vystřelila.")

#puziti powerup

    elif inpu == "e":
        print("Lod použila powerup.")

#ukonceni hry

    elif inpu == "q":
        print("Hra ukončena.")
        break