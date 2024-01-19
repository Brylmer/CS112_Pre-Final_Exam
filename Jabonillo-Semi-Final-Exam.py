def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def display_primes(start, end):
    if start < 0:
        print("Enter a non-negative number.")
        return
    if end <= start:
        print(f"Enter a number greater than {start}.")
        return

    print(f"Prime numbers between {start} and {end}:")
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            print(num, end=" ")

if __name__ == "__main__":
    while True:
        start = int(input("Enter the start number (or 0 to terminate): "))
        
        if start == 0:
            print("Program terminated.")
            break

        end = int(input("Enter the end number: "))

        display_primes(start, end)