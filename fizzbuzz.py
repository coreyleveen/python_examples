def fizzbuzz():
    for n in range(100):
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 5 == 0:
            print("Buzz")
        elif n % 3:
            print("Fizz")
        else:
            print(n)

fizzbuzz()
