sayı = int(input("herhangi bir sayı giriniz"))
sayaç = 0
if sayı < 0:
    print("pozitif sayı giriniz")
else:
    for i in range(2,(sayı+1)):
        if (sayı % i) != 0:
            sayaç = sayaç        
        elif (sayı % i) == 0:
            sayaç += 1
    if (sayı == 0) or (sayı == 1) or (sayaç > 1):
        print(f"{sayı} is not prime number")
    else:
        print(f"{sayı} is prime number")
    