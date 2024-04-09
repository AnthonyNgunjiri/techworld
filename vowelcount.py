#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence.
#eg " Hello World " => returns
# Prompt the user to input a sentence right at the start
sentence = input("Enter a sentence: ")
def count_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    sentence = sentence.lower()
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count
print(f"The number of vowels in the sentence '{sentence}' is: {count_vowels(sentence)}")


