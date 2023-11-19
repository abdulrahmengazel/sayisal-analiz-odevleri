import Newton_Raphson_metodu
import Ikiye_Bolme_metodu1
import Ikiye_Bolme_metodu2

print("********************************")
print("********************************")
print("Programa Hoş Geldiniz")
print("********************************")
print("********************************")
print("1.f(x) = 4*e^(- X / 2)-X")
print("2.f(x)=X^3 − 2*X^2 − 5 ")
print("3.f(x)=X^3 + 4*X^2 − 10 = 0")
print("********************************")
print("********************************")
fun =int(input("lutfan bir funksiyon seşiniz  : "))


if (fun == 1) :
   x0=int(input("lutfan başlangıç değer giriniz : "))
   print ( "********************************" )
   iterasyon = int ( input ( "Kaç iterasyon hesaplamakistediğinizi girin : " ) )
   Newton_Raphson_metodu.newton_raphson(x0,iterasyon)

elif(fun == 2) :
    ilk=int(input("lutfan  aralığındaki ilk değer girin"))
    print ( "********************************" )
    son=int(input("lutfan  aralığındaki son değer girin"))
    print ( "********************************" )
    iterasyon = int ( input ( "Kaç iterasyon hesaplamakistediğinizi girin : " ) )
    Ikiye_Bolme_metodu1.İterasyonlarHesaplanma(ilk,son,iterasyon)

elif(fun == 3) :
    ilk=int(input("lutfan  aralığındaki ilk değer girin"))
    print ( "********************************" )
    son=int(input("lutfan  aralığındaki son değer girin"))
    print ( "********************************" )
    iterasyon = int ( input ( "Kaç iterasyon hesaplamakistediğinizi girin : " ) )
    Ikiye_Bolme_metodu2.İterasyonlarHesaplanma(ilk,son,iterasyon)
