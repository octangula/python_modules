# rika
# py 3.10
# returns all combinations of `chars` that are `length` characters long, neat solution without any other modules

def combs(chars, length):

    total = []

    for i in range(len(chars) ** length):
        index = i
        characters = []
        string = ""
        for j in range(length):
            string += chars[index % len(chars)]
            index = int(index / len(chars))
        total.append(string)

    return total
