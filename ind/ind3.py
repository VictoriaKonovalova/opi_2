#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Программа, которая создает директорию, затем создает в этой директории файл с некоторым текстом.
Затем  переименовает этот файл и удаляет его. После этого программа  удаляет созданную ранее директорию.
В задаче используются функций модуля os, а именно mkdir(), rename(), remove() и rmdir().
"""
import os

if __name__ == "__main__":
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
