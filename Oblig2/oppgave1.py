#  If and else

num = int(input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall:"))

if num == 42:
    print("Det stemmer, meningen med livet er 42!")
elif 30 <= num <= 50:   # and num != 42:
    print("Nærme, men feil.")
else:
    print("FEIL!")

# Line 7: This is a chained comparison. Simplifies alternative code like #  num >= 30 and num <=50
# Feedback on this task from teacher: Since elif runs when if does not, this means that and num != 42 is obsolete.
