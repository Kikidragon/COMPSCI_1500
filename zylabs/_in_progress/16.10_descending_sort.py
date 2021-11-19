# FIXME UNFINISHED

# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
    for i in numbers:
        print(i)
    # for i in range(len(numbers) - 1):
    #     index_smallest = i
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[j] < numbers[index_smallest]:
    #             index_smallest = j
    #     temp = numbers[i]
    #     numbers[i] = numbers[index_smallest]
    #     numbers[index_smallest] = temp
    #


if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = []
    nums = input()
    nums_split = nums.split()
    for i in nums_split:
        int(i)
        numbers.append(i)

    selection_sort_descend_trace(numbers)

# while a <= triangle_height:
#     z = a
#     while z != 0:
#         print(triangle_char, end=' ')
#         z -= 1
#     print()
#     a += 1