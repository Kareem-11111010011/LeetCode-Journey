class Solution:
    def romanToInt(self, s: str) -> int:
        output_integer = 0
        special_roman_numeral = {"IV": " 4 ", "IX": " 9 ", "XL": " 40 ", "XC": " 90 ", "CD": " 400 ", "CM": " 900 "} 
        regular_roman_numerals = {"I": " 1 ", "V": " 5 ", "X": " 10 ", "L": " 50 ", "C": " 100 ", "D": " 500 ", "M": " 1000 "}
        for special_roman_numeral, value in special_roman_numeral.items():
            if special_roman_numeral in s:
                s = s.replace(special_roman_numeral, value)
        for roman_numeral, value in regular_roman_numerals.items():
            if roman_numeral in s:
                s = s.replace(roman_numeral, value)
        for num in s.split():
            output_integer += int(num)
        return output_integer
        
                
            
            

