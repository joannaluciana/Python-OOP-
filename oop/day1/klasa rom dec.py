class Romnum :
    def rom2dec(self, roman):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dec = 0
        for i in range(len(roman)):
            if i > 0 and rom_val[roman[i]] > rom_val[roman[i - 1]]:
                dec += rom_val[roman[i]] - 2 * rom_val[roman[i - 1]]
            else:
                dec += rom_val[roman[i]]
        return dec

x=Romnum()

print(x.rom2dec('MMMCMLXXXVI'))
'MMMCMLXXXVI'
