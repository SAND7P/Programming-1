print("---------------------------")
secret_num=7
guess=int(input("Guess the number:"))
while guess!=secret_num:
    if guess<secret_num:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess the number:"))
print("Correct!!")
print("---------------------------")
