print("Welcome to my computer quiz!")

playing = input(" Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay let's play ;)")
score = 0


answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
answer = input("what does tv stand for")
if answer.lower() == " televison ":
    print("correct")
    score += 1
else:
    print("incorrect")
    

print("you got" + str(score) + "questions correct!")
print("you got" + str((score/ 1) * 100) + "%.")
#we can add our own questions by copying and pasting the first code
