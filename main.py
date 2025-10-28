def to_decimal(number_string, orighinal_base):
    """Convert a number string from a given base to decimal (base 10).

    Args:
        number_string (str): The number in string   format.
        orighinal_base (int): The base of the input number (between 2 and 36). """
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = number_string.upper()

    value = 0
    ex = 0

    for char in number_string[::-1]:
        if char in digits[:orighinal_base]:
            ValueError(f"Character '{char}' is not valid for base {orighinal_base}")
        
    char_value = digits.index(char)
    value += char_value * (orighinal_base ** ex)
    ex += 1
    
    return value
    

def from_decimal(decimal_number, target_base):

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if decimal_number == 0:
        return "0"
    
    result = ""

    while decimal_number > 0:
        remainder = decimal_number % target_base
        result = digits[remainder] + result
        decimal_number //= target_base

    return result

def main():
    number_string = input("Enter the number to convert: ")
    orighinal_base = int(input("Enter the original base (2-36): "))
    target_base = int(input("Enter the target base (2-36): "))

    decimal_number = to_decimal(number_string, orighinal_base)
    converted_number = from_decimal(decimal_number, target_base)

    print(f"The number {number_string} in base {orighinal_base} is {converted_number} in base {target_base}.")

if __name__ == "__main__":
    main()
