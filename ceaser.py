def caesar(text):
    a = ["a", "b" ,"c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    cypher = []
    for i in text:
        ind = a.index(i)
        try:
            bukva = a[ind+13]
        except:
            bukva = a[ind-13]

        cypher.append(bukva)
    return ''.join(cypher)

print caesar("hello")