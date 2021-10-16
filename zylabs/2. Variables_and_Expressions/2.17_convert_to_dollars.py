''' Type your code here. '''
quarter = int(input())
dime = int(input())
nickel = int(input())
penny = int(input())

dollar = ((quarter * 25) + (dime * 10) + (nickel * 5) + (penny * 1)) / 100
#print(f'Amount: ${dollar:.2f}')