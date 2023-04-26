def find_occurrences(T, P):
    n = len(T)
    m = len(P)
    occurrences = []
    found = False
    for i in range(n - m + 1):
        if T[i:i+m] == P:
            occurrences.append(i)
            found = True
    return occurrences, found

T = "I like this cat, this cat is my pet"
P = "cat"
occurrences, found = find_occurrences(T, P)
if found:
    print(f"The pattern {P} was found at positions: {occurrences}")
else:
    print(f"The pattern {P} was not found in the text.")