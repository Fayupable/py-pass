# import random
# import string

# def rastgele_sifre_olustur(uzunluk=25):
#     karakterler = string.ascii_letters + string.digits + string.punctuation
#     sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
#     return sifre

# sifre = rastgele_sifre_olustur()
# print("Oluşturulan Şifre:", sifre)

import random
import string

def rastgele_sifre_olustur(uzunluk=25):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

def sifre_kaydet(hesap, sifre):
    with open("sifreler.txt", "a") as dosya:
        dosya.write(f"Hesapı: {hesap}\nŞifre: {sifre}\n{'-'*30}\n")

def hesap_kontrol(hesap, yeni_sifre):
    with open("sifreler.txt", "r") as dosya:
        icerik = dosya.read()
        hesaplar = icerik.split('---')
        for hesap_bilgisi in hesaplar:
            if f"Hesap: {hesap}" in hesap_bilgisi:
                eski_sifre = hesap_bilgisi.split("Şifre: ")[1].split("\n")[0]
                if yeni_sifre == eski_sifre:
                    return True
    return False

while True:
    hesap = input("Hesap adını girin: ")

    if hesap_kontrol(hesap, rastgele_sifre_olustur()):
        print(f"{hesap} isimli hesabın şifresi başka bir hesabın şifresiyle aynı. Yeni bir şifre oluşturuluyor.")
        yeni_sifre = rastgele_sifre_olustur()
        print("Yeni Oluşturulan Şifre:", yeni_sifre)
        sifre_kaydet(hesap, yeni_sifre)
    else:
        yeni_sifre = rastgele_sifre_olustur()
        print("Oluşturulan Şifre:", yeni_sifre)
        sifre_kaydet(hesap, yeni_sifre)
        break

