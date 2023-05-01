import string

a = string.ascii_uppercase[3:] + string.ascii_uppercase[:3]

tt = str.maketrans(string.ascii_lowercase, a)

x = input("put sentences to encrypt:")
print(x.translate(tt))
