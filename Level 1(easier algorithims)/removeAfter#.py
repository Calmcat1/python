def remove_url_anchor(url):
    output = ""
    n = len(url)

    if "#" in url:
       for i in range (url.index("#") - 1):
           output += url[i]
    else:
        for i in range(n):
            output += url[i]
            
    return output
           
           




print(remove_url_anchor("this is me # 1"))


