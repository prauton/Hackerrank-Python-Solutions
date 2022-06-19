y,z = map(int, input().split())
for i in range(1, y, 2):
    print((i * ".|.").center(z,"-"))
print("WELCOME".center(z, "-"))
for i in range(y-2, -1, -2):
    print((i * ".|.").center(z, "-"))
