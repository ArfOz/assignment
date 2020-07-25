cümle = input("cümle giriniz:")

sayılar ={}

for i in cümle:
    sayılar[i] = cümle.count(i)
    
print(sayılar)