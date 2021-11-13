class Integer:

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"
        return cls(int(value))

    @classmethod
    def from_roman(cls, roman):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(roman)):
            if i > 0 and rom_val[roman[i]] > rom_val[roman[i - 1]]:
                int_val += rom_val[roman[i]] - 2 * rom_val[roman[i - 1]]
            else:
                int_val += rom_val[roman[i]]
        return cls(int_val)

    @classmethod
    def from_string(cls, string):
        if not isinstance(string, str):
            return "wrong type"
        try:
            return cls(int(string))
        except:
            return "wrong type"


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
