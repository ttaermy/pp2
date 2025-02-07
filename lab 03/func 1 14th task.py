import random

# Task 1: Generate all permutations of a string
def next_permutation(s, ans, results):
    if len(s) == 0:
        results.append(ans)
        return
    for i in range(len(s)):
        ch = s[i]
        L_substr = s[0: i]
        R_substr = s[i + 1:]
        next_permutation(L_substr + R_substr, ans + ch, results)

# Task 2: Reverse words in a sentence
def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

# Task 3: Detect "369" sequence in a list
def has_369(array):
    pattern = [3, 6, 9]
    index = 0
    for num in array:
        if num == pattern[index]:
            index += 1
        if index == len(pattern):
            return True
    return False

# Task 4: Print a histogram
def histogram(lst):
    for num in lst:
        print('*' * num)

# Task 5: Guess the number game
def guess_game():
    name = input("Hello! What is your name? ")
    rand_num = random.randint(1, 35)
    print("Well", name, "I am thinking of a number between 1 and 35.")

    x = -1
    cnt = 0

    while x != rand_num:
        cnt += 1
        try:
            x = int(input("Take a guess! "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if x < rand_num:
            print("Too low!")
        elif x > rand_num:
            print("Too high!")
        else:
            print("Good job", name, "You guessed my number in", cnt, "guesses!")

# Main menu function
def main():
    while True:
        print("\n===== My Python Project =====")
        print("1. Play Guess the Number")
        print("2. Generate Histogram")
        print("3. Check for '369' Sequence")
        print("4. Reverse Words in a Sentence")
        print("5. Find String Permutations")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            guess_game()
        elif choice == "2":
            lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
            histogram(lst)
        elif choice == "3":
            nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
            print("Contains '369' in order:", has_369(nums))
        elif choice == "4":
            sentence = input("Enter a sentence: ")
            print("Reversed:", reverse_words(sentence))
        elif choice == "5":
            s = input("Enter a string: ")
            results = []
            next_permutation(s, "", results)
            print("Permutations:", results)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number from 1 to 6.")

# Run the main program
if __name__ == "__main__":
    main()
