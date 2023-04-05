import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome in paper, scissors and rock game!\n")
your_choice = int(input("Choose:\n0-rock,\n1-paper,\n2-scissors\n"))
print("You choose: ")
if your_choice == 0:
    print(rock)
elif your_choice == 1:
    print(paper)
elif your_choice == 2:
    print(scissors)
else:
    print("Wrong choice. Game over")

computer_choice = random.randint(0,2)
print("The computer choose: ")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if your_choice >= 3 or your_choice < 0:
    print("Wrong choice. Game over")
elif your_choice == 0 and computer_choice == 2:
    print("You win!")
elif your_choice == computer_choice:
    print("A draw!")
elif your_choice == 2 and computer_choice == 0:
    print("You loose!")
elif your_choice > computer_choice:
    print("You win!")
elif your_choice < computer_choice:
    print("You loose")



