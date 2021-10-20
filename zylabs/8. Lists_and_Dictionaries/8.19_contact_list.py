contact = input()
contacts = contact.split()
contact_list = {}
find = input()
# person who you want to find the number of
x = len(contacts)
# print(x)

for i in range(len(contacts)):
    if (contacts[i] == find):
        break

# s = input()
# name = input()
# splits = s.split(" ")
# i = 0
# for i in range(len(splits)):
#   if(splits[i] == name):
#       break
# print(splits[i+1])


# FIXME
# while x > 0:
#     x -= 1
#     # a = contacts[len(contacts) - len(contacts)]
#     # b = contacts[len(contacts) - x]
#     contact_list[contacts[len(contacts)-len(contacts)]] = contacts[len(contacts)-((len(contacts)-1))]
# #     # add to a dictionary


print(contacts[i + 1])
# print(contact_list(find))    


# user_input = input()
# entries = user_input.split(',')
# country_pop = {}

# for pair in entries:
#     split_pair = pair.split(':')
#     country_pop[split_pair[0]] = split_pair[1]