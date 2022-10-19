import string

y = string.ascii_letters
def decipher():
    r = ""
    x, q = eval(input("please input the code and key (code in"") :"))
    xx = [t for t in x]
    for c in xx :
        if c in y :
            l = y.find(c)
            k = (l-q) % 26
            m = y[k]
            r += m
        else:
            r += c
    return r
print(decipher())

