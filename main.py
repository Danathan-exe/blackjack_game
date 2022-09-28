# #input the two cards
Letterc = [  #creating arrays for the Letter options.
    'a', 'j', 'k', 'q'
]
#input the two cards
while True:
  card1 = input("what is your first card")
  try:
    card1 = int(card1)
  except:
    card1 = card1.lower()

  if type(card1) == int:
    if card1 > 10:
      print("This number is too high. Please enter a new number.")
    else:
      break
  else:
    if card1 in Letterc:
      break
    else:
      print("This is not a correct card letter. Please enter from letters: A, J, K, or Q")
  



while True:
  card2 = input("what is your second card")
  try:
    card2 = int(card2)
  except:
    card2 = card2.lower()

  if type(card2) == int:
    if card2 > 10:
      print("This number is too high. Please enter a new number.")
    else:
      break
  else:
    if card2 in Letterc:
      break
    else:
      print("This is not a correct card letter. Please enter from letters: A, J, K, or Q")


while True:
    try:
        card1 = int(card1)
        break

    except:
        card1 = card1.lower()
        break
#setting the card Value for A

while True:
    try:
        card2 = int(card2)
        break
    except:
        card2 = card2.lower()
        break
#setting the card Value for A

# while True:
# if type(card1) == int
if card1 in Letterc:
    # if the card is an ace, the player can select 11 or 1
    if card1 == 'a':
        ls = [1, 11]
        # loop until they select 11 or 1 to assure proper rules
        while True:
            card1val = int(
                input("Do you want your ace (card #1) to be an 11 or a 1?"))
            if card1val not in ls:
                print("This was not a 1 or an 11. Please try again.")
            else:
                break
    else:
        card1val = 10
else:
    card1val = card1

#setting the card Value for A
if card2 in Letterc:
    # if the card is an ace, the player can select 11 or 1
    if card2 == 'a':
        ls = [1, 11]
        # loop until they select 11 or 1 to assure proper rules
        while True:
            card2val = int(
                input("Do you want your ace (card #2) to be an 11 or a 1?"))
            if card2val not in ls:
                print("This was not a 1 or an 11. Please try again.")
            else:
                break
    else:
        card2val = 10
else:
    card2val = card2
  
score = card1val + card2val
print("Your score is:")
print(score)
print()

if card1 == 8 and card2 ==8:
  print("Split!")
elif score == 17 and card1 or card2 == 'a':
  print("Hit!")
elif score == 17 and score == 20 and score == 18 and score ==19:
    print("Stay")

elif score == 21:
  print("Blackjack!")


    