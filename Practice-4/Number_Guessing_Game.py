secret = 8
count = 0
while count < 5:
    guess = int(input())
    count += 1
    if guess == secret:
        print("Correct")
        break
    elif guess < secret:
        print("Too Low")
    else:
        print("Too High")
if count == 5 and guess != secret:
    print("Game Over")