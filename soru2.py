kelime=input("kelime giriniz:")
def terstenokuma(kelime):

    sag = 0
    sol = len(kelime) - 1
    while (sag < sol):
        if (kelime[sag] != kelime[sol]):
            return print("kelime[sag]" == "kelime[sol]")
            sag = sag + 1
            sol = sol - 1
        else:
            return print("kelime[sag]" != "kelime[sol]")

terstenokuma(kelime)
