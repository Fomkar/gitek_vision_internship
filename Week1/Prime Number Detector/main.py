"""
A prime number (or a prime) is a natural number greater than 1 that is not a 
product of two smaller natural numbers. A natural number greater than 1 that 
is not prime is called a composite number.
"""

def PrimeDetector(number):
    isPrime = True
    for i in range(2, number):
        if (number % i) == 0:
            isPrime = False
            break
    print(f"[Detector]: {'Prime Number' if isPrime else 'Composite Number.'}")

while True:
    try:
        number = int(input("[User]: "))
        if number < 2:
            print("Please Enter Bigger Integer Value than 1...")
        else:
            PrimeDetector(number)
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