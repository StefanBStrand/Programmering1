#  If and else

num = int(input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall:"))

if num == 42:
    print("Det stemmer, meningen med livet er 42!")
elif num >= 30 and num <=50:
    print("Nærme, men feil.")
else:
    print("FEIL!")
