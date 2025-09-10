'''
Here's the situation: You work for a company where salespeople
receive commissions of 13% on their total sales,
and your boss wants you to help the salespeople calculate
their commissions by creating a program that asks them their
name and how much they've sold this month.
Your program will respond with a sentence that includes their
name and the commission amount
they're entitled to.
'''
name = input("what's your name?\n")
sold = float(input("Write your balance for the month\n"))
commission = sold * 0.13
print (f"Hi! {name} your commission balance is: ${commission}")