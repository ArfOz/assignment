yaş = str.capitalize(input("75 yaş üstü sigara bağımlısı mısınız:"))
kronik = str.capitalize(input("ciddi kronik rahatsızlığınız var mı:"))
bağışıklık = str.capitalize(input("bağışıklık sisteminiz güçlü mü:"))
if (yaş =="Yes")and (kronik == "Yes" )and (bağışıklık == "Yes"):
    print("riskli gruptasın dikkat et")
elif (yaş =="Yes") and (kronik == "Yes" ) and (bağışıklık == "No"):
    print("riskin biraz fazla")
elif(yaş =="Yes") and (kronik == "No" ) and (bağışıklık == "No"):
    print("Yaşın var dikkat et")
elif (yaş =="No") and (kronik == "Yes" ) and (bağışıklık == "Yes"):
    print("gençsin ama dikkat et")
else :
    print("rahat ol sıkıntı yok")
