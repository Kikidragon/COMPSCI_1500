def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s
    else:
        first_char = s[0]
        all_else = s[1:]
        reverse_all_else = reverse_string(all_else)
        return reverse_all_else + first_char
# done in class
# EASIER WAY HAHA return s[::-1]

if __name__ == "__main__":
    in_str = input()
    result_str = reverse_string(in_str)
    print('Reverse of "' + in_str +  '" is "' + result_str + '".')