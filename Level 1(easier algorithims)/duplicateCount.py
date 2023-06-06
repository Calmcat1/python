def duplicate_count(text):
    arr = []
    countArr = []
    nonDuplicateArr = []
    for char in text:
        arr.append(char)
        countArr.append(arr.count(char))
    return arr, countArr


print(duplicate_count("hey this is one"))

        