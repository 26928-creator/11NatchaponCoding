print("โปรแกรมเกมทายเลข")

import random

target = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("เดาตัวเลขระหว่าง 1-100: "))
    attempts += 1

    if guess > target:
        print("มากไปหน่อย")
    elif guess < target:
        print("น้อยไปหน่อย") 
    else:
        print(f"ถูกต้อง! คุณใช้โอกาส {attempts} ครั้ง")
        break