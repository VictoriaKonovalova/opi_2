# open the file2.txt in append mode. Create a new file if no such file exists.
with open("file2.txt", "w") as filept:
    # appending the content to the file
    filept.write(
        "Python is the modern day language. It makes things so simple.\n"
        "It is the fastest-growing programing language"
    )
