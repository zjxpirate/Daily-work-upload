

input = "2276696"

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')



def phone_mnemonic(phone_number):
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            # All digits are processed, so add partial_mnemonic to mnemonic.
            # (We add a copy since subsequent calls modify partial_mnemonic).
            mnemonics.append(''.join(partial_mnemonic))
        else:
            # Try all possible characters for this digit.
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)


    mnemonics, partial_mnemonic = [], [0] * len(phone_number)
    phone_mnemonic_helper(0)

    return mnemonics



result = phone_mnemonic(input)

print(result)



