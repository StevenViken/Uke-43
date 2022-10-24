
def primeCheck():
    prime_numbers = [1, 5, 6, 7, 10, 11, 19, 23, 25, 26, 31, 26, 37, 40, 43, 67, 73, 99, 101]
    truePrimeNumbers = []
    for i in range(len(prime_numbers)):
        isPrime = True
        for j in range(prime_numbers[i]):
            if isinstance(prime_numbers[i] / (j + 1), int):
                isPrime = False
        if isPrime == True:
            truePrimeNumbers.append(prime_numbers[i])
    return truePrimeNumbers

print(primeCheck())