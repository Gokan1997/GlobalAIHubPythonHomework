
FirstName=(input("Adınızı giriniz:"))
LasttName=(input("Soyadınızı giriniz:"))
Age=(int(input("yaşınızı giriniz:")))
DateOfBirth=(int(input("Doğum Yılınızı giriniz:")))
Information_List=[FirstName,LasttName,Age,DateOfBirth]
for i in Information_List:
    print(i)
if Age < 18:
    print("You can't go out because ıt so dangerous")
else:
    print ("You can go out the street")


