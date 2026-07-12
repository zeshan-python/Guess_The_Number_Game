import random

# High Score
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except:
    high_score = 0

# Total Wins
try:
    with open("wins.txt", "r") as file:
        total_wins = int(file.read())
except:
    total_wins = 0


while True:

    print("\n🎮 ===== GUESS THE NUMBER GAME =====")
    print("1. Easy (1 - 10)")
    print("2. Medium (11 - 50)")
    print("3. Hard (51 - 100)")

    choice = input("Choose difficulty (1/2/3): ")

    if choice == "1":
        secret_number = random.randint(1, 10)
        attempts = 5

    elif choice == "2":
        secret_number = random.randint(11, 50)
        attempts = 7

    elif choice == "3":
        secret_number = random.randint(51, 100)
        attempts = 10

    else:
        print("❌ Invalid choice!")
        continue

    hint_used = False

    print(f"\n🏆 High Score: {high_score}")
    print("🎯 Game Started!")

    while attempts > 0:

        guess = int(input("Enter your guess: "))

        if not hint_used:
            hint = input("Need a hint? (yes/no): ").lower()

            if hint == "yes":
                if secret_number % 2 == 0:
                    print("💡 Hint: The number is Even.")
                else:
                    print("💡 Hint: The number is Odd.")

                hint_used = True

        if guess == secret_number:
            print("\n🎉 Congratulations! You guessed the number.")
            print("🏆 You won!")

            total_wins += 1

            with open("wins.txt", "w") as file:
                file.write(str(total_wins))

            print(f"❤️ Total Wins: {total_wins}")

            if attempts >= 4:
                print("🥇 Gold Medal!")
            elif attempts >= 2:
                print("🥈 Silver Medal!")
            else:
                print("🥉 Bronze Medal!")

            if attempts > high_score:
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