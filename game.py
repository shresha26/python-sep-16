import random

# number = random.randint(10,20)
# print(number)
# attempt = 0

# while False:
#   user_input = int(input("Enter number: "))
#   attempt = attempt + 1
#   if user_input == number:
#     print("Number matched in", attempt)
#     break
#   else:
#     print("Try again")

#   if attempt>=max_attempt:
#     print("Max attempt reached")
#     print("Number was", number)
#     break

# while False:
#   user_input = int(input("Enter number: "))
#   attempt = attempt + 1
#   if user_input == number:
#     print("Number matched in", attempt)
#     break
#   elif user_input>number:
#     print("Guess lower")
#   else:
#     print("Guess upper")



# while False:
#     user_input = int(input("Enter the number "))
#     attempt = attempt + 1
#     if user_input == number:
#         print("Number match in ", attempt)
#         play_again = input("Do you want to play again Y/N ").upper()
#         if play_again == "Y":
#             number = random.randint(10,50)
#             attempt = 0
#             print("Random number for loop", number)
#             print("Lets play again")
#         else:
#             break
#     else:
#         print("Try again")



# data = ["hello",1,2,1.5,"testing"]
# print(random.choice(data))


print("-----------------------------")

while True:
    data = ["R","P","S"]
    computer = random.choice(data)
    print(computer)
    user = input("Enter R/P/S ").upper()
    if user not in data:
        print("Please guess R/P/S only ")
        continue

    if user == computer:
        print("DRAW")
        break
    elif (
        (user == "R" and computer == "S")
        or (user == "S" and computer == "P")
        or (user == "P" and computer == "R")
    ):
       print("User Win")
    else:
        print("Computer Win")

    result = input("Do you want to play again ").lower()
    if result!="y":
        break