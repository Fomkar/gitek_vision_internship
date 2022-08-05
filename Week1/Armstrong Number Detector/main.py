"""
An Armstrong Number is a number that when you raise each digit of the number to 
the power of the number of digits and then add them up you get the original number.

Example:
    153 = (1^3) + (5^3) + (3^3)
"""

def ArmstrongDetector(number, number_of_digits):
    original_number = number
    digits_sum = 0
    while number > 0:
        digit = number % 10
        digits_sum += digit ** number_of_digits
        number //= 10
    print(f"{original_number} is {'an Armstrong Number.' if (original_number == digits_sum) else 'not an Armstrong Number.'}")
        

while True:
    try:
        number = int(input("[User]: "))
        if number < 0:
            print("Please Enter Nonnegative Integer...")
        else:
            ArmstrongDetector(number, len(str(number)))
            try_again = input("Do You Want Try Another Number [Y/N]: ")
            if (try_again == 'Y') or (try_again == 'y'):
                print("Detector Restarting...")
                continue
            elif (try_again == 'N') or (try_again == 'n'):
                print("Logging Out From Detector...")
                break
            else:
                print("Invalid Answer, Logging Out From Detector...")
                break
    except ValueError:
        print("Invalid Character, Please Enter a Valid Number...")