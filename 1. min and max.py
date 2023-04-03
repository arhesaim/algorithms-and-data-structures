nums = [2,3,9, 9, 4,5,6,1,1,2,9,1,8,6]
elements = {}
elementNum = 0
max = nums[0]
min = nums[0]

choice = input("1. max \n2. min\n")

if choice == "1":
    for i in nums:
        if i > max:
            max = i
    for i in nums:
        if i == max:
            elements[elementNum] = i
        elementNum += 1
    for key in elements:
        print(f"index: {key}, number: {elements[key]}")
elif choice == "2":
    for i in nums:
        if i < min:
            min = i
    for i in nums:
        if i == min:
            elements[elementNum] = i
        elementNum += 1
    for key in elements:
        print(f"index: {key}, number: {elements[key]}")