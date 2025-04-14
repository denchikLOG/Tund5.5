#5.5
#1 kool

# def kool():
#     opilased,puudumised=[],[]
#     for _ in range(int(input("Mitu õpilast lisada? "))):
#         nimi=input("Õpilase nimi: ")
#         puud=int(input("Puudumiste arv: "))
#         opilased.append(nimi)
#         puudumised.append(puud)
#     while True:
#         print("\n1 - Parimad õpilased\n2 - Sorteeri puudumiste järgi\n3 - Komisjon (>50 puudumist)\n4 - Võta maha (>100 puudumist)\n5 - Otsi õpilast\n0 - Välju")
#         valik=input("Valik: ")
#         if valik=="1":
#             n=int(input("Mitu parimat näidata? "))
#             for nimi,puud in sorted(zip(opilased,puudumised),key=lambda x:x[1])[:n]:
#                 print(f"{nimi} - {puud}")
#         elif valik=="2":
#             for nimi,puud in sorted(zip(opilased,puudumised),key=lambda x:x[1]):
#                 print(f"{nimi} - {puud}")
#         elif valik=="3":
#             for nimi,puud in zip(opilased,puudumised):
#                 if puud>50:
#                     print(f"{nimi} - {puud}")
#         elif valik=="4":
#             u_opilased,u_puudumised=[],[]
#             for nimi,puud in zip(opilased,puudumised):
#                 if puud<=100:
#                     u_opilased.append(nimi)
#                     u_puudumised.append(puud)
#                 else:
#                     print(f"Mahavõetud: {nimi} - {puud}")
#             opilased=u_opilased
#             puudumised=u_puudumised
#         elif valik=="5":
#             nimi=input("Sisesta nimi: ")
#             if nimi in opilased:
#                 print(f"{nimi} - {puudumised[opilased.index(nimi)]}")
#             else:
#                 print("Õpilast ei leitud.")
#         elif valik=="0":
#             break
#         else:
#             print("Tundmatu valik.")
# kool()
#4 pood
# def pood():
#     покупки,hinnad,ostsid=[],[],[]
#     n=int(input("Kui palju toode tahate lisada? "))
#     for _ in range(n):
#         toode=input("Toode nimi: ")
#         hind=float(input(f"Toode hind {toode}: "))
#         покупки.append(toode)
#         hinnad.append(hind)
#     while True:
#         print("\n1 -Emalda toode ja pane seda ostsid ")
#         print("2 - Pana kõik tooded ja nende hinnad A-Z")
#         print("3 - Otsi kõige oodavam-kallim toode")
#         print("4 - Otsi toode hind")
#         print("5 - Mine ära")    
#         valik=input("Mida teha?(1-5): ")
#         if valik=="1":
#             toode=input("Kirjuta toode midaa te ostsite: ")
#             if toode in покупки:
#                 index=покупки.index(toode)
#                 ostsid.append((toode,hinnad[index]))
#                 del покупки[index]
#                 del hinnad[index]
#                 print(f"{toode} on pannud ostsid .")
#             else:
#                 print(f"Toode {toode} ei leidnud.")
#         elif valik=="2":
#             print("Tooded ja hinnad A-Z:")
#             for toode,hind in sorted(zip(покупки,hinnad)):
#                 print(f"{toode} - {hind} руб.")
#         elif valik=="3":
#             if покупки:
#                 max_price=max(hinnad)
#                 min_price=min(hinnad)
#                 max_item=покупки[hinnad.index(max_price)]
#                 min_item=покупки[hinnad.index(min_price)]
#                 print(f"Kõige kallim: {max_item} - {max_price} eur.")
#                 print(f"kõige oodavaim: {min_item} - {min_price} eur.")
#             else:
#                 print("Список покупок пуст.")
#         elif valik=="4":
#             toode=input("Kirjuta toode nimi et leida hind: ")
#             if toode in покупки:
#                 print(f"Toode hind {toode}: {hinnad[покупки.index(toode)]} eur.")
#             else:
#                 print(f"toode {toode} ei leidnud.")
#         elif valik=="5":
#             break
# pood()

#7 tootajad
def tootajad():
    töötajad,sünniajad=[],[]
    n=int(input("Mitu töötajat küsitleda? "))
    for _ in range(n):
        nimi=input("Töötaja nimi: ")
        töötajad.append(nimi)
        sünniaasta=int(input(f"{nimi} sünniaasta: "))
        sünniajad.append(sünniaasta)    
    def get_age(sünniaasta):
        return 2025-sünniaasta
    def sort_by_age(item):
        return get_age(item[1])
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
            n=int(input("Näita (1 - noorimad, 2 - vanimad): "))
            sorted_employees=sorted(zip(töötajad,sünniajad),key=sort_by_age,reverse=(n==2))
            for i,(nimi,sünniaasta) in enumerate(sorted_employees[:10],1):
                print(f"{i}. {nimi} - {2025-sünniaasta} aastat")
        elif valik=="4":
            aasta=int(input("Sisesta sünniaasta: "))
            for nimi,sünniaasta in zip(töötajad,sünniajad):
                if sünniaasta==aasta:
                    print(f"{nimi} - {aasta}")
        elif valik=="0":
            print("Nägemist!")
            break
tootajad()

# #9

# import random
# def lapsed():
#     nimed,hinnad=[],[]
#     for _ in range(int(input("Mitu last lisada? "))):
#         nimi=input("Nimi: ")
#         nimed.append(nimi)
#         hinnad.append(round(random.uniform(4.0,10.0),2))
#     while True:
#         print("\n1 - Kõik lapsed (A-Z)\n2 - Parim hinne\n3 - Keskmine hinne\n4 - Laste keskmine hinne\n0 - Välju")
#         valik=input("Valik: ")
#         if valik=="1":
#             for nimi,hinne in sorted(zip(nimed,hinnad)): print(f"{nimi} - {hinne}")
#         elif valik=="2":
#             if 10.0 in hinnad: print(f"Parim hinne: {nimed[hinnad.index(10.0)]} - 10.0")
#             else: print("Parim hinne puudub.")
#         elif valik=="3":
#             print(f"Keskmine hinne: {sum(hinnad)/len(hinnad):.2f}")
#         elif valik=="4":
#             nimi=input("Sisesta lapse nimi: ")
#             if nimi in nimed:
#                 hinne=sum(hinnad[i] for i,n in enumerate(nimed) if n==nimi)/nimed.count(nimi)
#                 print(f"{nimi} keskmine hinne: {hinne:.2f}")
#             else: print(f"{nimi} pole leitud.")
#         elif valik=="0": 
#         break

# lapsed()
