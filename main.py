n = int(input())
user_str = input()
list1 = [i for i in range(n+1)]
for j in range(len(list1)):
    if 0 == j%2:
        list1[j] = user_str
print(list1)