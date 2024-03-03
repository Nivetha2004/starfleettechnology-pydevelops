card_no = list(input("Enter a card number: ").replace(' ', '').replace('-', ''))
last_no = card_no.pop()
card_no.reverse()
operated_digits = []
for index, digit in enumerate(card_no):
    digit = int(digit)
    if index % 2 == 0:
        two_digit = digit * 2
        if two_digit > 9:
            two_digit = two_digit - 9
        operated_digits.append(two_digit)
    else:
        operated_digits.append(digit)
total = int(last_no) + sum(operated_digits)
if total % 10 == 0:
    print("Valid!")
else:
    print("Invalid!")

