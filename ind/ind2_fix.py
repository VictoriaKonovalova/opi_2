#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Вариант 6
Напишите программу, которая будет
способствовать дешифрации текста путем вывода на экран частоты появления разных букв.
При этом пробелы и знаки препинания должны быть проигнорированы. Также не
должен учитываться регистр, то есть символы a и A должны восприниматься как одна буква.
Имя файла для анализа пользователь должен передавать программе посредством
аргумента командной строки. Если программе не удастся открыть файл для анализа или
аргументов командной строки будет слишком много, на экране должно быть отображено
соответствующее сообщение об ошибке.
"""
# импортируем системный модуль
import sys

# Отслеживаем,чтобы программа обязательно запускалась с одним переданным параметром
if len(sys.argv) != 2:
    print("Ошибка!Имя файла необходимо передать в качестве аргумента.")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    inf = f.read()
    # Открываем на чтение файл, имя которого было передано в командной строке
    inf = open(sys.argv[1], "r", encoding="utf-8")
    frequence = dict()  # создаю пустой словарь
    line = inf.readline()
    while line != "":
        line = line.replace(".", " ")
        line = line.replace(",", " ")
        line = line.replace(":", " ")
        line = line.replace("!", " ")
        line = line.replace("-", " ")
        line = line.replace("?", " ")
        line = line.replace(" ", "")
        line = line.lower()
        line = line.rstrip()
        for letter in line:
            if letter in frequence:
                frequence[letter] += 1
            else:
                frequence[letter] = 1
        line = inf.readline()
    inf.close()
    for letter in frequence:
        print(letter, ":", frequence[letter])
