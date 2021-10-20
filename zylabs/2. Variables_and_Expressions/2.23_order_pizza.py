''' Type your code here. '''
pizza = int(input())

sub = pizza * 9.99
tax = sub * 0.06
total = tax + sub

print("Subtotal: ${:.2f}".format(sub))
print("Total due: ${:.2f}".format(total))