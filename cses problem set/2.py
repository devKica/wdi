n = int(input())
sum_numbers = sum([int(x) for x in input().split(" ")])

print(int(n*(n+1)/2-sum_numbers))
