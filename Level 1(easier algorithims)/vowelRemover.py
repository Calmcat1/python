def shortcut(s):
    vowels = ['a','e','i','o','u']
    output = ""
    for char in s:
        if char in vowels:
            char = ""
        output += char
    return output
    
        
       
    
            

print(shortcut("hey its me"))