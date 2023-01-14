print("hesap makinesine hoşgeldiniz")
birinci_sayı = int(input("bir sayı girin: "))
ikinci_sayı = int(input("ikinci sayı girin: "))

print("""
toplama işlemi yapmak için +
çıkarma işlemi yapmak için -
çarpma işlemi yapmak için *
bölme işlemi yapmak için /
""")

yapılmak_istenen_islem = input("yapmak istediğiniz işlemin işaretini giriniz")

if(yapılmak_istenen_islem == "+"):
    print(birinci_sayı + ikinci_sayı)
elif(yapılmak_istenen_islem == "-" ):
    print(birinci_sayı - ikinci_sayı)
elif(yapılmak_istenen_islem == "*"):
    print(birinci_sayı * ikinci_sayı)
elif(yapılmak_istenen_islem == "/" ):
    print(birinci_sayı / ikinci_sayı)
    
else:
    print ("Böyle bir işlem bulanamamıştır, lütfen tekrar deneyiniz..")
