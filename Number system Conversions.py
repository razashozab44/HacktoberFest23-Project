def binary_to_decimal(binary_str):
    decimal = 0
    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
    return decimal

def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def hexadecimal_to_decimal(hex_str):
    hex_str = hex_str.lower()
    decimal = 0
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    for digit in hex_str:
        decimal = decimal * 16 + hex_dict[digit]
    return decimal

def decimal_to_hexadecimal(decimal):
    if decimal == 0:
        return "0"
    hex_chars = "0123456789abcdef"
    hexadecimal = ""
    while decimal > 0:
        hexadecimal = hex_chars[decimal % 16] + hexadecimal
        decimal = decimal // 16
    return hexadecimal

def convert():
    while True:
        print("Conversion Options:")
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Hexadecimal to Decimal")
        print("4. Decimal to Hexadecimal")
        print("5. Binary to Hexadecimal")
        print("6. Hexadecimal to Binary")
        print("7. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            binary_str = input("Enter a binary number: ")
            decimal = binary_to_decimal(binary_str)
            print(f"Decimal: {decimal}")
        elif choice == '2':
            decimal = int(input("Enter a decimal number: "))
            binary_str = decimal_to_binary(decimal)
            print(f"Binary: {binary_str}")
        elif choice == '3':
            hex_str = input("Enter a hexadecimal number: ")
            decimal = hexadecimal_to_decimal(hex_str)
            print(f"Decimal: {decimal}")
        elif choice == '4':
            decimal = int(input("Enter a decimal number: "))
            hex_str = decimal_to_hexadecimal(decimal)
            print(f"Hexadecimal: {hex_str}")
        elif choice == '5':
            binary_str = input("Enter a binary number: ")
            decimal = binary_to_decimal(binary_str)
            hex_str = decimal_to_hexadecimal(decimal)
            print(f"Hexadecimal: {hex_str}")
        elif choice == '6':
            hex_str = input("Enter a hexadecimal number: ")
            decimal = hexadecimal_to_decimal(hex_str)
            binary_str = decimal_to_binary(decimal)
            print(f"Binary: {binary_str}")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    convert()
