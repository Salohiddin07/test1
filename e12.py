# 1-task
# favourite_foods = ['Lavash', 'Osh']
# favourite_foods.insert(2, 'Mastava')
# favourite_foods.append('Grechka')

# print(favourite_foods)

# 2-task

l = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']

kichik = []
kotta = []

for i in l:
    if i.islower():
        kichik.append(i)

for k in l:
    if k.isupper():
        kotta.append(k)


print(kichik)



