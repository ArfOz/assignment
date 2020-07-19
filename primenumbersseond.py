sayı = int(input("herhangi bir sayı giriniz"))

prime_list = []
notprime_list = []
if sayı < 0:
    print("pozitif sayı giriniz")
elif sayı==0 or sayı ==1:
    print("sayı asal değildir")
else:
    for t in range(2,(sayı+1)):
        sayaç = 0
        for i in range(2,(t)):
            if (t % i) != 0:
                sayaç = sayaç        
            elif (t % i) == 0:
                sayaç += 1
        if sayaç >= 1:
            prime_list.append(t)
        else:
            notprime_list.append(t)

            
        
print("prime_list" ,list(set(prime_list)))
print("not prime list",  list(set(notprime_list)))