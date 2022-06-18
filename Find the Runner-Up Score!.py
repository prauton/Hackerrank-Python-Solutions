n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
for x in arr:
    if x != max(arr):
        print(x)
        break
