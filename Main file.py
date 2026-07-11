import random

try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except:
    high_score = 999999

while True:
    print("\n🎮 ===== GUESS THE NUMBER GAME =====")
    print("1. Easy (1 - 10)")
    print("2. Medium (1 - 50)")
    print("3. Hard (1 - 100)")

    choice = input("Choose difficulty (1/2/3): ")

    if choice == "1":
        secret_number = random.randint(1, 10)
        attempts = 5

    elif choice == "2":
        secret_number = random.randint(1, 50)
        attempts = 7

    elif choice == "3":
        secret_number = random.randint(1, 100)
        attempts = 10

    else:
        print("❌ Invalid choice! Try again.")
        continue

    print(f"\n🏆 High Score: {high_score}")
    print("🎯 Game Started!")

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("\n🎉 Congratulations! You guessed the number.")
            print("🏆 You won!")

            if attempts < high_score:
                high_score = attempts

                with open("highscore.txt", "w") as file:
                    file.write(str(high_score))

                print("🌟 New High Score!")

            break

        elif guess < secret_number:
            print("📉 Too low!")

        else:
            print("📈 Too high!")

        attempts -= 1

        if attempts > 0:
            print(f"💡 Attempts left: {attempts}")

    if attempts == 0:
        print("\n💀 You lost!")
        print(f"✅ The correct number was: {secret_number}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n👋 Thanks for playing!")
        print("Allah Hafiz! ❤️")
        break