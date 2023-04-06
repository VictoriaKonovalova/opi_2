#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Вариант 6
Написать программу, которая считывает текст из файла и выводит на экран только
предложения, не содержащие запятых.
"""

if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as fileptr:
        sentences = fileptr.readlines()
        for sentence in sentences:
            if "," not in sentence:
                print(sentence)
