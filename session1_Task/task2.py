text = input("Enter your text: ")

words = 0
letters = 0
sentences = 0

for i in text:

    if i == " ":
        words += 1

    elif i == "." or i == "!" or i == "?":
        sentences += 1

    elif i.isalpha():
        letters += 1

words +=1

grade = 0.0588 * (letters / words * 100) - 0.296 * (sentences / words * 100) - 15.8

if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print("Grade ", round(grade))