def driving_cost(miles_per_gallon, dollars_per_gallon, x):
    money = (dollars_per_gallon / miles_per_gallon)
    y = (x * money)
    print('{:.2f}'.format(y))
    return y


if __name__ == '__main__':
    mi_per_gal = float(input())
    dol_per_gal = float(input())

    driving_cost(mi_per_gal, dol_per_gal, x=10)
    driving_cost(mi_per_gal, dol_per_gal, x=50)
    driving_cost(mi_per_gal, dol_per_gal, x=400)
#   print_book_description(title='The Lord of the Rings', publisher='George Allen & Unwin',
#                       year=1954, author='J. R. R. Tolkien', version=1.0,
#                       num_pages=456, num_chapters=22)
#     #output 10 50 400
#  mi        dol
# ------- x ------ = cost
#  gal       gal
# Type your code here.


