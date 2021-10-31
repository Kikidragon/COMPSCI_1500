def reverse_list(letters):
    # # for i in letters:
    #   values.reverse()
    # return values
    # letters.reverse()
    letters = letters[::-1]
    return letters


if __name__ == '__main__':
    ch = ['a', 'b', 'c']
    print(reverse_list(ch))  # Should print ['c', 'b', 'a']