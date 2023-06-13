def printer_error(s):
    errorArr = []
    acceptedChars = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    for char in s:
        if char in acceptedChars:
            continue
        else:
            errorArr.append(char)
    return f"{len(errorArr)}/{len(s)}"


print(printer_error("abcdefghijklmnopqrstuvwxyz"))