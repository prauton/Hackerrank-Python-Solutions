def count_substring(string, sub_string):
    n = len(sub_string)
    count, i = 0, 0
    while i <= len(string): 
        if string[i:n] == sub_string:
            count = count+1
        i = i +1
        n = n + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
