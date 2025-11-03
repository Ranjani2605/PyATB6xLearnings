#1) Print even numbers between 1 and 20
for i in range(1,21):
    if i % 2 == 0:
        print(i)

#2) Print numbers from 10 down to 1
for j in range(10,0,-1):
    print(j)

#3) Skip numbers divisible by 3, from (0,100)
for k in range(0,100):
    if k%3 == 0:
        continue
    print(k)