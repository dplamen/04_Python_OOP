def get_primes(integers):
    for number in integers:
        prime = True
        if number <= 1:
            prime = False
        else:
            for divisor in range(2, number):
                if number % divisor == 0:
                    prime = False
                    break

        if prime:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))