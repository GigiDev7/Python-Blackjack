import random

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

my_cards = [random.choice(cards),random.choice(cards)]
dealer_cards = [random.choice(cards),random.choice(cards)]

sum_my = sum(my_cards)
sum_dealer = sum(dealer_cards)

print(my_cards,dealer_cards[0])



def bj():
    game_finished = False
    global sum_my
    if  game_finished:
        return
    
    choice = input('press h to hit or f to finish ')
    
    if choice == 'h':
        new_card = random.choice(cards) 
        if new_card == 11:
            if sum_my + 11 > 21:
                my_cards.append(1)
                sum_my += 1
            else:
                my_cards.append(new_card)
                sum_my += 11
        else:
            my_cards.append(new_card)
            sum_my += new_card
        print(my_cards,dealer_cards[0])

        if sum_my >= 21:
            game_finished = True
        else:
            bj()
    else:
        game_finished = True
            
    
bj()

if sum_my > 21 or sum_my < sum_dealer:
    print('you lost',my_cards,dealer_cards)
elif sum_my == sum_dealer:
    print('draw',my_cards,dealer_cards)
else:
    print('you won',my_cards,dealer_cards)

