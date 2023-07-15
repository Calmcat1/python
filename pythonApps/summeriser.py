
# this is the function that handles the opening of files
def fileopener(file):
    openedFile = open(file,"r+")
    print(openedFile.read())