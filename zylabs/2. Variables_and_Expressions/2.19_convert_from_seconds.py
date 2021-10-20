''' Type your code here '''

seconds = int(input())

second = seconds % 60
minutes = (seconds % 3600) / 60
hours = seconds / 3600


print("Hours:", int(hours))
print("Minutes:", int(minutes))
print("Seconds:", int(second))

#print("Hours:", hours // 1)
#print("Minutes:", minutes // 1)
#print("Seconds:", second // 1)