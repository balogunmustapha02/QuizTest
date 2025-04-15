# A simple quiz program that uses conditional statements to evaluate users' responses and provide feedback
# This quiz contains true or false questions on shapes

print("Welcome to Simple Quiz by Balogun Mustapha")
print("Attempt all questions")
score = 0

# Question 1
print("Question 1: A quadrilateral shape is a shape with four sides.")
print("a) True")
print("b) False")
answer = input("Input your answer a/b: ")
if answer == "a":
    print("Correct")
    score += 1
else:
    print("Incorrect. Correct answer is a")

# Question 2
print("Question 2: A triangle is a shape with six sides.")
print("a) True")
print("b) False")
answer = input("Input your answer a/b: ")
if answer == "b":
    print("Correct")
    score += 1
else:
    print("Incorrect. Correct answer is b")

# Question 3
print("Question 3: A square is a shape with four equal sides.")
print("a) True")
print("b) False")
answer = input("Input your answer a/b: ")
if answer == "a":
    print("Correct")
    score += 1
else:
    print("Incorrect. Correct answer is a")

# Question 4
print("Question 4: A rectangle is not a quadrilateral shape.")
print("a) True")
print("b) False")
answer = input("Input your answer a/b: ")
if answer == "b":
    print("Correct")
    score += 1
else:
    print("Incorrect. Correct answer is b")

# Question 5
print("Question 5: A triangle with all its sides equal is known as an equilateral triangle.")
print("a) True")
print("b) False")
answer = input("Input your answer a/b: ")
if answer == "a":
    print("Correct")
    score += 1
else:
    print("Incorrect. Correct answer is a")

# Print final score
print(f'Your final score: {score}/5')
