import wolframalpha
import json


def convert(text):
    ok = text.replace("&&", "*")
    final = ok.replace("||", "+")
    print(final)



def generate_table(length):
    table = []
    for i in range(0, 2 ** length, +1):
        table.append([])
    # first column
    for i in range(0, len(table), +1):
        if i <= len(table) / 2:
            table[i].append(0)
        else:
            table[i].append(1)
    # second column
    for i in range(0, len(table), +1):
        if i <= len(table) / 4:
            table[i].append(0)
        else:
            table[i].append(1)


    print(table)




def askwolf(text):
    client = wolframalpha.Client("R54W9L-RW8HHWEA6U")
    res = client.query(text)
    for element in res:
        if element['@title'] == "Minimal forms":
            return element['@alt']


truth_table_3 = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
]

truth_table_4 = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0]
]


alphabet = ['A', 'B', 'C', 'D', 'E', 'F']


def get_max_terms(truth_table):
    solution = ""
    for row in truth_table:
        if row[-1] == 0:
            count = 0
            for element in row:
                if count < (len(row) - 1):

                    if element == 0:
                        solution += "!"

                    solution += alphabet[count]
                    if count < (len(row) - 2):
                        solution += " && "

                    count += 1
            solution += " || "

    print("!Q = " + solution)



def get_min_terms(truth_table):
    solution = ""
    for row in truth_table:
        if row[-1] == 1:
            count = 0
            for element in row:
                if count < (len(row) - 1):

                    if element == 0:
                        solution += "!"

                    solution += alphabet[count]
                    if count < (len(row) - 2):
                        solution += " && "

                    count += 1
            solution += " || "

    print(solution)
    convert(solution)



get_max_terms(truth_table_4)


def convert(text):
    ok = text.replace("&&", "*")
    final = ok.replace("||", "+")
    print(final)
    return final

convert("")

# http://www.32x8.com/var4.html build circuit and use Karnaugh
# https://www.dcode.fr/boolean-expressions-calculato simplify boolean statements

