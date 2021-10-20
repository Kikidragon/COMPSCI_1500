def kilo_to_pounds(kilos):
    # This statement intentionally has an error.
    return (kilos * 2.204)


if __name__ == '__main__':
    kilos = float(input());

    pounds = kilo_to_pounds(kilos);
    print(pounds, "lbs");