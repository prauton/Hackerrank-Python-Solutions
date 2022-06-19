import string
def print_rangoli(size):
    
    design = string.ascii_lowercase
    lst = []
    for i in range(n):
        s = "-".join(design[i:n])
        lst.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(lst[:0:-1]+lst))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
