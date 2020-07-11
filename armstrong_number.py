devam = True
while devam:
    sayı = input("enter a positive number")
    toplama = 0
    uzunluk = len(sayı)
    if sayı.isdigit() == True:
        for i in range(uzunluk):
            toplama += int(sayı[i]) ** (uzunluk)
        if int(sayı) == toplama:
            print(f"{sayı} is an armstrong number")
        else:
            print(f"{sayı} is not an armstrong number")
    else:
        print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
        
    devam = input("devam etmek istiyor musunuz:  y or n")
    if devam == "y":
        devam = True
    else:
        devam = False