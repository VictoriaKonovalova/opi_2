import os

filename = "ind3.txt"
directory = "new"
filepath = directory + "/" + filename

print(filepath)

# Создаем директорию
os.mkdir(directory)

# Создаем файл
with open(filepath, "w") as f:
    f.write("Hello!!!")

# Переименовываем файл
os.rename(filepath, directory + "/ind3_new.txt")

# Удаляем файл
os.remove(directory + "/ind3_new.txt")

# Удаляем директорию
os.rmdir(directory)
