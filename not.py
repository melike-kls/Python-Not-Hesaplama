vize=int(input("Vize notunu giriniz.\n"))
final=int(input("Final notunu giriniz.\n"))
ortalama=(float(vize)*0.4)+(float(final)*0.6)
print("Ortalama :{0} ".format(ortalama))
if(ortalama<40):
      print("Kaldınız")
else:
      print("Geçtiniz")
