class Romnum :




    def change (self,arab):
        arab = str(arab)
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "IIX", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "XXC", "CX"]
        hundr = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "CCM", "CM"]

        while len(arab) < 5:
            arab = "0" + arab
            print(int(arab[-4]) * "M" + hundr[int(arab[-3])] + tens[int(arab[-2])] + ones[int(arab[-1])])




l1= Romnum()
l2= Romnum()

l1.change(123)
l2.change(1254)


