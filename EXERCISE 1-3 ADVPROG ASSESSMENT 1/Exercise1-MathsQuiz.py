import random

# ------------------------------------------------------------
# Function: displayMenu
# ------------------------------------------------------------
def displayMenu():
    print("\nDIFFICULTY LEVEL")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")
    while True:
        try:
            choice = int(input("Select difficulty (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")


# ------------------------------------------------------------
# Function: randomInt
# ------------------------------------------------------------
def randomInt(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)


# ------------------------------------------------------------
# Function: decideOperation
# ------------------------------------------------------------
def decideOperation():
    return random.choice(['+', '-'])


# ------------------------------------------------------------
# Function: displayProblem
# ------------------------------------------------------------
def displayProblem(num1, num2, op):
    while True:
        try:
            ans = int(input(f"{num1} {op} {num2} = "))
            return ans
        except ValueError:
            print("Please enter a valid integer.")


# ------------------------------------------------------------
# Function: isCorrect
# ------------------------------------------------------------
def isCorrect(userAns, num1, num2, op):
    correctAns = num1 + num2 if op == '+' else num1 - num2
    if userAns == correctAns:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Incorrect. The correct answer was {correctAns}.")
        return False


# ------------------------------------------------------------
# Function: displayResults
# ------------------------------------------------------------
def displayResults(score):
    print("\n-------------------------------")
    print(f"FINAL SCORE: {score}/100")
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    print(f"GRADE: {grade}")
    print("-------------------------------\n")


# ------------------------------------------------------------
# Function: playQuiz
# ------------------------------------------------------------
def playQuiz():
    level = displayMenu()
    score = 0
    for i in range(1, 11):
        print(f"\nQuestion {i}:")
        num1 = randomInt(level)
        num2 = randomInt(level)
        op = decideOperation()

        # First attempt
        answer = displayProblem(num1, num2, op)
        correctAns = num1 + num2 if op == '+' else num1 - num2
        if answer == correctAns:
            print("✅ Correct on first try!")
            score += 10
            continue

        # Second attempt
        print("Try again...")
        answer = displayProblem(num1, num2, op)
        if answer == correctAns:
            print("✅ Correct on second try!")
            score += 5
        else:
            print(f"❌ Wrong again. Correct answer: {correctAns}")

    displayResults(score)


# ------------------------------------------------------------
# Main program loop
# ------------------------------------------------------------
def main():
    print("=== ARITHMETIC QUIZ PROGRAM ===")
    while True:
        playQuiz()
        again = input("Would you like to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye.")
            break


# ------------------------------------------------------------
if __name__ == "__main__":
    main()