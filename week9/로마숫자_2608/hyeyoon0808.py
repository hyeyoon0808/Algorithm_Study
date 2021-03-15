import sys

input=sys.stdin.readline

def roman_to_num(s):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, '\n': 0}
        int = 0
        for i in range(len(s)):
            if i > 0 and rom[s[i]] > rom[s[i - 1]]:
                int += rom[s[i]] - 2 * rom[s[i - 1]]
            else:
                int += rom[s[i]]
        return int

def num_to_roman(number):
	result = ""
	ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	roms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
	for i in range(len(ints)):
		start = number // ints[i]
		result += roms[i] * start
		number -= ints[i] * start
	return result

a, b=input(), input()
numA=roman_to_num(a)
numB=roman_to_num(b)
total = numA+numB
print(total)
roman = num_to_roman(total)
print(roman)
