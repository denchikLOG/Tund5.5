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
