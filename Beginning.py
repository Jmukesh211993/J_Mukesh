print("Let the learning journey begins")
career = "Data Engineer"
print(career)
experience = 3
print(type(experience))
x = y = z = 7
y = 8
print(x, y, z)
def my_function():
 f = 2 
 return f 
print(my_function())


def your_function():
 a = 555
 print(a)
 your_function()



word = input("Enter the word: ")

vowels = "aeiouAEIOU"
vowel_count = 0


for char in word:
    
    if char in vowels:
        
        print(char)

        vowel_count += 1


print("Number of vowels:", vowel_count)

def trim_text(input_text):
    trimmed_text = input_text.rstrip()
    return trimmed_text

# Get user input
user_input = input("Enter a text with trailing spaces: ")

# Trim the text
result = trim_text(user_input)

# Display the result
print("Trimmed text:", repr(result))
