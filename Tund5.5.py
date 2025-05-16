# 5.5
#7 töötajad
def töötajad():
    töötajad=[]
    sünniajad=[]
    n=int(input("Mitu töötajat küsitleda? "))
    for _ in range(n):
        nimi=input("Töötaja nimi: ")
        töötajad.append(nimi)
        sünniaasta=int(input(f"{nimi} sünniaasta: "))
        sünniajad.append(sünniaasta)
    while True:
        print("\n1 - Pensionärid\n2 - Keskmine vanus\n3 - 10 nooremat/vanemat\n4 - Otsi sünniaasta järgi\n0 - Välju")
        valik=input("Valik: ")
        if valik=="1":
            for nimi,sünniaasta in zip(töötajad,sünniajad):
                if 2025-sünniaasta>=65:
                    print(f"{nimi} - {2025-sünniaasta} aastat")
        elif valik=="2":
            avg_age=sum([2025-sünniaasta for sünniaasta in sünniajad])/len(sünniajad)
            print(f"Keskmine vanus: {avg_age:.2f} aastat")
        elif valik=="3":
            n=int(input("Näita (1-noorimad, 2-vanimad): "))
            sorted_employees=sorted(zip(töötajad,sünniajad),key=lambda x: 2025-x[1],reverse=(n==2))
            for i,(nimi,sünniaasta) in enumerate(sorted_employees[:10],1):
                print(f"{i}. {nimi} - {2025-sünniaasta} aastat")
        elif valik=="4":
            aasta=int(input("Sisesta sünniaasta: "))
            for nimi,sünniaasta in zip(töötajad,sünniajad):
                if sünniaasta==aasta:
                    print(f"{nimi} - {aasta}")
                else:
                    print("On viga!")
        elif valik=="0":
            print("Nägemist!")
            break
töötajad()

####
def töötajad():
    nimed = []
    sünniajad = []
    n = int(input("Mitu töötajat küsitleda? "))
    for _ in range(n):
        nimi = input("Töötaja nimi: ")
        aasta = int(input(f"{nimi} sünniaasta: "))
        nimed.append(nimi)
        sünniajad.append(aasta)

    def vanus(aasta):
        return 2025 - aasta

    while True:
        print("\n1 - Pensionärid\n2 - Keskmine vanus\n3 - 10 nooremat/vanemat\n4 - Otsi sünniaasta järgi\n0 - Välju")
        valik = input("Valik: ")

        if valik == "1":
            for nimi, aasta in zip(nimed, sünniajad):
                if vanus(aasta) >= 65:
                    print(f"{nimi} - {vanus(aasta)} aastat")

        elif valik == "2":
            koguvanus = 0
            for aasta in sünniajad:
                koguvanus += vanus(aasta)
            keskmine = koguvanus / len(sünniajad)
            print(f"Keskmine vanus: {keskmine:.2f} aastat")

        elif valik == "3":
            valik2 = int(input("1 - Nooremat, 2 - Vanemat: "))
            andmed = list(zip(nimed, sünniajad))

            # Tavaline sorteerimine ilma lambda'ta
            for i in range(len(andmed)):
                for j in range(i + 1, len(andmed)):
                    vanus1 = vanus(andmed[i][1])
                    vanus2 = vanus(andmed[j][1])
                    if (valik2 == 1 and vanus1 > vanus2) or (valik2 == 2 and vanus1 < vanus2):
                        andmed[i], andmed[j] = andmed[j], andmed[i]

            print("Tulemused:")
            for i in range(min(10, len(andmed))):
                nimi, aasta = andmed[i]
                print(f"{i + 1}. {nimi} - {vanus(aasta)} aastat")

        elif valik == "4":
            otsitav = int(input("Sisesta sünniaasta: "))
            leitud = False
            for nimi, aasta in zip(nimed, sünniajad):
                if aasta == otsitav:
                    print(f"{nimi} - {aasta}")
                    leitud = True
            if not leitud:
                print("Sellise sünniaastaga töötajat ei leitud!")

        elif valik == "0":
            print("Nägemist!")
            break

        else:
            print("Tundmatu valik, proovi uuesti.")

töötajad()
