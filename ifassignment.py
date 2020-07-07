isim = str.capitalize(input("sahip adın nedir? :"))
isim_liste = {"Joseph": "1234", "Tom": "5678", "Mark" : "1357"}
if (isim in isim_liste):
    parola = isim_liste[isim]
    print(f"Merhaba {isim} patron parolan: {parola}")
else:
    print(f"bekleme yapma {isim} devam et")