def fizz_buzz(numbers):
    data = []
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            data.append("FizzBuzz")
        elif num % 3 == 0:
            data.append("Fizz")
        elif num % 5 == 0:
            data.append("Buzz")
        else:
            data.append(None)
    return data
