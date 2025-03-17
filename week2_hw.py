import random

number = random.randint(1,100)
count  = 0

while True:
    guess = int(input("숫자를 입력하세요: "))

    count+=1

    if guess > number:
        print("입력하신 값은 정답보다 작은수 입니다.")
    elif guess < number:
        print("입력하신 값은 정답보다 큰 수 입니다.")
    else:
        print(f"{count}번 만에 맞췄습니다.")
        break
