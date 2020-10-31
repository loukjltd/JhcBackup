#Question 4
#Josh net182 201810701580043

bo1 = True
let = {'K': 'King', 'Q': 'Queen', 'J': 'Jack', 'A': 'Ace'}
while bo1 == True:
    text = input('Enter a card letter:')
    if text.upper() in let :
        print(let[text.upper()])
        bo1 = False
    elif text in let:
        print(let[text])
        bo1 = False
    else:
        print('Try again.')