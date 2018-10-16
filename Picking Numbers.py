
n = int(input())

l1 = [int(i) for i in input().split()]

ans = 0

for x in l1:

    xs = l1.count(x)
    increments = l1.count(x+1)

    if xs + increments > ans:
        ans = xs + increments

    decrements = l1.count(x-1)

    if xs + decrements > ans:
        ans = xs + decrements

print(ans)



