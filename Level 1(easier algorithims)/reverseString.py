#this algorithim reverses a string

def solution(string):
    output = ""
    for char in reversed(string):
        output += char
    return output

print(solution("hey its me"))