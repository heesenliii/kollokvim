#1) salam adlı funksiya yaradın ki, heç bir arqument almadan sadəcə "Salam, Dünya!" çap etsin.
def salam():
    print("Salam, Dünya!")
#2) kub_hesabla adlı funksiya yaradın ki, bir rəqəm (n) qəbul etsin və onun kubunu qaytarsın.
def kub_hesabla(n):
    return n ** 3
#3) birlesdir adlı funksiya yaradın ki, iki söz qəbul etsin və onları boşluqla birləşdirib qaytarsın.
def birlesdir(söz1, söz2):
    return söz1 + " " + söz2
#4) cap_et adlı funksiya yaradın ki, bir listi arqument olaraq alsın və listin hər elementini for ilə çap etsin.
def cap_et(liste):
    for element in liste:
        print(element)
#5) toplam adlı funksiya yaradın ki, istənilən sayda rəqəmi (*args) qəbul edib onların cəmini qaytarsın.
def toplam(*args):
    return sum(args)
#6) ortalama adlı funksiya yaradın ki, istənilən sayda rəqəmi (*args) qəbul edib onların ortalamasını qaytarsın (əgər heç bir rəqəm yoxdursa, "Rəqəm yoxdur" qaytarsın).
def ortalama(*args):
    if len(args) == 0:
        return "Rəqəm yoxdur"
    return sum(args) / len(args)
#7) adlar_rəqəmlər adlı funksiya yaradın ki, istənilən sayda ad və rəqəm cütünü (**kwargs) qəbul edib hər cütü çap etsin (məsələn, "ad: bir, rəqəm: 1").
def adlar_rəqəmlər(**kwargs):
    for ad, rəqəm in kwargs.items():
        print(f"ad: {ad}, rəqəm: {rəqəm}")
#8) tip_yoxla adlı funksiya yaradın ki, bir dəyər qəbul edib onun tipini yoxlasın: "mətn", "rəqəm", "başqa" çap etsin.
def tip_yoxla(dəyər):
    if isinstance(dəyər, str):
        print("mətn")
    elif isinstance(dəyər, (int, float)):
        print("rəqəm")
    else:
        print("başqa")
#9) yas_kateqoriya adlı funksiya yaradın ki, input()/readline() ilə yaş soruşsun, 18-dən aşağıysa "Gənc", yuxarıdrsa "Yetkin" çap etsin.
def yas_kateqoriya():
    yaş = int(input("Yaşınızı daxil edin: "))
    if yaş < 18:
        print("Gənc")
    else:
        print("Yetkin")
#10) soz_uzunluq adlı funksiya yaradın ki, input()/readline() ilə istifadəçidən söz alsın və onun uzunluğunu çap etsin.
def soz_uzunluq():
    söz = input("Bir söz daxil edin: ")
    print(f"Sözün uzunluğu: {len(söz)}")
