#1 A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def my_function(grams):
    ounces = grams * 28.3495231
    return ounces

grams_input = float(input("Enter the weight in grams: "))
print("weight in ounces: ", my_function(grams_input))
    
#2Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def my_function(farenheit):
    celc = (5 / 9) * (farenheit - 32)
    return celc

farenheit_input = float(input("Enter the temperature: "))
print("temperature in celcius: ", my_function(farenheit_input))

#3Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2* chickens + 4* rabbits == numlegs:
            return chickens, rabbits
    return "No solution found"

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print("Chickens:", chickens, "Rabbits:", rabbits)

#4You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

import math
def filter_prime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+ 1):
        if n % i == 0:
            return False
    return True

list_input = vector(input("Enter the list of numbers: "))
print(filter_prime(list_input))

#5Write a function that accepts string from user and print all permutations of that string.

def next_permutation(s, ans, results):
    if len(s) == 0:
        results.append(ans)
        return
    for i in range(len(s)):
        ch = s[i]
        L_substr = s[0 : i]
        R_substr = s[i + 1 : ]
        remaining = L_substr + R_substr
        next_permutation(remaining, ans + ch, results)

s = input()
results = []
next_permutation(s, "", results)
print(results) 

#6Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

def reverse_sentence(sentence):
    words = sentence.split() 
    reversed_words = " ".join(reversed(words))  
    return reversed_words

user_input = input("Enter a sentence: ")
print(reverse_sentence(user_input))

#7

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#8

def has_007(array):
    pattern = [0, 0, 7]  
    index = 0  

    for num in array:
        if num == pattern[index]: 
            index += 1
        if index == len(pattern): 
            return True
    return False

nums = list(map(int, input().split()))
print(has_007(nums))

#9

import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

#10

def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#11

def is_palindrome(s):
    s = s.replace(" ", "").lower()  
    return s == s[::-1]  

#12

def histogram(lst):
    for num in lst:
        print('*' * num)

#13

import random

def guess_game():
    name = input("Hello! What is your name? ")  
    rand_num = random.randint(1, 20)  
    print("Well", name, "I am thinking of a number between 1 and 20.")

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

guess_game()