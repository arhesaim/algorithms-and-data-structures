# вариант 5

def replace_chars(s):
    result = ""
    for c in s:
        if c == "я":
            result += " "
        else:
            result += chr(ord(c) + 1)
    return result

s = "Якутская яшма явно ярче японской."
result = replace_chars(s)
print(result) 