def to_decimal(number_string, original_base):
    """Convert a number string from a given base to decimal (base 10)."""

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = number_string.upper()

    value = 0
    exponent = 0

    for char in number_string[::-1]:
        if char not in digits[:original_base]:
            raise ValueError(f"Character '{char}' is not valid for base {original_base}")
        
        char_value = digits.index(char)
        value += char_value * (original_base ** exponent)
        exponent += 1

    return value


def from_decimal(decimal_number, target_base):
    """Convert a decimal number to a given target base (2–36)."""

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
    original_base = int(input("Enter the original base (2-36): "))
    target_base = int(input("Enter the target base (2-36): "))

    decimal_number = to_decimal(number_string, original_base)
    converted_number = from_decimal(decimal_number, target_base)

    print(f"The number {number_string} in base {original_base} is {converted_number} in base {target_base}.")


if __name__ == "__main__":
    main()
