def prime_checker(number):
  for num in range(2, number):
    if number % num == 0:
      return print("It's not a prime number.")
  return print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
