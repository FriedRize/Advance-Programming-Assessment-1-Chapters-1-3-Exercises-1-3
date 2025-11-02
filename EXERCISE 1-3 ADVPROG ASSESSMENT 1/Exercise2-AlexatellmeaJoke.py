import random

def load_jokes(filename):
    jokes = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if '?' in line:
                setup, punchline = line.split('?', 1)
                jokes.append((setup.strip() + '?', punchline.strip()))
    return jokes

def tell_joke(jokes):
    joke = random.choice(jokes)
    print("\n" + joke[0])
    input("(Press Enter to hear the punchline...) ")
    print(joke[1] + "\n")

def main():
    jokes = load_jokes('randomJokes.txt')
    print("=== Alexa Joke Program ===")
    while True:
        cmd = input("Say 'Alexa tell me a joke' or 'quit': ").strip().lower()
        if cmd == 'quit':
            print("Goodbye!")
            break
        elif cmd == 'alexa tell me a joke':
            tell_joke(jokes)
        else:
            print("I didn't understand that.\n")

if __name__ == "__main__":
    main()