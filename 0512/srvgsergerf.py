dic = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15", "G": "16", "H": "17", "I": "34", "J": "18", "K": "19",\
       "L": "20", "M": "21", "N": "22", "O": "35", "P": "23", "Q": "24", "R": "25", "S": "26", "T": "27", "U": "28" ,"V": "29",\
       "W": "32", "X": "30", "Y": "31", "Z": "33"}
sum = 0
inp = input()
for i in range(len(inp)):
    sum += int(inp[i]) * (8 - i)
for letter, num in dic.items():
    if 10 - ((sum + int(num[0]) + int(num[1]) * 9) % 10) == int(inp[-1]):
        print(letter, end="")