k = 3666
hours = k // 3600
print(hours)
minute = (k // 60) % 60
print(minute)
second = k % 60
print(second)

print(str(hours) + ":" + str(minute) + ":" + str(second))