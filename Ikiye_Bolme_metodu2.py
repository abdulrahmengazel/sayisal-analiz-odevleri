#𝑥3 + 4𝑥2 − 10 = 0 denkleminin [1,2] aralığında kökünü ikiye
#bölme metodu ile 4 iterasyonda gerçekleştiriniz. Bulunan çözümün
#kodunu hazır fonksiyon kullanmadan yazınız

def f(x):
    return x ** 3 + 4 * x ** 2 - 10

def İlkSOnhesaplanam(ilk,son):
     if (f(ilk) * f(son) < 0 ):
         return (ilk+son)/2
     else:
         print("mabarref ")


def  İterasyonlarHesaplanma(ilk,son,sİterasyon):
    iterasyon = İlkSOnhesaplanam(ilk,son)

    for i in range(0,sİterasyon):
        print ( f"{i + 1} iterasyon = {iterasyon}" )
        if f (iterasyon) * f ( ilk ) < 0 :
            son = iterasyon
        else :
            ilk = iterasyon

        iterasyon = (ilk + son)/2

