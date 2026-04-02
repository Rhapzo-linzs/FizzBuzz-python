print("====PROGRAM FIZZBUZZ====")

#INPUT USER
awal = int(input("masukan angka awal :"))
akhir = int(input("masukan angka akhir :"))

print ("\nHasil FizzBuzz:\n")

for i in range(awal, akhir + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)