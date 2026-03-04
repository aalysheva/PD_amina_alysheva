ievade():
    sk1 = int(input("Ievadi pirmo skaitļu: "))
    sk2 = int(input("Ievadi otro skaitļu: "))
    return sk1, sk2

aprekini(sk1, sk2):
    reizinajums = sk1 * sk2
    return reizinajums

izvade(reizinajums):
    print(f"Jūsu skaitļu reizinājums: {reizinajums}")

sk1, sk2 = ievade()
rezultats = aprekini(sk1, sk2)
izvade(rezultats)
