import random
secret = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("حدس بزن (1-100): "))
    tries += 1

    if guess < secret:
        print("برو بالاتر")
    elif guess > secret:
        print("بیا پایینتر")
    else:
        print(f"آفرین! در {tries} تلاش درست حدس زدی")
        break
