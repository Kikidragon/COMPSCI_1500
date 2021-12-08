def selection_sort_descend_trace(numbers):
    for index in range(len(numbers) - 1):
        largest_index = index
        for n in range(index + 1, len(numbers)):
            if numbers[n] > numbers[largest_index]:
                largest_index = n
        numbers[index], numbers[largest_index] = numbers[largest_index], numbers[index]
        print(' '.join([str(x) for x in numbers]),'')
    return numbers


if __name__ == '__main__':
    number_list = [int(value) for value in input().split()]
    selection_sort_descend_trace(number_list)


# def selection_sort_descend_trace(numbers):
#     i = len(numbers)
#     print('Output: ')
#     for num in range(0, i - 1):
#         val = numbers[num]
#         start = num + 1
#         end = i
#         t = 0
#         for j in range(start, end):
#             if val < numbers[j]:
#                 x = j
#                 val = numbers[j]
#                 t = 1
#             if t == 1:
#                 y = numbers[num]
#         numbers[num] = val
#         numbers[x] = y
#     for p in range(i):
#         print(numbers[p], end=' ')
#         print('\n')
#     # for i in numbers:
#     #     print(i)
#     # for i in range(len(numbers) - 1):
#     #     index_smallest = i
#     #     for j in range(i + 1, len(numbers)):
#     #         if numbers[j] < numbers[index_smallest]:
#     #             index_smallest = j
#     #     temp = numbers[i]
#     #     numbers[i] = numbers[index_smallest]
#     #     numbers[index_smallest] = temp
#     #
#
#     #    for i in range(len(numbers)):
#     #     min = i
#     #     for j in range(i+1, len(numbers)):
#     #         if numbers[min] < numbers[j]:
#     #             min = j
#     #             numbers[i], numbers[min] = numbers[min], numbers[i]
#     #             print(numbers)
#
#
# if __name__ == "__main__":
#
#     numbers = []
#     nums = input()
#     nums_split = nums.split()
#     for i in nums_split:
#         int(i)
#         numbers.append(i)
#
#     selection_sort_descend_trace(numbers)
#
# # while a <= triangle_height:
# #     z = a
# #     while z != 0:
# #         print(triangle_char, end=' ')
# #         z -= 1
# #     print()
# #     a += 1

