def reverse(num):
    num = str(num)
    num_len = len(num)
    text = ""
    while len(text) < num_len:
        text += num[-1]
        num = num[:-1]
    return text

print(reverse(int(input("Number: "))))