# use open function to read the content of a file
f = open('sample.txt', 'r')
# read is a function here. the default mode is read.
data = f.read()
# data = f.read(5)
print(data)
f.close()
