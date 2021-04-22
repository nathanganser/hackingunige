# Define grammar
data = {
    "S": ["ACB"],
    "C": ["ACB", "S", "e"],
    "B": ["C"],
    "A": ["ab"]
}

use = ["P", "Q", "R", "M"]
# S can only happen once
data["S0"] = "S"

p_count = -1
# Remove
for el in data.copy():
    print(f'looking at key {el}')
    for array in data[el]:
        p_count = -1
        print(f'looking at array {array}')
        for letter in array:
            p_count += 1
            print(f'looking at letter {letter}')
            if letter.islower() and letter != "e":
                print('is lower case!')
                data[use[0]] = letter
                print(f'need to replace {array[p_count]}')
                array[p_count].replace(letter, use[0])
                print(f'letter is now {array[p_count]}')
                use.remove(use[0])

print(data)
print(use)