def driving_cost(miles_per_gallon, dollars_per_gallon, x):
    y = (dollars_per_gallon * x) / miles_per_gallon
    # print('{:.2f}'.format(y))
    return y


if __name__ == '__main__':
    mi_per_gal = float(input())
    dol_per_gal = float(input())

    if (mi_per_gal >= 0) and (dol_per_gal >= 0):
        cost = driving_cost(mi_per_gal, dol_per_gal, 10)
        print('{:.2f}'.format(cost))
        cost = driving_cost(mi_per_gal, dol_per_gal, 50)
        print('{:.2f}'.format(cost))
        cost = driving_cost(mi_per_gal, dol_per_gal, 400)
        print('{:.2f}'.format(cost))
    else:
        print("driving_cost({},{},{}) does not exist".format(mi_per_gal, dol_per_gal, 10))
#   print_book_description(title='The Lord of the Rings', publisher='George Allen & Unwin',
#                       year=1954, author='J. R. R. Tolkien', version=1.0,
#                       num_pages=456, num_chapters=22)
#     #output 10. Exceptions 50 400
#  mi        dol
# ------- x ------ = cost
#  gal       gal
# Type your code here.


